# BenefitMeterCredit

A benefit of type `meter_unit`.

Use it to grant a number of units on a specific meter.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `created_at`                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)             | :heavy_check_mark:                                                               | Creation timestamp of the object.                                                |
| `modified_at`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)             | :heavy_check_mark:                                                               | Last modification timestamp of the object.                                       |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the benefit.                                                           |
| `description`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | The description of the benefit.                                                  |
| `selectable`                                                                     | *bool*                                                                           | :heavy_check_mark:                                                               | Whether the benefit is selectable when creating a product.                       |
| `deletable`                                                                      | *bool*                                                                           | :heavy_check_mark:                                                               | Whether the benefit is deletable.                                                |
| `organization_id`                                                                | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the organization owning the benefit.                                   |
| `properties`                                                                     | [models.BenefitMeterCreditProperties](../models/benefitmetercreditproperties.md) | :heavy_check_mark:                                                               | Properties for a benefit of type `meter_unit`.                                   |
| `type`                                                                           | *Literal["meter_credit"]*                                                        | :heavy_check_mark:                                                               | N/A                                                                              |