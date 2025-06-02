# CustomerOrderUpdate

Schema to update an order.


## Fields

| Field                                                                                                           | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `billing_name`                                                                                                  | *Nullable[str]*                                                                                                 | :heavy_check_mark:                                                                                              | The name of the customer that should appear on the invoice. Can't be updated after the invoice is generated.    |
| `billing_address`                                                                                               | [Nullable[models.Address]](../models/address.md)                                                                | :heavy_check_mark:                                                                                              | The address of the customer that should appear on the invoice. Can't be updated after the invoice is generated. |