# OrganizationAvatarFileCreate

Schema to create a file to be used as an organization avatar.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `name`                                                                  | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `mime_type`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | MIME type of the file. Only images are supported for this type of file. |
| `size`                                                                  | *int*                                                                   | :heavy_check_mark:                                                      | Size of the file. A maximum of 1 MB is allowed for this type of file.   |
| `upload`                                                                | [models.S3FileCreateMultipart](../models/s3filecreatemultipart.md)      | :heavy_check_mark:                                                      | N/A                                                                     |
| `organization_id`                                                       | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |
| `checksum_sha256_base64`                                                | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |
| `service`                                                               | *Literal["organization_avatar"]*                                        | :heavy_check_mark:                                                      | N/A                                                                     |
| `version`                                                               | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |