# PortalAuthenticatedUser

Information about the authenticated portal user.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Type of authenticated user: 'customer' or 'member'                  |
| `name`                                                              | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | User's name, if available.                                          |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | User's email address.                                               |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Associated customer ID.                                             |
| `role`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Member role (owner, billing_manager, member). Only set for members. |