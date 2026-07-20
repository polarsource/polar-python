# CustomerPortalMemberUpdate

Schema for updating a member in the customer portal.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `name`                                                         | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The new name for the member.                                   | Jane Doe                                                       |
| `role`                                                         | [OptionalNullable[models.MemberRole]](../models/memberrole.md) | :heavy_minus_sign:                                             | The new role for the member.                                   |                                                                |