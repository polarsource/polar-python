# CustomerSession

A customer session that can be used to authenticate as a customer.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the object.                                                |
| `token`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `customer_portal_url`                                                | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `customer_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `customer`                                                           | [models.Customer](../models/customer.md)                             | :heavy_check_mark:                                                   | A customer in an organization.                                       |