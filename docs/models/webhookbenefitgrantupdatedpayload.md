# WebhookBenefitGrantUpdatedPayload

Sent when a benefit grant is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["benefit_grant.updated"]*                                   | :heavy_check_mark:                                                   | N/A                                                                  | benefit_grant.updated                                                |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.BenefitGrantWebhook](../models/benefitgrantwebhook.md)       | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |