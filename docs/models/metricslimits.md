# MetricsLimits

Date limits to get metrics.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `min_date`                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Minimum date to get metrics.                                                 |
| `intervals`                                                                  | [models.MetricsIntervalsLimits](../models/metricsintervalslimits.md)         | :heavy_check_mark:                                                           | Limits for each interval.                                                    |