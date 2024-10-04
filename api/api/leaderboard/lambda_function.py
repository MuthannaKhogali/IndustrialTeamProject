import boto3
import math


client = boto3.client("dynamodb", region_name="eu-west-2")
accounts_table = "qmbank-accounts"


def calculate_user_level(user_experience):
    if user_experience < 10:
        return 0
    return min(10, math.floor(math.log((4 * user_experience / 10) + 1, 5)))


def get_leaderboard():
    return client.query(
        TableName=accounts_table,
        IndexName="gsi-user_experience-index",
        KeyConditionExpression="#gsi = :one",
        ExpressionAttributeNames={"#gsi": "gsi"},
        ExpressionAttributeValues={":one": {"S": "1"}},
        # Sort in descending order.
        ScanIndexForward=False,
        Limit=15,
    )


def lambda_handler(event, context):
    leaderboard = get_leaderboard()["Items"]
    # return leaderboard
    leaderboard = [
        {
            "name": account["name"]["S"],
            "experience": account["user_experience"]["N"],
            "level": calculate_user_level(int(account["user_experience"]["N"])),
            "streak": account["user_streak"]["N"],
        }
        for account in leaderboard
        if int(account["account_no"]["S"]) >= 69
    ]

    return leaderboard
