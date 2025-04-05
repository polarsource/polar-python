# AuthorizeResponseUser


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `client`                                                     | [models.OAuth2ClientPublic](../models/oauth2clientpublic.md) | :heavy_check_mark:                                           | N/A                                                          |
| `sub_type`                                                   | *Literal["user"]*                                            | :heavy_check_mark:                                           | N/A                                                          |
| `sub`                                                        | [Nullable[models.AuthorizeUser]](../models/authorizeuser.md) | :heavy_check_mark:                                           | N/A                                                          |
| `scopes`                                                     | List[[models.Scope](../models/scope.md)]                     | :heavy_check_mark:                                           | N/A                                                          |