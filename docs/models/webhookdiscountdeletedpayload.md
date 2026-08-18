# WebhookDiscountDeletedPayload

Sent when a discount is deleted.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["discount.deleted"]*                                        | :heavy_check_mark:                                                   | N/A                                                                  | discount.deleted                                                     |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Discount](../models/discount.md)                             | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |