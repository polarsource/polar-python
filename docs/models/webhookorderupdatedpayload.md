# WebhookOrderUpdatedPayload

Sent when an order is updated.

An order is updated when:

* Its status changes, e.g. from `pending` to `paid`.
* It's refunded, partially or fully.

**Discord & Slack support:** Full


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `data`                             | [models.Order](../models/order.md) | :heavy_check_mark:                 | N/A                                |                                    |
| `type`                             | *Literal["order.updated"]*         | :heavy_check_mark:                 | N/A                                | order.updated                      |