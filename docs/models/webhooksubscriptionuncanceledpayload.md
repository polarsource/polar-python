# WebhookSubscriptionUncanceledPayload

Sent when a customer revokes a pending cancellation.

When a customer cancels with "at period end", they retain access until the
subscription would renew. During this time, they can change their mind and
undo the cancellation. This event is triggered when they do so.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["subscription.uncanceled"]*                                 | :heavy_check_mark:                                                   | N/A                                                                  | subscription.uncanceled                                              |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Subscription](../models/subscription.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |