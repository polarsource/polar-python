# CustomersUpdateExternalRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `external_id`                                                            | *str*                                                                    | :heavy_check_mark:                                                       | The customer external ID.                                                |
| `include_members`                                                        | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Include members in the response. Only populated when set to true.        |
| `customer_update_external_id`                                            | [models.CustomerUpdateExternalID](../models/customerupdateexternalid.md) | :heavy_check_mark:                                                       | N/A                                                                      |