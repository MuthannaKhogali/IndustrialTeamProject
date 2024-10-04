import base64
import boto3
import json

client = boto3.client("dynamodb", region_name="eu-west-2")
tableName = "qmbank-accounts"


def error(errorMessage):
    return {
        "statusCode": 400,
        "body": json.dumps({"error": errorMessage}),
    }


def lambda_handler(event, context):
    body = event.get("body", None)

    if not body:
        return error("missing required fields")

    if event.get("isBase64Encoded", None):
        body = base64.b64decode(body)

    try:
        body = json.loads(body)
    except json.JSONDecodeError:
        return error("invalid json received")

    if not body:
        return error("missing required fields")

    if "name" not in body:
        return error("missing required name field")
    name = body["name"]

    if not isinstance(name, str):
        return error("name field is not a string")

    if "starting_balance" not in body:
        return error("missing required starting_balance field")
    starting_balance = body["starting_balance"]

    if not isinstance(starting_balance, int):
        return error("starting_balance field is not a int")

    response = client.update_item(
        TableName=tableName + "-counter",
        Key={"pk": {"S": "orderCount"}},
        UpdateExpression="ADD #cnt :val",
        ExpressionAttributeNames={"#cnt": "count"},
        ExpressionAttributeValues={":val": {"N": "1"}},
        ReturnValues="UPDATED_NEW",
    )

    next_account_no = response["Attributes"]["count"]["N"].zfill(9)

    client.put_item(
        TableName=tableName,
        Item={
            "account_no": {"S": next_account_no},
            "name": {"S": body["name"]},
            "balance": {"N": str(body["starting_balance"])},
            "gsi": {"S": "1"},
        },
    )

    return {"account_no": next_account_no}
