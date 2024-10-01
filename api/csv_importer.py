import csv
import boto3
import os

csv_file_path = "industrial_project_dataset.csv"
table_name = "qmbank-accounts"

dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-west-2",
    aws_access_key_id=os.environ.get("ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("SECRET_KEY"),
)
table = dynamodb.Table(table_name)

with open(csv_file_path, "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        item = {
            "account_no": row["Account Number"],
            "name": row["Company Name"],
            "balance": 0,
            "company_category": row["Spending Category"],
            "company_env_scores": {
                "carbon_emissions": int(row["Carbon Emissions"]),
                "waste_management": int(row["Waste Management"]),
                "sustainability_practices": int(row["Sustainability Practices"]),
            },
            "company_description": row["Summary"],
        }

        table.put_item(Item=item)

print(f"CSV data imported successfully into {table_name}")
