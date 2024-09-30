import boto3
import json

default_client = boto3.client("dynamodb", region_name='us-east-1')
transactions_table = "qmbank_transactions"

def lambda_handler(event, context, client=default_client):
    try:
        # Parse api parameters, transaction/{id}
        transaction_id = event["pathParameters"]["id"]

        # Getting transaction from database
        transaction_item = client.get_item(
            TableName=transactions_table,
            Key={"id": {"S": id}}
        )

        # Check if transaction is in table
        if "Item" not in transaction_item:
            return {
                "statusCode": 404 # Not Found
            }
        
        transaction = transaction_item["Item"]

        response = {
            "Tid": transaction["id"]["S"],
            "sender_id": int(transaction["sender_id"]["N"]),
            "recipient_id": int(transaction["recipient_id"]["N"]),
            "amount": float(transaction["amount"]["N"])
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    
    except Exception as e:
        return {
            "statusCode": 500, "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }