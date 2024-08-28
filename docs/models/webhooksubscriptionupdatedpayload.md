# WebhookSubscriptionUpdatedPayload

Sent when a new subscription is updated. This event fires if the subscription is cancelled, both immediately and if the subscription is cancelled at the end of the current period.

**Discord & Slack support:** On cancellation


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `data`                                                                                             | [models.SubscriptionInput](../models/subscriptioninput.md)                                         | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `type`                                                                                             | [models.WebhookSubscriptionUpdatedPayloadType](../models/webhooksubscriptionupdatedpayloadtype.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |