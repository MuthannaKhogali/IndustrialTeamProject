import boto3
from moto import mock_aws
import json
import uuid
from decimal import Decimal

# Import the Lambda function
from lambda_function import lambda_handler

# Mock DynamoDB setup
@mock_aws
def test_get_transaction():
    # Create a mock DynamoDB client]
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    
    # Create the mock transactions table
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

    # Add sample data to the transactions table
    transaction_id = str(uuid.uuid4())
    dynamodb.put_item(
        TableName="transactions",
        Item={
            "TransactionID": {"S": transaction_id},
            "SenderID": {"N": "12345678"},
            "RecipientID": {"N": "87654321"},
            "Amount": {"N": "150.00"}
        }
    )

    # Define a mock event and context for the get-transaction test
    event = {
        "pathParameters": {
            "transaction_id": transaction_id
        }
    }
    context = {}  # Mock context can be empty

    # Call the Lambda function
    response = lambda_handler(event, context, client=dynamodb)

    # Print the response
    print("Response:", json.dumps(response, indent=2))


if __name__ == "__main__":
    test_get_transaction()