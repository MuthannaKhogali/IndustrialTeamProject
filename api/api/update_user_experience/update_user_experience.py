import boto3
from decimal import Decimal

default_client = boto3.client("dynamodb", region_name="eu-west-2")
accounts_table = "qmbank-accounts"

def update_user_experience(user_id, company_env_score, client=default_client):
    try:
        # calculate user's experience from decimal to an int (This is easier to store in the database as just an int, and also makes XP more exciting. big numbers are better)
        # If the decimal value is longer than 2 digits, it will simply round down and add the experience (0.357 becomes 35XP.)
        experience_to_add = int(company_env_score * 100)

        client.update_item(
            TableName=accounts_table,
            Key={"account_no": {"N": str(user_id)}},
            UpdateExpression="ADD user_experience :increment",
            ExpressionAttributeValues={":increment": {"N": str(experience_to_add)}}
        )

        return {
            "statusCode": 200,
            "body": {
                "message": "User experience updated successfully.",
                "experience_added": experience_to_add
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"message": "Internal Server Error", "error": str(e)}
        }