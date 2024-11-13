# WebhookSubscriptionUpdatedPayload

Sent when a subscription is updated. This event fires for all changes to the subscription, including renewals.

If you want more specific events, you can listen to `subscription.active`, `subscription.canceled`, and `subscription.revoked`.

To listen specifically for renewals, you can listen to `order.created` events and check the `billing_reason` field.

**Discord & Slack support:** On cancellation and revocation. Renewals are skipped.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `data`                                                                                             | [models.Subscription](../models/subscription.md)                                                   | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `type`                                                                                             | [models.WebhookSubscriptionUpdatedPayloadType](../models/webhooksubscriptionupdatedpayloadtype.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |