# MemberSessionCreate

Schema for creating a member session using a member ID.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `member_id`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | ID of the member to create a session for.                                           |                                                                                     |
| `return_url`                                                                        | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | When set, a back button will be shown in the customer portal to return to this URL. | https://example.com/account                                                         |