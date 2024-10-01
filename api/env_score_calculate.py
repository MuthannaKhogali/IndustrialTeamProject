import boto3
import json

default_client = boto3.client("dynamodb", region_name='us-east-1')
accounts_table = "qmbank-accounts"

def calculate_environmental_impact_score(account_id, client=default_client):
    try:
        # Gets ENV scores from database
        item = client.get_item(
            TableName=accounts_table,
            Key={"account_no": {"N": str(account_id)}}
        )

        # If item doesnt exist, or doesnt have ENV scores, we return 404 Not Found
        if "Item" not in item or "company_env_scores" not in item["Item"]:
            return {"statusCode": 404, "body": "Company or Environmental Scores Not Found"}
        
        env_scores = item["Item"]["company_env_scores"]["M"]
        carbon_emissions = int(env_scores["carbon_emissions"]["N"])
        waste_management = int(env_scores["waste_management"]["N"])
        sustainability_practices = int(env_scores["sustainability_practices"]["N"])

        # Score is between 1 and 10 per category
        max_score = 10

        # ENV score calculation
        total_score = carbon_emissions + waste_management + sustainability_practices
        max_total_score = 3 * max_score

        environmental_impact_score = total_score / max_total_score

        # RAG rating
        if environmental_impact_score <= 0.3:
            rag_rating = "RED"
        elif environmental_impact_score <= 0.7:
            rag_rating = "AMBER"
        else:
            rag_rating = "GREEN"

        return {
            "statusCode": 200,
            "body": json.dumps({
                "environmental_impact_score": environmental_impact_score,
                "rag_rating": rag_rating,
                "carbon_emissions_score": carbon_emissions,
                "waste_management_score": waste_management,
                "sustainability_practices_score": sustainability_practices
            })
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }