Cloud-Based Customer Data Processing & Monitoring Platform

Project Overview
A serverless AWS project that processes customer data from CSV files, validates records, stores them in DynamoDB, and provides APIs to retrieve and update customer information.

AWS Services
- **Amazon S3:** Stores CSV and configuration files.
- **AWS Lambda:** Processes CSV data and handles API requests.
- **Amazon DynamoDB:** Stores customer records.
- **Amazon API Gateway:** Exposes GET and PUT API routes.
- **Amazon CloudWatch:** Stores execution logs.
- **AWS IAM:** Controls access to AWS resources.

Workflow
1. Upload a CSV file to S3.
2. An S3 event triggers the CSV-processing Lambda function.
3. Lambda validates the records using `config.json`.
4. Valid records are saved to DynamoDB.
5. API Gateway routes GET and PUT requests to a second Lambda function.
6. The API Lambda retrieves or updates customer records.
7. CloudWatch logs help monitor and troubleshoot executions.

Testing
- Verified automatic CSV processing.
- Confirmed customer records in DynamoDB.
- Tested GET and PUT requests using Postman.
- Checked Lambda execution logs in CloudWatch.
- Reviewed AWS costs in Cost Explorer.

Security Improvements
- Add authorization to API routes.
- Replace broad IAM permissions with least-privilege policies.
- Never use real customer information in a public demonstration.

Key Learnings
- AWS serverless architecture
- Event-driven processing
- CSV validation and DynamoDB operations
- API integration and testing with Postman
- CloudWatch monitoring and troubleshooting
- Cloud security and cost awareness
