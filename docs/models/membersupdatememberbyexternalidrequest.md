# MembersUpdateMemberByExternalIDRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `external_id`                                    | *str*                                            | :heavy_check_mark:                               | The member external ID.                          |
| `customer_id`                                    | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The customer ID.                                 |
| `external_customer_id`                           | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The customer external ID.                        |
| `member_update`                                  | [models.MemberUpdate](../models/memberupdate.md) | :heavy_check_mark:                               | N/A                                              |