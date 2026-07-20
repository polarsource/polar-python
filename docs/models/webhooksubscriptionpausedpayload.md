# WebhookSubscriptionPausedPayload

Sent when a subscription is paused and the customer temporarily loses access.

No order is created while paused. The subscription resumes either on its
scheduled resume date or when resumed manually, starting a new billing period.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["subscription.paused"]*                                     | :heavy_check_mark:                                                   | N/A                                                                  | subscription.paused                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Subscription](../models/subscription.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |