# CustomerPortalCustomer


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `created_at`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | Creation timestamp of the object.                                                       |
| `modified_at`                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | Last modification timestamp of the object.                                              |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | The ID of the object.                                                                   |
| `email`                                                                                 | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `email_verified`                                                                        | *bool*                                                                                  | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `name`                                                                                  | *Nullable[str]*                                                                         | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `billing_address`                                                                       | [Nullable[models.Address]](../models/address.md)                                        | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `tax_id`                                                                                | List[[models.CustomerPortalCustomerTaxID](../models/customerportalcustomertaxid.md)]    | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `oauth_accounts`                                                                        | Dict[str, [models.CustomerPortalOAuthAccount](../models/customerportaloauthaccount.md)] | :heavy_check_mark:                                                                      | N/A                                                                                     |