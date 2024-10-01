import boto3
import json
from boto3.dynamodb.conditions import Key

default_client = boto3.client("dynamodb", region_name="us-east-1")
transactions_table = "qmbank_transactions"


# Gets all transactions for a given account using QUERY. Using the account_id. Gets all transactions where account is sender or recipient.
def get_account_transactions(account_id, client=default_client):
    try:
        # QUERY table
        response = client.scan(
            TableName=transactions_table,
            FilterExpression="sender_id = :account_id OR recipient_id = :account_id",
            ExpressionAttributeValues={":account_id": {"N": str(account_id)}},
        )

        transactions = response.get("Items", [])
        return transactions

    except Exception as e:
        print(f"Error fetching transactions for account: {e}")
        return None


def lambda_handler(event, context, client=default_client):
    try:
        # Gets account ID from path parameters. accounts/{id}/transactions
        account_id = event["pathParameters"]["id"]

        transactions = get_account_transactions(account_id, client)

        if not transactions:
            return {
                "statusCode": 404,
                "body": json.dumps(
                    {"message": "No transactions found for this account"}
                ),
            }

        return {"statusCode": 200, "body": json.dumps({"transactions": transactions})}

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)}),
        }
