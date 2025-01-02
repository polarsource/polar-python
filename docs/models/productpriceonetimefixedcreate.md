# ProductPriceOneTimeFixedCreate

Schema to create a one-time product price.


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `price_amount`                                    | *int*                                             | :heavy_check_mark:                                | The price in cents.                               |
| `type`                                            | *Literal["one_time"]*                             | :heavy_check_mark:                                | N/A                                               |
| `amount_type`                                     | *Literal["fixed"]*                                | :heavy_check_mark:                                | N/A                                               |
| `price_currency`                                  | *Optional[str]*                                   | :heavy_minus_sign:                                | The currency. Currently, only `usd` is supported. |