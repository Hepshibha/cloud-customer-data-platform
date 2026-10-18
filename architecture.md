
flowchart TD
    A["CSV File"] --> B["Amazon S3"]
    C["config.json"] --> B
    B --> D["S3 Event Notification"]
    D --> E["Lambda: CSV Processor"]
    E --> F["Validate Customer Data"]
    F --> G[("DynamoDB: CustomerRecords")]

    H["Postman"] --> I["Amazon API Gateway"]
    I --> J["Lambda: API Handler"]
    J <--> G

    E -. Logs .-> K["Amazon CloudWatch"]
    J -. Logs .-> K

    L["AWS IAM Permissions"] -.-> E
    L -.-> J
