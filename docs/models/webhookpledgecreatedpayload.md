# WebhookPledgeCreatedPayload

Sent when a new pledge is created. Note that this does mean that the pledge has been paid yet.

**Discord & Slack support:** Full


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `data`                                                                                 | [models.Pledge](../models/pledge.md)                                                   | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `type`                                                                                 | [models.WebhookPledgeCreatedPayloadType](../models/webhookpledgecreatedpayloadtype.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |