# WebhookSubscriptionCanceledPayload

Sent when a subscription is canceled.
Customers might still have access until the end of the current period.

**Discord & Slack support:** Full


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `data`                                           | [models.Subscription](../models/subscription.md) | :heavy_check_mark:                               | N/A                                              |                                                  |
| `type`                                           | *Literal["subscription.canceled"]*               | :heavy_check_mark:                               | N/A                                              | subscription.canceled                            |