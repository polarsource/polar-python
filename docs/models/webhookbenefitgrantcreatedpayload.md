# WebhookBenefitGrantCreatedPayload

Sent when a new benefit grant is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `type`                                                         | *Literal["benefit_grant.created"]*                             | :heavy_check_mark:                                             | N/A                                                            | benefit_grant.created                                          |
| `data`                                                         | [models.BenefitGrantWebhook](../models/benefitgrantwebhook.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |