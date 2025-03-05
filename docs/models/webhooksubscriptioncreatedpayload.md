# WebhookSubscriptionCreatedPayload

Sent when a new subscription is created.

When this event occurs, the subscription `status` might not be `active` yet, as we can still have to wait for the first payment to be processed.

**Discord & Slack support:** Full


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `data`                                           | [models.Subscription](../models/subscription.md) | :heavy_check_mark:                               | N/A                                              |                                                  |
| `type`                                           | *Literal["subscription.created"]*                | :heavy_check_mark:                               | N/A                                              | subscription.created                             |