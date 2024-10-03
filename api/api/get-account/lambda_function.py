import boto3

client = boto3.client("dynamodb")
tableName = "qmbank-accounts"


# Calculates user level based on current XP. Max level of 10.
# user_experience is the user's current XP, x & y represent difficulty.
# Level boundaries are calculated with (level / x)^y, rounded to nearest whole number, then multiplied by 100 to reflect our XP score.
# Returns user's level.
def calculate_user_level(user_experience, x=0.35, y=1.5):
    max_level = 10
    for level in range(1, max_level + 1):
        level_boundary = round((level / x) ** y * 100)
        if user_experience < level_boundary:
            return (
                level - 1 if level > 0 else 0
            )  # Return level 0 if no boundaries have been hit yet.
    return max_level  # Return level 10 if XP exceeds all boundaries


def get_alternatives(company_category: str) -> dict:
    alternatives = client.query(
        TableName=tableName,
        IndexName="company_category-index",
        KeyConditionExpression="#attr = :value",
        ExpressionAttributeNames={"#attr": "company_category"},
        ExpressionAttributeValues={":value": {"S": company_category}},
    )["Items"]

    alternatives = [
        {
            "account_id": alternative["account_no"]["S"],
            "name": alternative["name"]["S"],
            "company_category": alternative["company_category"]["S"],
            "company_env_scores": [
                int(alternative["company_env_scores"]["M"]["carbon_emissions"]["N"]),
                int(alternative["company_env_scores"]["M"]["waste_management"]["N"]),
                int(
                    alternative["company_env_scores"]["M"]["sustainability_practices"][
                        "N"
                    ]
                ),
            ],
            "company_desc": alternative["company_description"]["S"],
            "company_rag_score": (
                int(alternative["company_env_scores"]["M"]["carbon_emissions"]["N"])
                + int(alternative["company_env_scores"]["M"]["waste_management"]["N"])
                + int(
                    alternative["company_env_scores"]["M"]["sustainability_practices"][
                        "N"
                    ]
                )
            ),
        }
        for alternative in alternatives
    ]

    alternatives.sort(key=lambda x: int(x["company_rag_score"]), reverse=True)

    return alternatives


def lambda_handler(event, context):
    account_no = event["pathParameters"]["id"]

    item = client.get_item(TableName=tableName, Key={"account_no": {"S": account_no}})

    if "Item" not in item:
        return {"statusCode": 404}

    item = item["Item"]

    response = {
        "account_id": account_no,
        "name": item["name"]["S"],
        "balance": int(item["balance"]["N"]),
    }

    if "company_category" in item:
        response["is_company"] = True
        response["company_category"] = item["company_category"]["S"]
        response["company_env_scores"] = [
            int(item["company_env_scores"]["M"]["carbon_emissions"]["N"]),
            int(item["company_env_scores"]["M"]["waste_management"]["N"]),
            int(item["company_env_scores"]["M"]["sustainability_practices"]["N"]),
        ]
        response["company_desc"] = item["company_description"]["S"]
        response["company_rag_score"] = sum(response["company_env_scores"])
        response["alternatives"] = get_alternatives(response["company_category"])
    else:
        response["is_company"] = False
        response["level"] = calculate_user_level(
            int(item.get("user_experience", {}).get("N", 0))
        )
        response["streak"] = item.get("user_streak", {}).get("N", 0)

    return response
