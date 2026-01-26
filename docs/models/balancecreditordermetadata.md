# BalanceCreditOrderMetadata


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `order_id`              | *str*                   | :heavy_check_mark:      | N/A                     |
| `product_id`            | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `subscription_id`       | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `amount`                | *int*                   | :heavy_check_mark:      | N/A                     |
| `currency`              | *str*                   | :heavy_check_mark:      | N/A                     |
| `tax_amount`            | *int*                   | :heavy_check_mark:      | N/A                     |
| `tax_state`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `tax_country`           | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `fee`                   | *int*                   | :heavy_check_mark:      | N/A                     |