# PaymentMethodCard


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `type`                                                               | *Literal["card"]*                                                    | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `default`                                                            | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `card`                                                               | [models.PaymentMethodCardData](../models/paymentmethodcarddata.md)   | :heavy_check_mark:                                                   | N/A                                                                  |