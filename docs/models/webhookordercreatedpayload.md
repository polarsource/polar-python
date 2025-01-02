# WebhookOrderCreatedPayload

Sent when a new order is created.

**Discord & Slack support:** Full


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `data`                             | [models.Order](../models/order.md) | :heavy_check_mark:                 | N/A                                |
| `type`                             | *Literal["order.created"]*         | :heavy_check_mark:                 | N/A                                |