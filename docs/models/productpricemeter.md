# ProductPriceMeter

A meter associated to a metered price.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | The ID of the object.                                      |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the meter.                                     |
| `unit`                                                     | [models.MeterUnit](../models/meterunit.md)                 | :heavy_check_mark:                                         | N/A                                                        |
| `custom_label`                                             | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The label for the custom unit.                             |
| `custom_multiplier`                                        | *OptionalNullable[int]*                                    | :heavy_minus_sign:                                         | The multiplier to convert from base unit to display scale. |