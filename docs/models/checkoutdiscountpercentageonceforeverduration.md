# CheckoutDiscountPercentageOnceForeverDuration

Schema for a percentage discount that is applied once or forever.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `duration`                                               | [models.DiscountDuration](../models/discountduration.md) | :heavy_check_mark:                                       | N/A                                                      |
| `type`                                                   | [models.DiscountType](../models/discounttype.md)         | :heavy_check_mark:                                       | N/A                                                      |
| `basis_points`                                           | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The ID of the object.                                    |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `code`                                                   | *Nullable[str]*                                          | :heavy_check_mark:                                       | N/A                                                      |