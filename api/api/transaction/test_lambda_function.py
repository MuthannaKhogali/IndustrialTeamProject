import boto3
from moto import mock_aws
import json
from decimal import Decimal

# Import the Lambda function (IMPORTANT: run this with python -m test_lambda_function because of the way python imports work!?)
from ..transaction.lambda_function import lambda_handler

# Mock DynamoDB setup
@mock_aws
def test_lambda_function():
    # Create a mock DynamoDB table
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    
    # Create the mock accounts table
    dynamodb.create_table(
        TableName="qmbank-accounts",
        KeySchema=[
            {
                "AttributeName": "account_no",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "account_no",
                "AttributeType": "N"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10
        }
    )
    
    # Create the mock transactions table
    dynamodb.create_table(
        TableName="qmbank-transactions",
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10
        }
    )

    # Add sample data to the accounts table
    dynamodb.put_item(
        TableName="qmbank-accounts",
        Item={
            "account_no": {"N": "12345678"},
            "balance": {"N": "1000"},
            "name": {"S": "John Doe"},
            "user_experience": {"N": "0"}
        }
    )
    dynamodb.put_item(
        TableName="qmbank-accounts",
        Item={
            "account_no": {"N": "87654321"},
            "balance": {"N": "500"},
            "name": {"S": "Jane Doe Corp"},
            "company_env_scores": {
                "M": {
                    "carbon_emissions": {"N": "1"},
                    "waste_management": {"N": "3"},
                    "sustainability_practices": {"N": "2"}
                }
            }
        }
    )

    # Define a mock event and context for the transaction test
    event = {
        "httpMethod": "POST",  # Ensure the method is POST since you're creating a transaction
        "body": json.dumps({
            "sender_id": "12345678",
            "recipient_id": "87654321",
            "amount": 150  # Use an integer or Decimal value for amount
        })
    }
    context = {}  # Mock context can be empty

    # Call the Lambda function
    response = lambda_handler(event, context, client=dynamodb)

    # Print the response
    print("Response:", json.dumps(response, indent=2))


if __name__ == "__main__":
    test_lambda_function()