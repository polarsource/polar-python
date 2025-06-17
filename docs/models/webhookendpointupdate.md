# WebhookEndpointUpdate

Schema to update a webhook endpoint.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `url`                                                                | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  | https://webhook.site/cb791d80-f26e-4f8c-be88-6e56054192b0            |
| `format_`                                                            | [OptionalNullable[models.WebhookFormat]](../models/webhookformat.md) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `secret`                                                             | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  | f_z6mfSpxkjogyw3FkA2aH2gYE5huxruNf34MpdWMcA                          |
| `events`                                                             | List[[models.WebhookEventType](../models/webhookeventtype.md)]       | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |