# Products
(*products*)

## Overview

### Available Operations

* [products_list](#products_list) - List Products
* [products_create](#products_create) - Create Product
* [products_get](#products_get) - Get Product
* [products_update](#products_update) - Update Product
* [products_update_benefits](#products_update_benefits) - Update Product Benefits

## products_list

List products.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.products.products_list(security=polar_sh.ProductsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ProductsListRequest](../../models/productslistrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.ProductsListSecurity](../../productslistsecurity.md)        | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceProduct](../../models/listresourceproduct.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_create

Create a product.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.products.products_create(security=polar_sh.ProductsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "name": "<value>",
    "prices": [
        {
            "recurring_interval": polar_sh.ProductPriceRecurringInterval.YEAR,
            "price_amount": 978594,
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
| `security`                                                                        | [models.ProductsCreateSecurity](../../productscreatesecurity.md)                  | :heavy_check_mark:                                                                | The security requirements to use for the request.                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_get

Get a product by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.products.products_get(security=polar_sh.ProductsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ProductsGetSecurity](../../models/productsgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
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


## products_update

Update a product.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.products.products_update(security=polar_sh.ProductsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", product_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ProductsUpdateSecurity](../../models/productsupdatesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `product_update`                                                        | [models.ProductUpdate](../../models/productupdate.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_update_benefits

Update benefits granted by a product.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.products.products_update_benefits(security=polar_sh.ProductsUpdateBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", product_benefits_update={
    "benefits": [
        "<value>",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.ProductsUpdateBenefitsSecurity](../../models/productsupdatebenefitssecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `product_benefits_update`                                                               | [models.ProductBenefitsUpdate](../../models/productbenefitsupdate.md)                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
