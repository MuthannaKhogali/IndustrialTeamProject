import boto3
from moto import mock_aws
import json

from env_score_calculate import calculate_environmental_impact_score

@mock_aws
def test_env_score_calculate():
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")

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

    # Mock data
    dynamodb.put_item(
        TableName="qmbank-accounts",
        Item={
            "account_no": {"N": "12345678"},
            "company_env_scores": {
                "M": {
                    "carbon_emissions": {"N": "8"},
                    "waste_management": {"N": "7"},
                    "sustainability_practices": {"N": "9"}
                }
            }
        }
    )

    # function test
    result = calculate_environmental_impact_score(account_id="12345678", client=dynamodb)

    if isinstance(result["body"], str):
        result["body"] = json.loads(result["body"])

    #Expectedresult for assert
    expected_result = {
        "statusCode": 200,
        "body": {
            "environmental_impact_score": 0.8, # (8+7+9)/30
            "rag_rating": "GREEN",
            "carbon_emissions_score": 8,
            "waste_management_score": 7,
            "sustainability_practices_score": 9
        }
    }

    assert result["statusCode"] == expected_result["statusCode"], f"Expected {expected_result['statusCode']} but got {result['statusCode']}"

    assert result["body"]["environmental_impact_score"] == expected_result["body"]["environmental_impact_score"], \
        f"Expected {expected_result['body']['environmental_impact_score']} but got {result['body']['environmental_impact_score']}"
    assert result["body"]["rag_rating"] == expected_result["body"]["rag_rating"], \
        f"Expected {expected_result['body']['rag_rating']} but got {result['body']['rag_rating']}"
    assert result["body"]["carbon_emissions_score"] == expected_result["body"]["carbon_emissions_score"], \
        f"Expected {expected_result['body']['carbon_emissions_score']} but got {result['body']['carbon_emissions_score']}"
    assert result["body"]["waste_management_score"] == expected_result["body"]["waste_management_score"], \
        f"Expected {expected_result['body']['waste_management_score']} but got {result['body']['waste_management_score']}"
    assert result["body"]["sustainability_practices_score"] == expected_result["body"]["sustainability_practices_score"], \
        f"Expected {expected_result['body']['sustainability_practices_score']} but got {result['body']['sustainability_practices_score']}"
    
    print("Test passed!")
    print("Response:", json.dumps(result, indent=2))

if __name__ == "__main__":
    test_env_score_calculate()