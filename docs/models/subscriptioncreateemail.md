# SubscriptionCreateEmail

Request schema for creating a subscription by email.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `email`                                                        | *str*                                                          | :heavy_check_mark:                                             | The email address of the user.                                 |
| `product_id`                                                   | *str*                                                          | :heavy_check_mark:                                             | The ID of the product. **Must be the free subscription tier**. |