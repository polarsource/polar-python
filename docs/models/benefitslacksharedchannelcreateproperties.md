# BenefitSlackSharedChannelCreateProperties


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `slack_integration_id`                           | *str*                                            | :heavy_check_mark:                               | Polar Slack integration to use for this benefit. |
| `channel_name_template`                          | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `private`                                        | *Optional[bool]*                                 | :heavy_minus_sign:                               | N/A                                              |
| `welcome_message`                                | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | N/A                                              |
| `archive_on_revoke`                              | *Optional[bool]*                                 | :heavy_minus_sign:                               | N/A                                              |
| `team_invitees`                                  | List[*str*]                                      | :heavy_minus_sign:                               | N/A                                              |