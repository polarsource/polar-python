# ProductPriceRecurringFixedCreate

Schema to create a recurring product price, i.e. a subscription.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `price_amount`                                                                     | *int*                                                                              | :heavy_check_mark:                                                                 | The price in cents.                                                                |
| `recurring_interval`                                                               | [models.SubscriptionRecurringInterval](../models/subscriptionrecurringinterval.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `type`                                                                             | *Literal["recurring"]*                                                             | :heavy_check_mark:                                                                 | N/A                                                                                |
| `amount_type`                                                                      | *Literal["fixed"]*                                                                 | :heavy_check_mark:                                                                 | N/A                                                                                |
| `price_currency`                                                                   | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The currency. Currently, only `usd` is supported.                                  |