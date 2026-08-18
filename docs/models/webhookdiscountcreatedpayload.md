# WebhookDiscountCreatedPayload

Sent when a new discount is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["discount.created"]*                                        | :heavy_check_mark:                                                   | N/A                                                                  | discount.created                                                     |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Discount](../models/discount.md)                             | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |