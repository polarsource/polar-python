# CustomersListPaymentMethodsExternalRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `external_id`                                   | *str*                                           | :heavy_check_mark:                              | The customer external ID.                       |
| `page`                                          | *Optional[int]*                                 | :heavy_minus_sign:                              | Page number, defaults to 1.                     |
| `limit`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | Size of a page, defaults to 10. Maximum is 100. |