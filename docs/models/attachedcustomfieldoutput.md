# AttachedCustomFieldOutput

Schema of a custom field attached to a resource.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `custom_field_id`                                    | *str*                                                | :heavy_check_mark:                                   | ID of the custom field.                              |
| `custom_field`                                       | [models.CustomField](../models/customfield.md)       | :heavy_check_mark:                                   | N/A                                                  |
| `order`                                              | *int*                                                | :heavy_check_mark:                                   | Order of the custom field in the resource.           |
| `required`                                           | *bool*                                               | :heavy_check_mark:                                   | Whether the value is required for this custom field. |