# WebhookOrderCreatedPayload

Sent when a new order is created.

A new order is created when:

* A customer purchases a one-time product. In this case, `billing_reason` is set to `purchase`.
* A customer starts a subscription. In this case, `billing_reason` is set to `subscription_create`.
* A subscription is renewed. In this case, `billing_reason` is set to `subscription_cycle`.
* A subscription is upgraded, downgraded or revoked with an immediate proration invoice. In this case, `billing_reason` is set to `subscription_update`.

**Discord & Slack support:** Full


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `data`                             | [models.Order](../models/order.md) | :heavy_check_mark:                 | N/A                                |                                    |
| `type`                             | *Literal["order.created"]*         | :heavy_check_mark:                 | N/A                                | order.created                      |