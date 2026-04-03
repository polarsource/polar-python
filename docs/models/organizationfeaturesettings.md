# OrganizationFeatureSettings


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `issue_funding_enabled`                                       | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has issue funding enabled                |
| `seat_based_pricing_enabled`                                  | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has seat-based pricing enabled           |
| `revops_enabled`                                              | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has RevOps enabled                       |
| `wallets_enabled`                                             | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has Wallets enabled                      |
| `member_model_enabled`                                        | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has the Member model enabled             |
| `tinybird_read`                                               | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization reads from Tinybird                      |
| `tinybird_compare`                                            | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization compares Tinybird results with database  |
| `checkout_localization_enabled`                               | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has checkout localization enabled        |
| `overview_metrics`                                            | List[*str*]                                                   | :heavy_minus_sign:                                            | Ordered list of metric slugs shown on the dashboard overview. |
| `reset_proration_behavior_enabled`                            | *Optional[bool]*                                              | :heavy_minus_sign:                                            | If this organization has access to reset proration behavior.  |