# MetricDashboardSchema

A user-defined metrics dashboard.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the object.                                                |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Display name for the dashboard.                                      |
| `metrics`                                                            | List[*str*]                                                          | :heavy_check_mark:                                                   | List of metric slugs displayed in this dashboard.                    |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The ID of the organization owning this dashboard.                    |