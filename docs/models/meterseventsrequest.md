# MetersEventsRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `id`                                            | *str*                                           | :heavy_check_mark:                              | The meter ID.                                   |
| `page`                                          | *Optional[int]*                                 | :heavy_minus_sign:                              | Page number, defaults to 1.                     |
| `limit`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | Size of a page, defaults to 10. Maximum is 100. |