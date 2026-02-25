# ProductPriceFixed

A fixed price for a product.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the price.                                                 |
| `source`                                                             | [models.ProductPriceSource](../models/productpricesource.md)         | :heavy_check_mark:                                                   | N/A                                                                  |
| `amount_type`                                                        | *Literal["fixed"]*                                                   | :heavy_check_mark:                                                   | N/A                                                                  |
| `price_currency`                                                     | *str*                                                                | :heavy_check_mark:                                                   | The currency in which the customer will be charged.                  |
| `is_archived`                                                        | *bool*                                                               | :heavy_check_mark:                                                   | Whether the price is archived and no longer available.               |
| `product_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The ID of the product owning the price.                              |
| `price_amount`                                                       | *int*                                                                | :heavy_check_mark:                                                   | The price in cents.                                                  |