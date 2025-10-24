# WebhookCustomerSeatAssignedPayload

Sent when a new customer seat is assigned.

This event is triggered when a seat is assigned to a customer by the organization.
The customer will receive an invitation email to claim the seat.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["customer_seat.assigned"]*                                  | :heavy_check_mark:                                                   | N/A                                                                  | customer_seat.assigned                                               |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.CustomerSeat](../models/customerseat.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |