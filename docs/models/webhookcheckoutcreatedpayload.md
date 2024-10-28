# WebhookCheckoutCreatedPayload

Sent when a new checkout is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `data`                                                                                     | [models.PolarCheckoutSchemasCheckoutInput](../models/polarcheckoutschemascheckoutinput.md) | :heavy_check_mark:                                                                         | Checkout session data retrieved using an access token.                                     |
| `type`                                                                                     | [models.WebhookCheckoutCreatedPayloadType](../models/webhookcheckoutcreatedpayloadtype.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |