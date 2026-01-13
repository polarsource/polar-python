# ProductPriceSeatTiersInput

List of pricing tiers for seat-based pricing.

The minimum and maximum seat limits are derived from the tiers:
- minimum_seats = first tier's min_seats
- maximum_seats = last tier's max_seats (None for unlimited)


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `tiers`                                                                | List[[models.ProductPriceSeatTier](../models/productpriceseattier.md)] | :heavy_check_mark:                                                     | List of pricing tiers                                                  |