import base64
import boto3
import json

client = boto3.client("dynamodb", region_name="eu-west-2")
tableName = "qmbank-accounts"


def lambda_handler(event, context):
    body = event["body"]

    if event["isBase64Encoded"]:
        body = base64.b64decode(body)

    body = json.loads(body)

    if "name" not in body or "starting_balance" not in body:
        return {"statusCode": 400}

    response = client.update_item(
        TableName=tableName + "-counter",
        Key={"pk": {"S": "orderCount"}},
        UpdateExpression="ADD #cnt :val",
        ExpressionAttributeNames={"#cnt": "count"},
        ExpressionAttributeValues={":val": {"N": "1"}},
        ReturnValues="UPDATED_NEW",
    )

    next_account_no = response["Attributes"]["count"]["N"]

    client.put_item(
        TableName=tableName,
        Item={
            "account_no": {"N": str(next_account_no)},
            "name": {"S": body["name"]},
            "balance": {"N": str(body["starting_balance"])},
        },
    )

    return {"account_no": next_account_no}
