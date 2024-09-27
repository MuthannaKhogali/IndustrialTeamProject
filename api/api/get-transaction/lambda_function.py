import boto3
import json

client = boto3.client("dynamodb")
transactions_table = "transactions"

def lambda_handler(event, context):
    try:
        # Parse api parameters, transaction/{id}
        transaction_id = event["pathParameters"]["transaction_id"]

        # Getting transaction from database
        transaction_item = client.get_item(
            TableName=transactions_table,
            Key={"TransactionID": {"S": transaction_id}}
        )

        # Check if transaction is in table
        if "Item" not in transaction_item:
            return {
                "statusCode": 404 # Not Found
            }
        
        transaction = transaction_item["Item"]

        response = {
            "TransactionID": transaction["TransactionID"]["S"],
            "SenderID": int(transaction["SenderID"]["N"]),
            "RecipientID": int(transaction["RecipientID"]["N"]),
            "Amount": float(transaction["Amount"]["N"])
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    
    except Exception as e:
        return {
            "statusCode": 500  # Internal Server Error
        }