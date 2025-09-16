# WebhookBenefitCreatedPayload

Sent when a new benefit is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["benefit.created"]*                                         | :heavy_check_mark:                                                   | N/A                                                                  | benefit.created                                                      |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Benefit](../models/benefit.md)                               | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |