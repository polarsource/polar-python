# MetricsResponse

Metrics response schema.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `periods`                                              | List[[models.MetricPeriod](../models/metricperiod.md)] | :heavy_check_mark:                                     | List of data for each timestamp.                       |
| `totals`                                               | [models.MetricsTotals](../models/metricstotals.md)     | :heavy_check_mark:                                     | N/A                                                    |
| `metrics`                                              | [models.Metrics](../models/metrics.md)                 | :heavy_check_mark:                                     | N/A                                                    |