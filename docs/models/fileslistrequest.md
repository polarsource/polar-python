# FilesListRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `organization_id`                               | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | N/A                                             |
| `ids`                                           | List[*str*]                                     | :heavy_minus_sign:                              | List of file IDs to get.                        |
| `page`                                          | *Optional[int]*                                 | :heavy_minus_sign:                              | Page number, defaults to 1.                     |
| `limit`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | Size of a page, defaults to 10. Maximum is 100. |