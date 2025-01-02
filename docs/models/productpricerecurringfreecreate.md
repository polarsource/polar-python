# ProductPriceRecurringFreeCreate

Schema to create a free recurring product price, i.e. a subscription.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `recurring_interval`                                                               | [models.SubscriptionRecurringInterval](../models/subscriptionrecurringinterval.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `type`                                                                             | *Literal["recurring"]*                                                             | :heavy_check_mark:                                                                 | N/A                                                                                |
| `amount_type`                                                                      | *Literal["free"]*                                                                  | :heavy_check_mark:                                                                 | N/A                                                                                |