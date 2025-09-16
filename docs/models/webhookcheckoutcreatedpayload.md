# WebhookCheckoutCreatedPayload

Sent when a new checkout is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["checkout.created"]*                                        | :heavy_check_mark:                                                   | N/A                                                                  | checkout.created                                                     |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Checkout](../models/checkout.md)                             | :heavy_check_mark:                                                   | Checkout session data retrieved using an access token.               |                                                                      |