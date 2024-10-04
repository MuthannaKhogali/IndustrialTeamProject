import boto3


client = boto3.client("dynamodb", region_name="eu-west-2")
accounts_table = "qmbank-accounts"


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
            "level": -1,
            "streak": account["user_streak"]["N"],
        }
        for account in leaderboard
        if int(account["account_no"]["S"]) >= 69
    ]

    return leaderboard
