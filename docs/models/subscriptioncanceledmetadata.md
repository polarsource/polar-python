# SubscriptionCanceledMetadata


## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `subscription_id`               | *str*                           | :heavy_check_mark:              | N/A                             |
| `product_id`                    | *Optional[str]*                 | :heavy_minus_sign:              | N/A                             |
| `amount`                        | *int*                           | :heavy_check_mark:              | N/A                             |
| `currency`                      | *str*                           | :heavy_check_mark:              | N/A                             |
| `recurring_interval`            | *str*                           | :heavy_check_mark:              | N/A                             |
| `recurring_interval_count`      | *int*                           | :heavy_check_mark:              | N/A                             |
| `customer_cancellation_reason`  | *Optional[str]*                 | :heavy_minus_sign:              | N/A                             |
| `customer_cancellation_comment` | *Optional[str]*                 | :heavy_minus_sign:              | N/A                             |
| `canceled_at`                   | *str*                           | :heavy_check_mark:              | N/A                             |
| `ends_at`                       | *Optional[str]*                 | :heavy_minus_sign:              | N/A                             |
| `cancel_at_period_end`          | *Optional[bool]*                | :heavy_minus_sign:              | N/A                             |