# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [list_webhook_endpoints](#list_webhook_endpoints) - List Webhook Endpoints
* [create_webhook_endpoint](#create_webhook_endpoint) - Create Webhook Endpoint
* [get_webhook_endpoint](#get_webhook_endpoint) - Get Webhook Endpoint
* [update_webhook_endpoint](#update_webhook_endpoint) - Update Webhook Endpoint
* [delete_webhook_endpoint](#delete_webhook_endpoint) - Delete Webhook Endpoint
* [reset_webhook_endpoint_secret](#reset_webhook_endpoint_secret) - Reset Webhook Endpoint Secret
* [list_webhook_deliveries](#list_webhook_deliveries) - List Webhook Deliveries
* [redeliver_webhook_event](#redeliver_webhook_event) - Redeliver Webhook Event

## list_webhook_endpoints

List webhook endpoints.

**Scopes**: `webhooks:read` `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:list_webhook_endpoints" method="get" path="/v1/webhooks/endpoints" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.list_webhook_endpoints(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organization_id`                                                                             | [OptionalNullable[models.QueryParamOrganizationID]](../../models/queryparamorganizationid.md) | :heavy_minus_sign:                                                                            | Filter by organization ID.                                                                    |
| `page`                                                                                        | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | Page number, defaults to 1.                                                                   |
| `limit`                                                                                       | *Optional[int]*                                                                               | :heavy_minus_sign:                                                                            | Size of a page, defaults to 10. Maximum is 100.                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.WebhooksListWebhookEndpointsResponse](../../models/webhookslistwebhookendpointsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_webhook_endpoint

Create a webhook endpoint.

**Scopes**: `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:create_webhook_endpoint" method="post" path="/v1/webhooks/endpoints" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.create_webhook_endpoint(request={
        "url": "https://webhook.site/cb791d80-f26e-4f8c-be88-6e56054192b0",
        "format_": polar_sdk.WebhookFormat.SLACK,
        "events": [
            polar_sdk.WebhookEventType.SUBSCRIPTION_UNCANCELED,
        ],
        "organization_id": "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.WebhookEndpointCreate](../../models/webhookendpointcreate.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_webhook_endpoint

Get a webhook endpoint by ID.

**Scopes**: `webhooks:read` `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:get_webhook_endpoint" method="get" path="/v1/webhooks/endpoints/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.get_webhook_endpoint(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The webhook endpoint ID.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_webhook_endpoint

Update a webhook endpoint.

**Scopes**: `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:update_webhook_endpoint" method="patch" path="/v1/webhooks/endpoints/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.update_webhook_endpoint(id="<value>", webhook_endpoint_update={
        "url": "https://webhook.site/cb791d80-f26e-4f8c-be88-6e56054192b0",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | The webhook endpoint ID.                                              |
| `webhook_endpoint_update`                                             | [models.WebhookEndpointUpdate](../../models/webhookendpointupdate.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_webhook_endpoint

Delete a webhook endpoint.

**Scopes**: `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:delete_webhook_endpoint" method="delete" path="/v1/webhooks/endpoints/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.webhooks.delete_webhook_endpoint(id="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The webhook endpoint ID.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## reset_webhook_endpoint_secret

Regenerate a webhook endpoint secret.

**Scopes**: `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:reset_webhook_endpoint_secret" method="patch" path="/v1/webhooks/endpoints/{id}/secret" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.reset_webhook_endpoint_secret(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The webhook endpoint ID.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookEndpoint](../../models/webhookendpoint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_webhook_deliveries

List webhook deliveries.

Deliveries are all the attempts to deliver a webhook event to an endpoint.

**Scopes**: `webhooks:read` `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:list_webhook_deliveries" method="get" path="/v1/webhooks/deliveries" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.list_webhook_deliveries(page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `endpoint_id`                                                        | [OptionalNullable[models.EndpointID]](../../models/endpointid.md)    | :heavy_minus_sign:                                                   | Filter by webhook endpoint ID.                                       |
| `start_timestamp`                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Filter deliveries after this timestamp.                              |
| `end_timestamp`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Filter deliveries before this timestamp.                             |
| `page`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Page number, defaults to 1.                                          |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Size of a page, defaults to 10. Maximum is 100.                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.WebhooksListWebhookDeliveriesResponse](../../models/webhookslistwebhookdeliveriesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## redeliver_webhook_event

Schedule the re-delivery of a webhook event.

**Scopes**: `webhooks:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="webhooks:redeliver_webhook_event" method="post" path="/v1/webhooks/events/{id}/redeliver" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.webhooks.redeliver_webhook_event(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The webhook event ID.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |