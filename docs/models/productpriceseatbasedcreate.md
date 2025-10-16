# ProductPriceSeatBasedCreate

Schema to create a seat-based price with volume-based tiers.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `amount_type`                                                      | *Literal["seat_based"]*                                            | :heavy_check_mark:                                                 | N/A                                                                |
| `price_currency`                                                   | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The currency. Currently, only `usd` is supported.                  |
| `seat_tiers`                                                       | [models.ProductPriceSeatTiers](../models/productpriceseattiers.md) | :heavy_check_mark:                                                 | List of pricing tiers for seat-based pricing.                      |