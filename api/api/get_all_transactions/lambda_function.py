import boto3
from datetime import datetime
import json

default_client = boto3.client("dynamodb", region_name="eu-west-2")
transactions_table = "qmbank-transactions"


# Gets all transactions for a given account using QUERY. Using the account_id. Gets all transactions where account is sender or recipient.
def get_account_transactions(account_id, client=default_client):
    try:
        # QUERY table
        response = client.scan(
            TableName=transactions_table,
            FilterExpression="sender_id = :account_id OR recipient_id = :account_id",
            ExpressionAttributeValues={":account_id": {"S": str(account_id)}},
        )

        transactions = response.get("Items", [])
        return transactions

    except Exception as e:
        print(f"Error fetching transactions for account: {e}")
        return None


def get_recipient_name(recipient_id):
    return default_client.get_item(
        TableName="qmbank-accounts", Key={"account_no": {"S": recipient_id}}
    )["Item"]["name"]["S"]


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

    return [
        {
            "recipient_name": get_recipient_name(transaction["recipient_id"]["S"]),
            "recipient_id": transaction["recipient_id"]["S"],
            "sender_name": get_recipient_name(transaction["sender_id"]["S"]),
            "sender_id": transaction["sender_id"]["S"],
            "is_outgoing": True
            if account_id != transaction["recipient_id"]["S"]
            else False,
            "amount": transaction["amount"]["N"],
            "reference": transaction["reference"]["S"],
            "date": datetime.fromtimestamp(int(transaction["date"]["N"])).isoformat(),
            "experience": 1,
        }
        for transaction in transactions
    ]
