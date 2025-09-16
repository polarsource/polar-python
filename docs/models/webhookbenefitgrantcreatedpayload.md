# WebhookBenefitGrantCreatedPayload

Sent when a new benefit grant is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["benefit_grant.created"]*                                   | :heavy_check_mark:                                                   | N/A                                                                  | benefit_grant.created                                                |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.BenefitGrantWebhook](../models/benefitgrantwebhook.md)       | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |