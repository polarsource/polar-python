# DiscountFixedRepeatDurationBase


## Fields

| Field                                                                                                             | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `duration`                                                                                                        | [models.DiscountDuration](../models/discountduration.md)                                                          | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `duration_in_months`                                                                                              | *int*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `type`                                                                                                            | [models.DiscountType](../models/discounttype.md)                                                                  | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `amount`                                                                                                          | *int*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `currency`                                                                                                        | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `created_at`                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_check_mark:                                                                                                | Creation timestamp of the object.                                                                                 |
| `modified_at`                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_check_mark:                                                                                                | Last modification timestamp of the object.                                                                        |
| `id`                                                                                                              | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The ID of the object.                                                                                             |
| `metadata`                                                                                                        | Dict[str, [models.DiscountFixedRepeatDurationBaseMetadata](../models/discountfixedrepeatdurationbasemetadata.md)] | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `name`                                                                                                            | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Name of the discount. Will be displayed to the customer when the discount is applied.                             |
| `code`                                                                                                            | *Nullable[str]*                                                                                                   | :heavy_check_mark:                                                                                                | Code customers can use to apply the discount during checkout.                                                     |
| `starts_at`                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_check_mark:                                                                                                | Timestamp after which the discount is redeemable.                                                                 |
| `ends_at`                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_check_mark:                                                                                                | Timestamp after which the discount is no longer redeemable.                                                       |
| `max_redemptions`                                                                                                 | *Nullable[int]*                                                                                                   | :heavy_check_mark:                                                                                                | Maximum number of times the discount can be redeemed.                                                             |
| `redemptions_count`                                                                                               | *int*                                                                                                             | :heavy_check_mark:                                                                                                | Number of times the discount has been redeemed.                                                                   |
| `organization_id`                                                                                                 | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The organization ID.                                                                                              |