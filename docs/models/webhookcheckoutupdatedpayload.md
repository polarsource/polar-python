# WebhookCheckoutUpdatedPayload

Sent when a checkout is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `data`                                                 | [models.Checkout](../models/checkout.md)               | :heavy_check_mark:                                     | Checkout session data retrieved using an access token. |
| `type`                                                 | *Literal["checkout.updated"]*                          | :heavy_check_mark:                                     | N/A                                                    |