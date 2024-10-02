import base64
import boto3
import json
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
    client.update_item(
        TableName=accounts_table,
        Key={"account_no": {"S": str(account_id)}},
        UpdateExpression="SET balance = balance + :amount",
        ExpressionAttributeValues={":amount": {"N": str(amount)}},
        ConditionExpression="balance >= :amount",
    )


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


def error(errorMessage):
    return {
        "statusCode": 400,
        "body": json.dumps({"error": errorMessage}),
    }


# Main lambda function
def lambda_handler(event, context, client=default_client):
    # Parsing request body into dictionary, see example request
    body = event.get("body", None)

    if not body:
        return error("missing POST body")

    if event.get("isBase64Encoded", None):
        body = base64.b64decode(body)

    try:
        body = json.loads(body)
    except json.JSONDecodeError:
        return error("invalid json received")

    if not body:
        return error("missing required fields")

    sender_id = event["pathParameters"]["id"]

    if "recipient_id" not in body:
        return error("missing required recipient_id field")
    recipient_id = body["recipient_id"]

    if not isinstance(recipient_id, str):
        return error("recipient_id field is not a string")

    if "amount" not in body:
        return error("missing required amount field")
    amount = body["amount"]

    if not isinstance(amount, int):
        return error("amount field is not a int")

    if amount <= 0:
        return error("amount must be greater than 0")

    reference = body.get("reference", "")

    if sender_id == recipient_id:
        return error("sender_id is the same as the recipient_id")

    try:
        update_sender_account_balance(sender_id, amount, client)
    except client.exceptions.ConditionalCheckFailedException:
        return error("sender has insufficient balance")

    update_recipient_account_balance(recipient_id, amount, client)

    create_transaction_record(sender_id, recipient_id, amount, reference, client)

    # Returns success
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Transaction successful", "amount": float(amount)}
        ),
    }
