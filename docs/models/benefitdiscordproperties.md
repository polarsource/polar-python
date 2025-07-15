# BenefitDiscordProperties

Properties for a benefit of type `discord`.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `guild_id`                                                        | *str*                                                             | :heavy_check_mark:                                                | The ID of the Discord server.                                     |
| `role_id`                                                         | *str*                                                             | :heavy_check_mark:                                                | The ID of the Discord role to grant.                              |
| `kick_member`                                                     | *bool*                                                            | :heavy_check_mark:                                                | Whether to kick the member from the Discord server on revocation. |
| `guild_token`                                                     | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |