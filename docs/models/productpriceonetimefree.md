# ProductPriceOneTimeFree

A free one-time price for a product.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the price.                                                 |
| `is_archived`                                                        | *bool*                                                               | :heavy_check_mark:                                                   | Whether the price is archived and no longer available.               |
| `product_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The ID of the product owning the price.                              |
| `amount_type`                                                        | *Literal["free"]*                                                    | :heavy_check_mark:                                                   | N/A                                                                  |
| `type`                                                               | *Literal["one_time"]*                                                | :heavy_check_mark:                                                   | The type of the price.                                               |