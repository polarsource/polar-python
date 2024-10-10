# PolarCheckoutLegacySchemasCheckout

A checkout session.


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *str*                                                           | :heavy_check_mark:                                              | The ID of the checkout.                                         |
| `customer_email`                                                | *Nullable[str]*                                                 | :heavy_check_mark:                                              | N/A                                                             |
| `customer_name`                                                 | *Nullable[str]*                                                 | :heavy_check_mark:                                              | N/A                                                             |
| `product`                                                       | [models.Product](../models/product.md)                          | :heavy_check_mark:                                              | A product.                                                      |
| `product_price`                                                 | [models.ProductPrice](../models/productprice.md)                | :heavy_check_mark:                                              | N/A                                                             |
| `url`                                                           | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | URL the customer should be redirected to complete the purchase. |