import boto3
from datetime import datetime
from functools import partial
import json

default_client = boto3.client("dynamodb", region_name="eu-west-2")
transactions_table = "qmbank-transactions"


# Gets all transactions for a given account using QUERY. Using the account_id. Gets all transactions where account is sender or recipient.
def get_account_transactions(account_id, client=default_client):
    # QUERY table
    response = client.scan(
        TableName=transactions_table,
        FilterExpression="sender_id = :account_id OR recipient_id = :account_id",
        ExpressionAttributeValues={":account_id": {"S": str(account_id)}},
    )

    transactions = response.get("Items", [])
    return transactions


def add_company_score(transaction):
    # The account number in a transaction should be valid.
    if "is_outgoing" not in transaction:
        return transaction

    item = default_client.get_item(
        TableName="qmbank-accounts",
        Key={"account_no": {"S": transaction["recipient_id"]}},
    )["Item"]

    if "company_category" not in item:
        return transaction

    scores = [
        int(item["company_env_scores"]["M"]["carbon_emissions"]["N"]),
        int(item["company_env_scores"]["M"]["waste_management"]["N"]),
        int(item["company_env_scores"]["M"]["sustainability_practices"]["N"]),
    ]
    transaction["score"] = sum(scores) / 30

    return transaction


def add_is_outgoing(account_id, transaction):
    if account_id == transaction["recipient_id"]:
        transaction["is_outgoing"] = False
    else:
        transaction["is_outgoing"] = True
    return transaction


def lambda_handler(event, context, client=default_client):
    # Gets account ID from path parameters. accounts/{id}/transactions
    account_id = event["pathParameters"]["id"]

    transactions = get_account_transactions(account_id, client)

    if not transactions:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "No transactions found for this account"}),
        }

    transactions.sort(key=lambda x: int(x["date"]["N"]), reverse=True)

    response = [
        {
            "recipient_id": transaction["recipient_id"]["S"],
            "recipient_name": transaction["recipient_name"]["S"],
            "sender_id": transaction["sender_id"]["S"],
            "sender_name": transaction["sender_name"]["S"],
            "amount": transaction["amount"]["N"],
            "reference": transaction["reference"]["S"],
            "date": datetime.fromtimestamp(int(transaction["date"]["N"])).isoformat(),
            "experience": 1,
        }
        for transaction in transactions
    ]

    add_is_outgoing_partial = partial(add_is_outgoing, account_id)
    response = [add_is_outgoing_partial(x) for x in response]

    response = [add_company_score(x) for x in response]

    return response
