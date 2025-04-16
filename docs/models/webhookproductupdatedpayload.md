# WebhookProductUpdatedPayload

Sent when a product is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `type`                                 | *Literal["product.updated"]*           | :heavy_check_mark:                     | N/A                                    | product.updated                        |
| `data`                                 | [models.Product](../models/product.md) | :heavy_check_mark:                     | A product.                             |                                        |