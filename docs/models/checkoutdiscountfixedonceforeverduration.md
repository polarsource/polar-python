# CheckoutDiscountFixedOnceForeverDuration

Schema for a fixed amount discount that is applied once or forever.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `duration`                                               | [models.DiscountDuration](../models/discountduration.md) | :heavy_check_mark:                                       | N/A                                                      |                                                          |
| `type`                                                   | [models.DiscountType](../models/discounttype.md)         | :heavy_check_mark:                                       | N/A                                                      |                                                          |
| `amount`                                                 | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      | 1000                                                     |
| `currency`                                               | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | usd                                                      |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The ID of the object.                                    |                                                          |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |                                                          |
| `code`                                                   | *Nullable[str]*                                          | :heavy_check_mark:                                       | N/A                                                      |                                                          |