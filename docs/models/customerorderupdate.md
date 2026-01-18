# CustomerOrderUpdate

Schema to update an order.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `billing_name`                                                                                             | *OptionalNullable[str]*                                                                                    | :heavy_minus_sign:                                                                                         | The name of the customer that should appear on the invoice.                                                |
| `billing_address`                                                                                          | [OptionalNullable[models.AddressInput]](../models/addressinput.md)                                         | :heavy_minus_sign:                                                                                         | The address of the customer that should appear on the invoice. Country and state fields cannot be updated. |