# Checkouts
(*checkouts*)

## Overview

### Available Operations

* [~~create~~](#create) - Create Checkout :warning: **Deprecated** Use [create](docs/sdks/custom/README.md#create) instead.
* [~~get~~](#get) - Get Checkout :warning: **Deprecated**

## ~~create~~

Create a checkout session.

> :warning: **DEPRECATED**: This API is deprecated. We recommend you to use the new custom checkout API, which is more flexible and powerful. Please refer to the documentation for more information.. Use `create` instead.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.checkouts.create(request={
        "product_price_id": "<value>",
        "success_url": "http://limp-pastry.org",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CheckoutLegacyCreate](../../models/checkoutlegacycreate.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckoutLegacy](../../models/checkoutlegacy.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## ~~get~~

Get an active checkout session by ID.

> :warning: **DEPRECATED**: This API is deprecated. We recommend you to use the new custom checkout API, which is more flexible and powerful. Please refer to the documentation for more information..

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.checkouts.get(id="<id>")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckoutLegacy](../../models/checkoutlegacy.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |