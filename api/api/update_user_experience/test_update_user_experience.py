from moto import mock_aws
import boto3
from update_user_experience import update_user_experience
import json


@mock_aws
def test_update_user_experience():
    dynamodb = boto3.client("dynamodb", region_name="eu-west-2")
    
    # Create the mock accounts table
    dynamodb.create_table(
        TableName="qmbank-accounts",
        KeySchema=[{"AttributeName": "account_no", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "account_no", "AttributeType": "N"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    
    # Adds our sample data
    dynamodb.put_item(
        TableName="qmbank-accounts",
        Item={
            "account_no": {"N": "12345678"},
            "user_experience": {"N": "50"}
        }
    )
    
    # Updating experience
    company_env_score = 0.3  # Example environmental impact score
    result = update_user_experience("12345678", company_env_score, client=dynamodb)
    
    # Gets new user data.
    updated_user_data = dynamodb.get_item(
        TableName="qmbank-accounts",
        Key={"account_no": {"N": "12345678"}}
    )
    
    new_experience = int(updated_user_data["Item"]["user_experience"]["N"])

    # Calculate the expected result
    expected_experience = 50 + int(company_env_score * 100)

    # Validate that the experience was updated correctly
    assert new_experience == expected_experience, "User experience not updated correctly"
    print("Test passed")
    print("Response:", json.dumps(result, indent=2))

# Run the test
if __name__ == "__main__":
    test_update_user_experience()