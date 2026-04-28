# OrganizationCapabilities


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `checkout_payments`                                         | *bool*                                                      | :heavy_check_mark:                                          | Whether the organization can accept new checkout payments.  |
| `subscription_renewals`                                     | *bool*                                                      | :heavy_check_mark:                                          | Whether the organization can process subscription renewals. |
| `payouts`                                                   | *bool*                                                      | :heavy_check_mark:                                          | Whether the organization can withdraw its balance.          |
| `refunds`                                                   | *bool*                                                      | :heavy_check_mark:                                          | Whether the organization can issue refunds.                 |
| `api_access`                                                | *bool*                                                      | :heavy_check_mark:                                          | Whether the organization can access the API.                |
| `dashboard_access`                                          | *bool*                                                      | :heavy_check_mark:                                          | Whether the organization can access the dashboard.          |