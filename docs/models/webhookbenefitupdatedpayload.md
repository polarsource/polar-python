# WebhookBenefitUpdatedPayload

Sent when a benefit is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["benefit.updated"]*                                         | :heavy_check_mark:                                                   | N/A                                                                  | benefit.updated                                                      |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Benefit](../models/benefit.md)                               | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |