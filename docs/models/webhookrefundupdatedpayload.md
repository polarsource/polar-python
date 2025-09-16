# WebhookRefundUpdatedPayload

Sent when a refund is updated.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["refund.updated"]*                                          | :heavy_check_mark:                                                   | N/A                                                                  | refund.updated                                                       |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Refund](../models/refund.md)                                 | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |