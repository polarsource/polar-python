# WalletTopUpCreate

Request schema to top-up a wallet.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `amount`                                                                                 | *int*                                                                                    | :heavy_check_mark:                                                                       | The amount to top-up the wallet by, in cents.                                            | 2000                                                                                     |
| `currency`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | The currency. Currently, only `usd` is supported. It should match the wallet's currency. |                                                                                          |