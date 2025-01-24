# WebhookOrderRefundedPayload

Sent when an order is fully or partially refunded.

**Discord & Slack support:** Full


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `data`                             | [models.Order](../models/order.md) | :heavy_check_mark:                 | N/A                                |
| `type`                             | *Literal["order.refunded"]*        | :heavy_check_mark:                 | N/A                                |