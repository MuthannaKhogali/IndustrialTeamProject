import base64
import boto3
import json
from decimal import Decimal
import time
import uuid

# Init client
default_client = boto3.client("dynamodb", region_name="eu-west-2")
accounts_table = "qmbank-accounts"
transactions_table = "qmbank-transactions"

# Example Request:
# {
#   "sender_id": "12345678"
#   "recipient_id": "87654321"
#   "amount": 500
# }


# Gets account balance based on account ID, (we dont actually need this here anymore but it's here just incase!)
def get_account_balance(account_id, client):
    try:
        item = client.get_item(
            TableName=accounts_table, Key={"account_no": {"N": str(account_id)}}
        )
        return item.get("Item")
    except Exception as e:
        print(f"Error fetching account balance: {e}")
        return None


# Updates the balance of an account based on the account ID, based on https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
# Updated to stop race condition
def update_sender_account_balance(account_id, amount, client):
    try:
        client.update_item(
            TableName=accounts_table,
            Key={"account_no": {"S": str(account_id)}},
            UpdateExpression="SET balance = balance + :amount",
            ExpressionAttributeValues={":amount": {"N": str(-amount)}},
            ConditionExpression="balance >= :amount",
        )
    except Exception as e:
        print(f"Error updating account balance: {e}")
        raise


def update_recipient_account_balance(account_id, amount, client):
    try:
        client.update_item(
            TableName=accounts_table,
            Key={"account_no": {"S": str(account_id)}},
            UpdateExpression="SET balance = balance + :amount",
            ExpressionAttributeValues={":amount": {"N": str(amount)}},
        )
    except Exception as e:
        print(f"Error updating account balance: {e}")
        raise


# Pushes a record of the transaction to the transactions table.
def create_transaction_record(sender_id, recipient_id, amount, reference, client):
    try:
        client.put_item(
            TableName=transactions_table,
            Item={
                "id": {
                    "S": str(uuid.uuid4())
                },  # Unique transaction ID, I think this should work?? https://docs.python.org/3/library/uuid.html
                "sender_id": {"S": str(sender_id)},
                "recipient_id": {"S": str(recipient_id)},
                "amount": {"N": str(amount)},
                "date": {"N": str(int(time.time()))},
                "reference": {"S": reference},
            },
        )
    except Exception as e:
        print(f"Error creating transaction record: {e}")
        raise


# Main lambda function
def lambda_handler(event, context, client=default_client):
    # Parsing request body into dictionary, see example request
    body = event["body"]
    body = base64.b64decode(body)
    body = json.loads(body)
    sender_id = event["pathParameters"]["id"]
    recipient_id = body["recipient_id"]
    reference = body["reference"]
    if sender_id == recipient_id:
        return {"statusCode": 400}
    amount = Decimal(
        str(body["amount"])
    )  # Using python Decimal for precise floating calculation

    # Validate amount
    if amount <= 0:
        return {"statusCode": 400}  # Bad Request, amount must be greater than 0

    try:
        update_sender_account_balance(sender_id, amount, client)
    except client.exceptions.ConditionalCheckFailedException:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Insufficient balance"}),
        }

    update_recipient_account_balance(recipient_id, amount, client)

    create_transaction_record(sender_id, recipient_id, amount, reference, client)

    # Returns success
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Transaction successful", "amount": float(amount)}
        ),
    }
