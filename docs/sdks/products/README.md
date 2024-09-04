# Products
(*products*)

## Overview

### Available Operations

* [list](#list) - List Products
* [create](#create) - Create Product
* [get](#get) - Get Product
* [update](#update) - Update Product
* [update_benefits](#update_benefits) - Update Product Benefits

## list

List products.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.products.list()

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                          | [OptionalNullable[models.ProductsListQueryParamOrganizationIDFilter]](../../models/productslistqueryparamorganizationidfilter.md)          | :heavy_minus_sign:                                                                                                                         | Filter by organization ID.                                                                                                                 |
| `is_archived`                                                                                                                              | *OptionalNullable[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                         | Filter on archived products.                                                                                                               |
| `is_recurring`                                                                                                                             | *OptionalNullable[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                         | Filter on recurring products. If `true`, only subscriptions tiers are returned. If `false`, only one-time purchase products are returned.  |
| `benefit_id`                                                                                                                               | [OptionalNullable[models.QueryParamBenefitIDFilter]](../../models/queryparambenefitidfilter.md)                                            | :heavy_minus_sign:                                                                                                                         | Filter products granting specific benefit.                                                                                                 |
| `type_filter`                                                                                                                              | [OptionalNullable[models.QueryParamSubscriptionTierTypeFilter]](../../models/queryparamsubscriptiontiertypefilter.md)                      | :heavy_minus_sign:                                                                                                                         | Filter by subscription tier type.                                                                                                          |
| `page`                                                                                                                                     | *Optional[int]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Page number, defaults to 1.                                                                                                                |
| `limit`                                                                                                                                    | *Optional[int]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Size of a page, defaults to 10. Maximum is 100.                                                                                            |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[models.ProductsListResponse](../../models/productslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create a product.

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.products.create(request={
    "name": "<value>",
    "prices": [
        {
            "recurring_interval": polar_sdk.ProductPriceRecurringInterval.MONTH,
            "price_amount": 638424,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.ProductsCreateProductCreate](../../models/productscreateproductcreate.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## get

Get a product by ID.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.products.get(id="<value>")

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

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update a product.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.products.update(id="<value>", product_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `product_update`                                                    | [models.ProductUpdate](../../models/productupdate.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update_benefits

Update benefits granted by a product.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.products.update_benefits(id="<value>", product_benefits_update={
    "benefits": [
        "<value>",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `product_benefits_update`                                             | [models.ProductBenefitsUpdate](../../models/productbenefitsupdate.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
