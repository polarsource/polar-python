# TransactionOrder


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `product`                                                            | [models.TransactionProduct](../models/transactionproduct.md)         | :heavy_check_mark:                                                   | N/A                                                                  |
| `product_price`                                                      | [models.ProductPriceOutput](../models/productpriceoutput.md)         | :heavy_check_mark:                                                   | N/A                                                                  |
| `subscription_id`                                                    | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | N/A                                                                  |