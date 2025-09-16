# WebhookSubscriptionUncanceledPayload

Sent when a subscription is uncanceled.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["subscription.uncanceled"]*                                 | :heavy_check_mark:                                                   | N/A                                                                  | subscription.uncanceled                                              |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Subscription](../models/subscription.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |