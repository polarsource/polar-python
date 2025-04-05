# WebhookCustomerDeletedPayload

Sent when a customer is deleted.

**Discord & Slack support:** Basic


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `type`                                   | *Literal["customer.deleted"]*            | :heavy_check_mark:                       | N/A                                      | customer.deleted                         |
| `data`                                   | [models.Customer](../models/customer.md) | :heavy_check_mark:                       | A customer in an organization.           |                                          |