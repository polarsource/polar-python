# OrderPaidMetadata


## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `order_id`                 | *str*                      | :heavy_check_mark:         | N/A                        |
| `product_id`               | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `billing_type`             | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `amount`                   | *int*                      | :heavy_check_mark:         | N/A                        |
| `currency`                 | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `net_amount`               | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `tax_amount`               | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `applied_balance_amount`   | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `discount_amount`          | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `discount_id`              | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `platform_fee`             | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |
| `subscription_id`          | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `recurring_interval`       | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `recurring_interval_count` | *Optional[int]*            | :heavy_minus_sign:         | N/A                        |