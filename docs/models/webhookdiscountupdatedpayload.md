# WebhookDiscountUpdatedPayload

Sent when a discount is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["discount.updated"]*                                        | :heavy_check_mark:                                                   | N/A                                                                  | discount.updated                                                     |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Discount](../models/discount.md)                             | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |