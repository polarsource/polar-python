# CustomerOrderPaymentConfirmation

Response after confirming a retry payment.


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `status`                                       | *str*                                          | :heavy_check_mark:                             | Payment status after confirmation.             |
| `client_secret`                                | *OptionalNullable[str]*                        | :heavy_minus_sign:                             | Client secret for handling additional actions. |
| `error`                                        | *OptionalNullable[str]*                        | :heavy_minus_sign:                             | Error message if confirmation failed.          |