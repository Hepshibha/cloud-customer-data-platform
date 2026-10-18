
import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CustomerRecords")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):
    try:
        method = (
            event.get("requestContext", {})
            .get("http", {})
            .get("method")
            or event.get("httpMethod", "")
        )

        path_params = event.get("pathParameters") or {}
        customer_id = path_params.get("customer_id")

        if not customer_id:
            return response(400, {
                "error": "customer_id is required"
            })

        if method == "GET":
            result = table.get_item(
                Key={"customer_id": customer_id}
            )
            item = result.get("Item")

            if not item:
                return response(404, {
                    "error": "Customer not found"
                })

            return response(200, item)

        if method == "PUT":
            body = event.get("body") or "{}"

            if isinstance(body, str):
                body = json.loads(body)

            mobile_number = body.get("mobile_number")

            if not mobile_number:
                return response(400, {
                    "error": "mobile_number is required"
                })

            result = table.update_item(
                Key={"customer_id": customer_id},
                UpdateExpression="SET mobile_number = :mobile",
                ExpressionAttributeValues={
                    ":mobile": mobile_number
                },
                ReturnValues="ALL_NEW"
            )

            return response(200, result["Attributes"])

        return response(405, {
            "error": "Method not supported"
        })

    except Exception as exc:
        print(f"Request failed: {exc}")
        return response(500, {
            "error": "Internal server error"
        })
