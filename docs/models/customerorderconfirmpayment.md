# CustomerOrderConfirmPayment

Schema to confirm a retry payment using a Stripe confirmation token.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `confirmation_token_id`                                            | *str*                                                              | :heavy_check_mark:                                                 | ID of the Stripe confirmation token.                               |
| `payment_processor`                                                | [Optional[models.PaymentProcessor]](../models/paymentprocessor.md) | :heavy_minus_sign:                                                 | N/A                                                                |