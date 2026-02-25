# WebhookCheckoutExpiredPayload

Sent when a checkout expires.

This event fires when a checkout reaches its expiration time without being completed.
Developers can use this to send reminder emails or track checkout abandonment.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["checkout.expired"]*                                        | :heavy_check_mark:                                                   | N/A                                                                  | checkout.expired                                                     |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Checkout](../models/checkout.md)                             | :heavy_check_mark:                                                   | Checkout session data retrieved using an access token.               |                                                                      |