# OrganizationFeatureSettingsUpdate

Feature settings that organizations can update themselves.

Other feature settings are managed by Polar staff: they're ignored if
provided and keep their current value.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `seat_based_pricing_enabled`                                  | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has seat-based pricing enabled           |
| `member_model_enabled`                                        | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has the Member model enabled             |
| `checkout_localization_enabled`                               | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has checkout localization enabled        |
| `overview_metrics`                                            | List[*str*]                                                   | :heavy_minus_sign:                                            | Ordered list of metric slugs shown on the dashboard overview. |