# WebhookEndpointUpdate

Schema to update a webhook endpoint.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `url`                                                                | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  | https://webhook.site/cb791d80-f26e-4f8c-be88-6e56054192b0            |
| `format_`                                                            | [OptionalNullable[models.WebhookFormat]](../models/webhookformat.md) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `events`                                                             | List[[models.WebhookEventType](../models/webhookeventtype.md)]       | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `enabled`                                                            | *OptionalNullable[bool]*                                             | :heavy_minus_sign:                                                   | Whether the webhook endpoint is enabled.                             |                                                                      |