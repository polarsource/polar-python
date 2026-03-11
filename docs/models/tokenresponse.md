# TokenResponse


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `access_token`          | *str*                   | :heavy_check_mark:      | N/A                     |
| `token_type`            | *Literal["Bearer"]*     | :heavy_check_mark:      | N/A                     |
| `expires_in`            | *int*                   | :heavy_check_mark:      | N/A                     |
| `refresh_token`         | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `scope`                 | *str*                   | :heavy_check_mark:      | N/A                     |
| `id_token`              | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |