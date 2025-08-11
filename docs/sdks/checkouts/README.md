# Checkouts
(*checkouts*)

## Overview

### Available Operations

* [list](#list) - List Checkout Sessions
* [create](#create) - Create Checkout Session
* [get](#get) - Get Checkout Session
* [update](#update) - Update Checkout Session
* [client_get](#client_get) - Get Checkout Session from Client
* [client_update](#client_update) - Update Checkout Session from Client
* [client_confirm](#client_confirm) - Confirm Checkout Session from Client

## list

List checkout sessions.

**Scopes**: `checkouts:read` `checkouts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:list" method="get" path="/v1/checkouts/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CheckoutsListQueryParamOrganizationIDFilter]](../../models/checkoutslistqueryparamorganizationidfilter.md)                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `product_id`                                                                                                                                                            | [OptionalNullable[models.CheckoutsListQueryParamProductIDFilter]](../../models/checkoutslistqueryparamproductidfilter.md)                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by product ID.                                                                                                                                                   |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.CheckoutsListQueryParamCustomerIDFilter]](../../models/checkoutslistqueryparamcustomeridfilter.md)                                             | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `status`                                                                                                                                                                | [OptionalNullable[models.StatusFilter]](../../models/statusfilter.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by checkout session status.                                                                                                                                      |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by customer email.                                                                                                                                               |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CheckoutSortProperty](../../models/checkoutsortproperty.md)]                                                                                               | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CheckoutsListResponse](../../models/checkoutslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a checkout session.

**Scopes**: `checkouts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:create" method="post" path="/v1/checkouts/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.create(request={
        "customer_billing_address": {
            "country": "US",
        },
        "products": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CheckoutCreate](../../models/checkoutcreate.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Checkout](../../models/checkout.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a checkout session by ID.

**Scopes**: `checkouts:read` `checkouts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:get" method="get" path="/v1/checkouts/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The checkout session ID.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Checkout](../../models/checkout.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a checkout session.

**Scopes**: `checkouts:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:update" method="patch" path="/v1/checkouts/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.update(id="<value>", checkout_update={
        "customer_billing_address": {
            "country": "US",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The checkout session ID.                                            |
| `checkout_update`                                                   | [models.CheckoutUpdate](../../models/checkoutupdate.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Checkout](../../models/checkout.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.AlreadyActiveSubscriptionError | 403                                   | application/json                      |
| models.NotOpenCheckout                | 403                                   | application/json                      |
| models.PaymentNotReady                | 403                                   | application/json                      |
| models.ResourceNotFound               | 404                                   | application/json                      |
| models.HTTPValidationError            | 422                                   | application/json                      |
| models.SDKError                       | 4XX, 5XX                              | \*/\*                                 |

## client_get

Get a checkout session by client secret.

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:client_get" method="get" path="/v1/checkouts/client/{client_secret}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.client_get(client_secret="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The checkout session client secret.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckoutPublic](../../models/checkoutpublic.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ResourceNotFound     | 404                         | application/json            |
| models.ExpiredCheckoutError | 410                         | application/json            |
| models.HTTPValidationError  | 422                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

## client_update

Update a checkout session by client secret.

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:client_update" method="patch" path="/v1/checkouts/client/{client_secret}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.client_update(client_secret="<value>", checkout_update_public={
        "customer_billing_address": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_secret`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The checkout session client secret.                                 |
| `checkout_update_public`                                            | [models.CheckoutUpdatePublic](../../models/checkoutupdatepublic.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckoutPublic](../../models/checkoutpublic.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.AlreadyActiveSubscriptionError | 403                                   | application/json                      |
| models.NotOpenCheckout                | 403                                   | application/json                      |
| models.PaymentNotReady                | 403                                   | application/json                      |
| models.ResourceNotFound               | 404                                   | application/json                      |
| models.ExpiredCheckoutError           | 410                                   | application/json                      |
| models.HTTPValidationError            | 422                                   | application/json                      |
| models.SDKError                       | 4XX, 5XX                              | \*/\*                                 |

## client_confirm

Confirm a checkout session by client secret.

Orders and subscriptions will be processed.

### Example Usage

<!-- UsageSnippet language="python" operationID="checkouts:client_confirm" method="post" path="/v1/checkouts/client/{client_secret}/confirm" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.client_confirm(client_secret="<value>", checkout_confirm_stripe={
        "customer_billing_address": {
            "country": "US",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `client_secret`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | The checkout session client secret.                                   |
| `checkout_confirm_stripe`                                             | [models.CheckoutConfirmStripe](../../models/checkoutconfirmstripe.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CheckoutPublicConfirmed](../../models/checkoutpublicconfirmed.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.PaymentError                   | 400                                   | application/json                      |
| models.AlreadyActiveSubscriptionError | 403                                   | application/json                      |
| models.NotOpenCheckout                | 403                                   | application/json                      |
| models.PaymentNotReady                | 403                                   | application/json                      |
| models.ResourceNotFound               | 404                                   | application/json                      |
| models.ExpiredCheckoutError           | 410                                   | application/json                      |
| models.HTTPValidationError            | 422                                   | application/json                      |
| models.SDKError                       | 4XX, 5XX                              | \*/\*                                 |