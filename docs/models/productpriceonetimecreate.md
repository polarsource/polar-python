# ProductPriceOneTimeCreate

Schema to create a one-time product price.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `price_amount`                                                                     | *int*                                                                              | :heavy_check_mark:                                                                 | The price in cents.                                                                |
| `type`                                                                             | [models.ProductPriceOneTimeCreateType](../models/productpriceonetimecreatetype.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `price_currency`                                                                   | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The currency. Currently, only `usd` is supported.                                  |