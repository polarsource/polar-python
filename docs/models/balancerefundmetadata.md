# BalanceRefundMetadata


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `transaction_id`        | *str*                   | :heavy_check_mark:      | N/A                     |
| `refund_id`             | *str*                   | :heavy_check_mark:      | N/A                     |
| `order_id`              | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `order_created_at`      | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `product_id`            | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `subscription_id`       | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `amount`                | *int*                   | :heavy_check_mark:      | N/A                     |
| `currency`              | *str*                   | :heavy_check_mark:      | N/A                     |
| `presentment_amount`    | *int*                   | :heavy_check_mark:      | N/A                     |
| `presentment_currency`  | *str*                   | :heavy_check_mark:      | N/A                     |
| `refundable_amount`     | *Optional[int]*         | :heavy_minus_sign:      | N/A                     |
| `tax_amount`            | *int*                   | :heavy_check_mark:      | N/A                     |
| `tax_state`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `tax_country`           | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `fee`                   | *int*                   | :heavy_check_mark:      | N/A                     |