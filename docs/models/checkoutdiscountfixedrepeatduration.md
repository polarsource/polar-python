# CheckoutDiscountFixedRepeatDuration

Schema for a fixed amount discount that is applied on every invoice
for a certain number of months.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `duration`                                               | [models.DiscountDuration](../models/discountduration.md) | :heavy_check_mark:                                       | N/A                                                      |
| `duration_in_months`                                     | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `type`                                                   | [models.DiscountType](../models/discounttype.md)         | :heavy_check_mark:                                       | N/A                                                      |
| `amount`                                                 | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `currency`                                               | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The ID of the object.                                    |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `code`                                                   | *Nullable[str]*                                          | :heavy_check_mark:                                       | N/A                                                      |