# WebhookOrderRefundedPayload

Sent when an order is fully or partially refunded.

**Discord & Slack support:** Full


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `type`                             | *Literal["order.refunded"]*        | :heavy_check_mark:                 | N/A                                | order.refunded                     |
| `data`                             | [models.Order](../models/order.md) | :heavy_check_mark:                 | N/A                                |                                    |