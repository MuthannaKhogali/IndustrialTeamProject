import boto3
import json
from decimal import Decimal
import uuid

# Init client
client = boto3.client("dynamodb")
accounts_table = "qmbank-accounts"
transactions_table = "transactions"

# Example Request:
# {
#   "sender_id": "12345678"
#   "recipient_id": "87654321"
#   "amount": 500
# }

# Gets account balance based on account ID, (i think we just need balance for this function)
def get_account_balance(account_id):
    try:
        item = client.get_item(
            TableName=accounts_table,
            Key={"account_no": {"N": str(account_id)}}
        )
        return item.get("Item")
    except Exception as e:
        print(f"Error fetching account balance: {e}")
        return None
    
# Updates the balance of an account based on the account ID, based on https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
def update_account_balance(account_id, new_balance):
    try:
        client.update_item(
            TableName=accounts_table,
            Key={"account_no": {"N": str(account_id)}},
            UpdateExpression="SET balance = :new_balance",
            ExpressionAttributeValues={":new_balance": {"N": str(new_balance)}}
        )
    except Exception as e:
        print(f"Error updating account balance: {e}")
        raise 

# Pushes a record of the transaction to the transactions table.
def create_transaction_record(sender_id, recipient_id, amount):
    try:
        client.put_item(
            TableName=transactions_table,
            Item={
                "TransactionID": {"S": str(uuid.uuid4())}, # Unique transaction ID, I think this should work?? https://docs.python.org/3/library/uuid.html
                "SenderID": {"N": str(sender_id)},
                "RecipientID": {"N": str(recipient_id)},
                "Amount": {"N": str(amount)}
            }
        )
    except Exception as e:
        print(f"Error creating transaction record: {e}")
        raise


# Main lambda function
def lambda_handler(event, context):
    try:
        # Parsing request body into dictionary, see example request
        body = json.loads(event["body"])
        sender_id = body["sender_id"]
        recipient_id = body["recipient_id"]
        amount = Decimal(str(body["amount"])) # Using python Decimal for precise floating calculation

        # Validate amount
        if amount <= 0:
            return {"statusCode": 400} # Bad Request, amount must be greater than 0
        
        # Fetches sender's balance
        sender_account = get_account_balance(sender_id)
        if not sender_account:
            return {"statusCode": 404} # Not Found
        
        # Check if sender has required balance
        sender_balance = Decimal(sender_account["balance"]["N"])
        if sender_balance < amount:
            return {"statusCode": 400} # Bad Request, insufficient balance
        
        # Fetches recipient's balance
        recipient_account = get_account_balance(recipient_id)
        if not recipient_account:
            return {"statusCode": 404} # Not Found
        
        recipient_balance = Decimal(recipient_account["balance"]["N"])


        # TRANSACTION LOGIC
        new_sender_balance = sender_balance - amount
        new_recipient_balance = recipient_balance + amount

        # Update account balances database side
        update_account_balance(sender_id, new_sender_balance)
        update_account_balance(recipient_id, new_recipient_balance)

        # Records the transaction
        create_transaction_record(sender_id, recipient_id, amount)

        # Returns success
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Transaction successful",
                "new_sender_balance": float(new_sender_balance),
                "new_recipient_balance": float(new_recipient_balance)
            })
        }
    
    except Exception as e:
        return {"statusCode": 500} # Internal Server Error
        


