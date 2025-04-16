# WebhookProductCreatedPayload

Sent when a new product is created.

**Discord & Slack support:** Basic


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `type`                                 | *Literal["product.created"]*           | :heavy_check_mark:                     | N/A                                    | product.created                        |
| `data`                                 | [models.Product](../models/product.md) | :heavy_check_mark:                     | A product.                             |                                        |