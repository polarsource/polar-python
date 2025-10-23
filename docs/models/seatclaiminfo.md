# SeatClaimInfo

Read-only information about a seat claim invitation.
Safe for email scanners - no side effects when fetched.


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `product_name`                              | *str*                                       | :heavy_check_mark:                          | Name of the product                         |
| `product_id`                                | *str*                                       | :heavy_check_mark:                          | ID of the product                           |
| `organization_name`                         | *str*                                       | :heavy_check_mark:                          | Name of the organization                    |
| `organization_slug`                         | *str*                                       | :heavy_check_mark:                          | Slug of the organization                    |
| `customer_email`                            | *str*                                       | :heavy_check_mark:                          | Email of the customer assigned to this seat |
| `can_claim`                                 | *bool*                                      | :heavy_check_mark:                          | Whether the seat can be claimed             |