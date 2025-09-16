# WebhookRefundCreatedPayload

Sent when a refund is created regardless of status.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["refund.created"]*                                          | :heavy_check_mark:                                                   | N/A                                                                  | refund.created                                                       |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Refund](../models/refund.md)                                 | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |