# MetricDashboardUpdate

Schema for updating a metrics dashboard.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | Display name for the dashboard.                    |
| `metrics`                                          | List[*str*]                                        | :heavy_minus_sign:                                 | List of metric slugs to display in this dashboard. |