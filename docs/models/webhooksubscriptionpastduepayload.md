# WebhookSubscriptionPastDuePayload

Sent when a subscription payment fails and the subscription enters `past_due` status.

This is a recoverable state - the customer can update their payment method to restore the subscription.
Benefits may be revoked depending on the organization's grace period settings.

If payment retries are exhausted, a `subscription.revoked` event will be sent.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["subscription.past_due"]*                                   | :heavy_check_mark:                                                   | N/A                                                                  | subscription.past_due                                                |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Subscription](../models/subscription.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |