# ProductPriceSeatTier

A pricing tier for seat-based pricing.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `min_seats`                                              | *int*                                                    | :heavy_check_mark:                                       | Minimum number of seats (inclusive)                      |
| `max_seats`                                              | *OptionalNullable[int]*                                  | :heavy_minus_sign:                                       | Maximum number of seats (inclusive). None for unlimited. |
| `price_per_seat`                                         | *int*                                                    | :heavy_check_mark:                                       | Price per seat in cents for this tier                    |