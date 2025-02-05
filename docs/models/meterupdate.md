# MeterUpdate


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `metadata`                                                                | Dict[str, [models.MeterUpdateMetadata](../models/meterupdatemetadata.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `name`                                                                    | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | The name of the meter. Will be shown on customer's invoices and usage.    |
| `filter_`                                                                 | [OptionalNullable[models.Filter]](../models/filter_.md)                   | :heavy_minus_sign:                                                        | The filter to apply on events that'll be used to calculate the meter.     |
| `aggregation`                                                             | [OptionalNullable[models.Aggregation]](../models/aggregation.md)          | :heavy_minus_sign:                                                        | The aggregation to apply on the filtered events to calculate the meter.   |