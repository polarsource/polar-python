# ProductPriceRecurringCreate

Schema to create a recurring product price, i.e. a subscription.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `recurring_interval`                                                                   | [models.ProductPriceRecurringInterval](../models/productpricerecurringinterval.md)     | :heavy_check_mark:                                                                     | The recurring interval of the price.                                                   |
| `price_amount`                                                                         | *int*                                                                                  | :heavy_check_mark:                                                                     | The price in cents.                                                                    |
| `type`                                                                                 | [models.ProductPriceRecurringCreateType](../models/productpricerecurringcreatetype.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `price_currency`                                                                       | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The currency. Currently, only `usd` is supported.                                      |