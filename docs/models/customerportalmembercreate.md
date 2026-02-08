# CustomerPortalMemberCreate

Schema for adding a new member to the customer's team.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `email`                                                | *str*                                                  | :heavy_check_mark:                                     | The email address of the new member.                   |
| `name`                                                 | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | The name of the new member (optional).                 |
| `role`                                                 | [Optional[models.MemberRole]](../models/memberrole.md) | :heavy_minus_sign:                                     | N/A                                                    |