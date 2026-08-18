# WebhookSubscriptionCycledPayload

Sent when a subscription enters a new billing period.

The payload carries the new `current_period_start` and `current_period_end`.
It fires when the period rolls over, before the renewal order exists and
regardless of whether the renewal payment succeeds — listen to `order.paid`
if you need the payment.

A trial converting to a paid subscription starts a new period, so it fires
there too. Read `status` to tell the two apart.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["subscription.cycled"]*                                     | :heavy_check_mark:                                                   | N/A                                                                  | subscription.cycled                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Subscription](../models/subscription.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |