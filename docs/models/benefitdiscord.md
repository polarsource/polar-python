# BenefitDiscord

A benefit of type `discord`.

Use it to automatically invite your backers to a Discord server.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | The ID of the benefit.                                                   |
| `created_at`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_check_mark:                                                       | Creation timestamp of the object.                                        |
| `modified_at`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_check_mark:                                                       | Last modification timestamp of the object.                               |
| `type`                                                                   | *Literal["discord"]*                                                     | :heavy_check_mark:                                                       | N/A                                                                      |
| `description`                                                            | *str*                                                                    | :heavy_check_mark:                                                       | The description of the benefit.                                          |
| `selectable`                                                             | *bool*                                                                   | :heavy_check_mark:                                                       | Whether the benefit is selectable when creating a product.               |
| `deletable`                                                              | *bool*                                                                   | :heavy_check_mark:                                                       | Whether the benefit is deletable.                                        |
| `organization_id`                                                        | *str*                                                                    | :heavy_check_mark:                                                       | The ID of the organization owning the benefit.                           |
| `metadata`                                                               | Dict[str, [models.MetadataOutputType](../models/metadataoutputtype.md)]  | :heavy_check_mark:                                                       | N/A                                                                      |
| `properties`                                                             | [models.BenefitDiscordProperties](../models/benefitdiscordproperties.md) | :heavy_check_mark:                                                       | Properties for a benefit of type `discord`.                              |