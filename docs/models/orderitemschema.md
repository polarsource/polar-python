# OrderItemSchema

An order line item.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the object.                                                |
| `label`                                                              | *str*                                                                | :heavy_check_mark:                                                   | Description of the line item charge.                                 |
| `amount`                                                             | *int*                                                                | :heavy_check_mark:                                                   | Amount in cents, before discounts and taxes.                         |
| `tax_amount`                                                         | *int*                                                                | :heavy_check_mark:                                                   | Sales tax amount in cents.                                           |
| `proration`                                                          | *bool*                                                               | :heavy_check_mark:                                                   | Whether this charge is due to a proration.                           |
| `product_price_id`                                                   | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | Associated price ID, if any.                                         |