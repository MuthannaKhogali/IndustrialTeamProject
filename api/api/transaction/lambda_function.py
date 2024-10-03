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
        UpdateExpression="SET balance = balance - :amount",
        ExpressionAttributeValues={":amount": {"N": str(amount)}},
        ConditionExpression="balance >= :amount",
    )


def update_recipient_account_balance(account_id, amount, client):
    client.update_item(
        TableName=accounts_table,
        Key={"account_no": {"S": str(account_id)}},
        UpdateExpression="SET balance = balance + :amount",
        ExpressionAttributeValues={":amount": {"N": str(amount)}},
    )


def update_user_experience(user_id, experience_points, client=default_client):
    client.update_item(
        TableName=accounts_table,
        Key={"account_no": {"S": str(user_id)}},
        UpdateExpression="ADD user_experience :increment",
        ExpressionAttributeValues={":increment": {"N": str(experience_points)}},
    )


def update_user_streak(sender_id, recipient, client=default_client):
    # +1 streak if green, -1 if orange, reset if red.
    env_score = calculate_environmental_impact_score(recipient["account_no"]["S"])

    update_value = 1

    if env_score <= 0.3:
        update_expression = "SET user_streak = :value"
        update_value = 0
    elif env_score <= 0.7:
        update_expression = "ADD user_streak :value"
        update_value = -1
    else:
        update_expression = "ADD user_streak :value"
        update_value = 1

    try:
        client.update_item(
            TableName=accounts_table,
            Key={"account_no": {"S": str(sender_id)}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues={
                ":zero": {"N": "0"},
                ":value": {"N": str(update_value)},
            },
            # If the user_streak doesn't already exist the condition would fail, so don't fail in that case.
            ConditionExpression="user_streak >= :zero OR attribute_not_exists(user_streak)",
        )
    except client.exceptions.ConditionalCheckFailedException:
        # This may happen if we try to subtract the user streak below zero, but is expected behaviour.
        pass


# Calculates ENV scores, returns an ENV score, a RAG rating as a string, and the three scores independently.
def calculate_environmental_impact_score(
    account_id, client=default_client
) -> int | None:
    # Gets ENV scores from database
    item = client.get_item(
        TableName=accounts_table, Key={"account_no": {"S": str(account_id)}}
    )

    # If item doesnt exist, or doesnt have ENV scores, we return 404 Not Found
    if "Item" not in item or "company_env_scores" not in item["Item"]:
        return None

    item = item["Item"]

    env_scores = item["company_env_scores"]["M"]
    carbon_emissions = int(env_scores["carbon_emissions"]["N"])
    waste_management = int(env_scores["waste_management"]["N"])
    sustainability_practices = int(env_scores["sustainability_practices"]["N"])

    # ENV score calculation
    total_score = carbon_emissions + waste_management + sustainability_practices

    environmental_impact_score = total_score / 30

    return environmental_impact_score


# Pushes a record of the transaction to the transactions table.
def create_transaction_record(
    sender_id, recipient_id, amount, reference, experience, client
):
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
            "experience": {"N": str(experience)},
        },
    )


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

    if (
        client.get_item(
            TableName=accounts_table, Key={"account_no": {"S": str(sender_id)}}
        ).get("Item", None)
        is None
    ):
        return error("sender_id doesn't exist")

    recipient = client.get_item(
        TableName=accounts_table, Key={"account_no": {"S": str(recipient_id)}}
    ).get("Item", None)
    if recipient is None:
        return error("recipient_id doesn't exist")

    try:
        update_sender_account_balance(sender_id, amount, client)
    except client.exceptions.ConditionalCheckFailedException:
        return error("sender has insufficient balance")

    update_recipient_account_balance(recipient_id, amount, client)

    # Updates user's level and XP!
    environmental_score = calculate_environmental_impact_score(recipient_id, client)

    # calculate user's experience from decimal to an int (This is easier to store in the database as just an int, and also makes XP more exciting. big numbers are better)
    # If the decimal value is longer than 2 digits, it will simply round down and add the experience (0.357 becomes 35XP.)
    transaction_experience_points = int(environmental_score * 100)

    if environmental_score is not None:
        update_user_experience(sender_id, transaction_experience_points, client)

    update_user_streak(sender_id, recipient)

    create_transaction_record(
        sender_id,
        recipient_id,
        amount,
        reference,
        transaction_experience_points,
        client,
    )

    return {"statusCode": 200}
