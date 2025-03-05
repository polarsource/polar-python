# WebhookBenefitGrantRevokedPayload

Sent when a new benefit grant is revoked.

**Discord & Slack support:** Basic


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `data`                                                         | [models.BenefitGrantWebhook](../models/benefitgrantwebhook.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |
| `type`                                                         | *Literal["benefit_grant.revoked"]*                             | :heavy_check_mark:                                             | N/A                                                            | benefit_grant.revoked                                          |