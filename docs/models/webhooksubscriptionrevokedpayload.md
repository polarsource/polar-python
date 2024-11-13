# WebhookSubscriptionRevokedPayload

Sent when a subscription is revoked, the user looses access immediately.
Happens when the subscription is canceled, or payment is past due.

**Discord & Slack support:** Full


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `data`                                                                                             | [models.Subscription](../models/subscription.md)                                                   | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `type`                                                                                             | [models.WebhookSubscriptionRevokedPayloadType](../models/webhooksubscriptionrevokedpayloadtype.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |