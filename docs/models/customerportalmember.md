# CustomerPortalMember

A member of the customer's team as seen in the customer portal.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the object.                                                |
| `email`                                                              | *str*                                                                | :heavy_check_mark:                                                   | The email address of the member.                                     |
| `name`                                                               | *Nullable[str]*                                                      | :heavy_check_mark:                                                   | The name of the member.                                              |
| `role`                                                               | [models.MemberRole](../models/memberrole.md)                         | :heavy_check_mark:                                                   | N/A                                                                  |