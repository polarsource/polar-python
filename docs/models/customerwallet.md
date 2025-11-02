# CustomerWallet

A wallet represents your balance with an organization.

You can top-up your wallet and use the balance to pay for usage.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the object.                                                |                                                                      |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |                                                                      |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |                                                                      |
| `customer_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | The ID of the customer that owns the wallet.                         | 992fae2a-2a17-4b7a-8d9e-e287cf90131b                                 |
| `balance`                                                            | *int*                                                                | :heavy_check_mark:                                                   | The current balance of the wallet, in cents.                         | 5000                                                                 |
| `currency`                                                           | *str*                                                                | :heavy_check_mark:                                                   | The currency of the wallet.                                          | usd                                                                  |