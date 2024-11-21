# DiscountProduct

A product that a discount can be applied to.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the product.                                               |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The name of the product.                                             |
| `description`                                                        | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | The description of the product.                                      |
| `is_recurring`                                                       | *bool*                                                               | :heavy_check_mark:                                                   | Whether the product is a subscription tier.                          |
| `is_archived`                                                        | *bool*                                                               | :heavy_check_mark:                                                   | Whether the product is archived and no longer available.             |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The ID of the organization owning the product.                       |