# WebhookProductCreatedPayload

Sent when a new product is created.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["product.created"]*                                         | :heavy_check_mark:                                                   | N/A                                                                  | product.created                                                      |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Product](../models/product.md)                               | :heavy_check_mark:                                                   | A product.                                                           |                                                                      |