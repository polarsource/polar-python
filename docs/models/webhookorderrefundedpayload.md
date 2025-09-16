# WebhookOrderRefundedPayload

Sent when an order is fully or partially refunded.

**Discord & Slack support:** Full


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["order.refunded"]*                                          | :heavy_check_mark:                                                   | N/A                                                                  | order.refunded                                                       |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Order](../models/order.md)                                   | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |