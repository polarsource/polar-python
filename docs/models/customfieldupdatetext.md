# CustomFieldUpdateText

Schema to update a custom field of type text.


## Fields

| Field                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `metadata`                                                                                                                                                                                                                                                                                   | Dict[str, [models.CustomFieldUpdateTextMetadata](../models/customfieldupdatetextmetadata.md)]                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | Key-value object allowing you to store additional information.<br/><br/>The key must be a string with a maximum length of **40 characters**.<br/>The value must be either:<br/><br/>* A string with a maximum length of **500 characters**<br/>* An integer<br/>* A boolean<br/><br/>You can store up to **50 key-value pairs**. |
| `name`                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                          |
| `slug`                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                          |
| `type`                                                                                                                                                                                                                                                                                       | [models.CustomFieldUpdateTextType](../models/customfieldupdatetexttype.md)                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                          |
| `properties`                                                                                                                                                                                                                                                                                 | [OptionalNullable[models.CustomFieldTextProperties]](../models/customfieldtextproperties.md)                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                          |