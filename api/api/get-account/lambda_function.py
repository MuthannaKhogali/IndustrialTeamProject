import boto3

client = boto3.client("dynamodb")
tableName = "qmbank-accounts"


def lambda_handler(event, context):
    id = event["pathParameters"]["id"]

    item = client.get_item(TableName=tableName, Key={"account_no": {"N": str(id)}})

    if "Item" not in item:
        return {"statusCode": 404}

    item = item["Item"]

    response = {
        "account_id": str(id).zfill(8),
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
        # response["alternatives"] =
    else:
        response["is_company"] = False
        # TODO
        response["level"] = 1
        response["streak"] = 0

    return response
