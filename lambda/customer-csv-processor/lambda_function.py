
import json
import boto3
import csv
import io

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CustomerRecords")

BUCKET_NAME = "cloud-customer-monitoring-hepshibha-2026"


def lambda_handler(event, context):
    print("Customer CSV processor started")

    config_obj = s3.get_object(
        Bucket=BUCKET_NAME, Key="config.json"
    )
    config = json.loads(
        config_obj["Body"].read().decode("utf-8")
    )

    csv_obj = s3.get_object(
        Bucket=BUCKET_NAME, Key="Customer_Test.csv"
    )
    content = csv_obj["Body"].read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(content))

    required_fields = config["required_fields"]
    allowed_statuses = config["allowed_statuses"]
    saved_count = 0
    invalid_count = 0

    for row in reader:
        row = {key: value.strip() for key, value in row.items()}

        missing = [
            field for field in required_fields
            if not row.get(field, "")
        ]

        if missing:
            print("INVALID: missing fields", missing, row)
            invalid_count += 1
        elif row["account_status"] not in allowed_statuses:
            print("INVALID: account status", row)
            invalid_count += 1
        else:
            table.put_item(Item=row)
            print("SAVED customer:", row["customer_id"])
            saved_count += 1

    print(f"Summary: saved={saved_count}, invalid={invalid_count}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "saved": saved_count,
            "invalid": invalid_count
        })
    }
