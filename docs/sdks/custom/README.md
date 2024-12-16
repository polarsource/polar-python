# Custom
(*checkouts.custom*)

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

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CheckoutsCustomListQueryParamOrganizationIDFilter]](../../models/checkoutscustomlistqueryparamorganizationidfilter.md)                         | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `product_id`                                                                                                                                                            | [OptionalNullable[models.CheckoutsCustomListQueryParamProductIDFilter]](../../models/checkoutscustomlistqueryparamproductidfilter.md)                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by product ID.                                                                                                                                                   |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CheckoutSortProperty](../../models/checkoutsortproperty.md)]                                                                                               | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CheckoutsCustomListResponse](../../models/checkoutscustomlistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a checkout session.

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.create(request={
        "product_id": "<value>",
        "payment_processor": polar_sdk.CheckoutProductCreatePaymentProcessor.STRIPE,
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

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.get(id="<value>")

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

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.update(id="<value>", checkout_update={})

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## client_get

Get a checkout session by client secret.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.client_get(client_secret="<value>")

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## client_update

Update a checkout session by client secret.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.client_update(client_secret="<value>", checkout_update_public={})

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## client_confirm

Confirm a checkout session by client secret.

Orders and subscriptions will be processed.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.checkouts.custom.client_confirm(client_secret="<value>", checkout_confirm_stripe={})

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |