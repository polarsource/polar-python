# WebhookSubscriptionActivePayload

Sent when a subscription becomes active,
whether because it's a new paid subscription or because payment was recovered.

**Discord & Slack support:** Full


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `data`                                                                                           | [models.Subscription](../models/subscription.md)                                                 | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `type`                                                                                           | [models.WebhookSubscriptionActivePayloadType](../models/webhooksubscriptionactivepayloadtype.md) | :heavy_check_mark:                                                                               | N/A                                                                                              |