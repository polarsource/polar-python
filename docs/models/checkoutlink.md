# CheckoutLink

Checkout link data.


## Fields

| Field                                                                                                                                                                      | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_at`                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                       | :heavy_check_mark:                                                                                                                                                         | Creation timestamp of the object.                                                                                                                                          |
| `modified_at`                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                       | :heavy_check_mark:                                                                                                                                                         | Last modification timestamp of the object.                                                                                                                                 |
| `id`                                                                                                                                                                       | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | The ID of the object.                                                                                                                                                      |
| `metadata`                                                                                                                                                                 | Dict[str, [models.CheckoutLinkMetadata](../models/checkoutlinkmetadata.md)]                                                                                                | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `client_secret`                                                                                                                                                            | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | Client secret used to access the checkout link.                                                                                                                            |
| `success_url`                                                                                                                                                              | *Nullable[str]*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                         | URL where the customer will be redirected after a successful payment.                                                                                                      |
| `label`                                                                                                                                                                    | *Nullable[str]*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                         | Optional label to distinguish links internally                                                                                                                             |
| `allow_discount_codes`                                                                                                                                                     | *bool*                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                         | Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it. |
| `product_id`                                                                                                                                                               | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | ID of the product to checkout.                                                                                                                                             |
| `product_price_id`                                                                                                                                                         | *Nullable[str]*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                         | ID of the product price to checkout. First available price will be selected unless an explicit price ID is set.                                                            |
| `discount_id`                                                                                                                                                              | *Nullable[str]*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                         | ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored.                                   |
| `product`                                                                                                                                                                  | [models.CheckoutLinkProduct](../models/checkoutlinkproduct.md)                                                                                                             | :heavy_check_mark:                                                                                                                                                         | Product data for a checkout link.                                                                                                                                          |
| `product_price`                                                                                                                                                            | [Nullable[models.ProductPrice]](../models/productprice.md)                                                                                                                 | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `discount`                                                                                                                                                                 | [Nullable[models.CheckoutLinkDiscount]](../models/checkoutlinkdiscount.md)                                                                                                 | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `url`                                                                                                                                                                      | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `payment_processor`                                                                                                                                                        | [models.PaymentProcessor](../models/paymentprocessor.md)                                                                                                                   | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |