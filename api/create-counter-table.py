import boto3
import os

csv_file_path = "industrial_project_dataset.csv"
table_name = "qmbank-accounts-counter"

dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-west-2",
    aws_access_key_id=os.environ.get("ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("SECRET_KEY"),
)
table = dynamodb.Table(table_name)

item = {"pk": "orderCount", "count": 68}

table.put_item(Item=item)
