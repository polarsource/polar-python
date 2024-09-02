# UserFreeSubscriptionCreate


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `product_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | ID of the free tier to subscribe to.                                                      |
| `customer_email`                                                                          | *OptionalNullable[str]*                                                                   | :heavy_minus_sign:                                                                        | Email of the customer. This field is required if the API is called outside the Polar app. |