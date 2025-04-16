# WebhookBenefitGrantRevokedPayload

Sent when a benefit grant is revoked.

**Discord & Slack support:** Basic


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `type`                                                         | *Literal["benefit_grant.revoked"]*                             | :heavy_check_mark:                                             | N/A                                                            | benefit_grant.revoked                                          |
| `data`                                                         | [models.BenefitGrantWebhook](../models/benefitgrantwebhook.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |