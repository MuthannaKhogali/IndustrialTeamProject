import boto3
from moto import mock_aws
import json
from lambda_function import lambda_handler

@mock_aws
def test_get_account_transactions():
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")

    dynamodb.create_table(
        TableName="transactions",
        KeySchema=[
            {
                "AttributeName": "TransactionID",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "TransactionID",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10
        }
    )

    # Sample transaction data
    dynamodb.put_item(
        TableName="transactions",
        Item={
            "TransactionID": {"S": "abc123"},
            "SenderID": {"N": "12345678"},
            "RecipientID": {"N": "87654321"},
            "Amount": {"N": "150"}
        }
    )
    dynamodb.put_item(
        TableName="transactions",
        Item={
            "TransactionID": {"S": "ghi789"},
            "SenderID": {"N": "87654321"},
            "RecipientID": {"N": "12345678"},
            "Amount": {"N": "50"}
        }
    )

    event = {
        "pathParameters": {
            "id": "12345678"
        }
    }
    context = {}

    response  = lambda_handler(event, context, client=dynamodb)

    print("Response:", json.dumps(response, indent=2))

    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert len(body["transactions"]) == 2 # we expect 2 transactions here
    assert body["transactions"][0]["SenderID"]["N"] == "12345678" or body["transactions"][0]["RecipientID"]["N"] == "12345678"
    assert body["transactions"][1]["SenderID"]["N"] == "12345678" or body["transactions"][1]["RecipientID"]["N"] == "12345678"

if __name__ == "__main__":
    test_get_account_transactions()