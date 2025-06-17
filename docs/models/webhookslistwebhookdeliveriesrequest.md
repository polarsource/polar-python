# WebhooksListWebhookDeliveriesRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `endpoint_id`                                                  | [OptionalNullable[models.EndpointID]](../models/endpointid.md) | :heavy_minus_sign:                                             | Filter by webhook endpoint ID.                                 |
| `page`                                                         | *Optional[int]*                                                | :heavy_minus_sign:                                             | Page number, defaults to 1.                                    |
| `limit`                                                        | *Optional[int]*                                                | :heavy_minus_sign:                                             | Size of a page, defaults to 10. Maximum is 100.                |