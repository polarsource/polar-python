# WebhookProductCreatedPayload

Sent when a new product is created.

**Discord & Slack support:** Basic


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `data`                                 | [models.Product](../models/product.md) | :heavy_check_mark:                     | A product.                             |
| `type`                                 | *Literal["product.created"]*           | :heavy_check_mark:                     | N/A                                    |