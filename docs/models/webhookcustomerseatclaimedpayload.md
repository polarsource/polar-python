# WebhookCustomerSeatClaimedPayload

Sent when a customer seat is claimed.

This event is triggered when a customer accepts the seat invitation and claims their access.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["customer_seat.claimed"]*                                   | :heavy_check_mark:                                                   | N/A                                                                  | customer_seat.claimed                                                |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.CustomerSeat](../models/customerseat.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |