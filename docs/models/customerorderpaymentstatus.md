# CustomerOrderPaymentStatus

Payment status for an order.


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `status`                         | *str*                            | :heavy_check_mark:               | Current payment status.          |
| `error`                          | *OptionalNullable[str]*          | :heavy_minus_sign:               | Error message if payment failed. |