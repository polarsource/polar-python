# WebhookCheckoutUpdatedPayload

Sent when a checkout is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `data`                                                                                     | [models.PolarCheckoutSchemasCheckoutInput](../models/polarcheckoutschemascheckoutinput.md) | :heavy_check_mark:                                                                         | Checkout session data retrieved using an access token.                                     |
| `type`                                                                                     | [models.WebhookCheckoutUpdatedPayloadType](../models/webhookcheckoutupdatedpayloadtype.md) | :heavy_check_mark:                                                                         | N/A                                                                                        |