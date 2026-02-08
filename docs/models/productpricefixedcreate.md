# ProductPriceFixedCreate

Schema to create a fixed price.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `amount_type`                                                            | *Literal["fixed"]*                                                       | :heavy_check_mark:                                                       | N/A                                                                      |
| `price_currency`                                                         | [Optional[models.PresentmentCurrency]](../models/presentmentcurrency.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `price_amount`                                                           | *int*                                                                    | :heavy_check_mark:                                                       | The price in cents.                                                      |