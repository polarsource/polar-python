# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [webhooks_list_webhook_endpoints](#webhooks_list_webhook_endpoints) - List Webhook Endpoints
* [webhooks_create_webhook_endpoint](#webhooks_create_webhook_endpoint) - Create Webhook Endpoint
* [webhooks_get_webhook_endpoint](#webhooks_get_webhook_endpoint) - Get Webhook Endpoint
* [webhooks_delete_webhook_endpoint](#webhooks_delete_webhook_endpoint) - Delete Webhook Endpoint
* [webhooks_update_webhook_endpoint](#webhooks_update_webhook_endpoint) - Update Webhook Endpoint
* [webhooks_list_webhook_deliveries](#webhooks_list_webhook_deliveries) - List Webhook Deliveries
* [webhooks_redeliver_webhook_event](#webhooks_redeliver_webhook_event) - Redeliver Webhook Event

## webhooks_list_webhook_endpoints

List webhook endpoints.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.webhooks.webhooks_list_webhook_endpoints(security=polar_sh.WebhooksListWebhookEndpointsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.WebhooksListWebhookEndpointsSecurity](../../models/webhookslistwebhookendpointssecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `organization_id`                                                                                   | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Filter by organization ID.                                                                          |
| `user_id`                                                                                           | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Filter by user ID.                                                                                  |
| `page`                                                                                              | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | Page number, defaults to 1.                                                                         |
| `limit`                                                                                             | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | Size of a page, defaults to 10. Maximum is 100.                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.ListResourceWebhookEndpoint](../../models/listresourcewebhookendpoint.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## webhooks_create_webhook_endpoint

Create a webhook endpoint.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.webhooks.webhooks_create_webhook_endpoint(security=polar_sh.WebhooksCreateWebhookEndpointSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "url": "https://webhook.site/cb791d80-f26e-4f8c-be88-6e56054192b0",
    "format": polar_sh.WebhookFormat.SLACK,
    "secret": "f_z6mfSpxkjogyw3FkA2aH2gYE5huxruNf34MpdWMcA",
    "events": [
        polar_sh.WebhookEventType.SUBSCRIPTION_CREATED,
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [models.WebhookEndpointCreate](../../models/webhookendpointcreate.md)                          | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [models.WebhooksCreateWebhookEndpointSecurity](../../webhookscreatewebhookendpointsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## webhooks_get_webhook_endpoint

Get a webhook endpoint by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.webhooks.webhooks_get_webhook_endpoint(security=polar_sh.WebhooksGetWebhookEndpointSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.WebhooksGetWebhookEndpointSecurity](../../models/webhooksgetwebhookendpointsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `id`                                                                                            | *str*                                                                                           | :heavy_check_mark:                                                                              | The webhook endpoint ID.                                                                        |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## webhooks_delete_webhook_endpoint

Delete a webhook endpoint.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.webhooks.webhooks_delete_webhook_endpoint(security=polar_sh.WebhooksDeleteWebhookEndpointSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.WebhooksDeleteWebhookEndpointSecurity](../../models/webhooksdeletewebhookendpointsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The webhook endpoint ID.                                                                              |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## webhooks_update_webhook_endpoint

Update a webhook endpoint.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.webhooks.webhooks_update_webhook_endpoint(security=polar_sh.WebhooksUpdateWebhookEndpointSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", webhook_endpoint_update={
    "url": "https://webhook.site/cb791d80-f26e-4f8c-be88-6e56054192b0",
    "secret": "f_z6mfSpxkjogyw3FkA2aH2gYE5huxruNf34MpdWMcA",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.WebhooksUpdateWebhookEndpointSecurity](../../models/webhooksupdatewebhookendpointsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The webhook endpoint ID.                                                                              |
| `webhook_endpoint_update`                                                                             | [models.WebhookEndpointUpdate](../../models/webhookendpointupdate.md)                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## webhooks_list_webhook_deliveries

List webhook deliveries.

Deliveries are all the attempts to deliver a webhook event to an endpoint.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.webhooks.webhooks_list_webhook_deliveries(security=polar_sh.WebhooksListWebhookDeliveriesSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.WebhooksListWebhookDeliveriesSecurity](../../models/webhookslistwebhookdeliveriessecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `endpoint_id`                                                                                         | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | Filter by webhook endpoint ID.                                                                        |
| `page`                                                                                                | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Page number, defaults to 1.                                                                           |
| `limit`                                                                                               | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Size of a page, defaults to 10. Maximum is 100.                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ListResourceWebhookDelivery](../../models/listresourcewebhookdelivery.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## webhooks_redeliver_webhook_event

Schedule the re-delivery of a webhook event.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.webhooks.webhooks_redeliver_webhook_event(security=polar_sh.WebhooksRedeliverWebhookEventSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.WebhooksRedeliverWebhookEventSecurity](../../models/webhooksredeliverwebhookeventsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The webhook event ID.                                                                                 |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
