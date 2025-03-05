# FilesListRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `organization_id`                               | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | N/A                                             | 1dbfc517-0bbf-4301-9ba8-555ca42b9737            |
| `ids`                                           | List[*str*]                                     | :heavy_minus_sign:                              | List of file IDs to get.                        |                                                 |
| `page`                                          | *Optional[int]*                                 | :heavy_minus_sign:                              | Page number, defaults to 1.                     |                                                 |
| `limit`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | Size of a page, defaults to 10. Maximum is 100. |                                                 |