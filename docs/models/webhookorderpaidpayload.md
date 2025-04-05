# WebhookOrderPaidPayload

Sent when an order is paid.

When you receive this event, the order is fully processed and payment has been received.

**Discord & Slack support:** Full


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `type`                             | *Literal["order.paid"]*            | :heavy_check_mark:                 | N/A                                | order.paid                         |
| `data`                             | [models.Order](../models/order.md) | :heavy_check_mark:                 | N/A                                |                                    |