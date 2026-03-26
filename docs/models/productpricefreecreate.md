# ProductPriceFreeCreate

Schema to create a free price.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `amount_type`                                                                                          | *Literal["free"]*                                                                                      | :heavy_check_mark:                                                                                     | N/A                                                                                                    |
| `price_currency`                                                                                       | [Optional[models.PresentmentCurrency]](../models/presentmentcurrency.md)                               | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `tax_behavior`                                                                                         | [OptionalNullable[models.TaxBehaviorOption]](../models/taxbehavioroption.md)                           | :heavy_minus_sign:                                                                                     | The tax behavior of the price. If not set, it will default to the organization's default tax behavior. |