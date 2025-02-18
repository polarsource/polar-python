# PolarOrders
(*customer_portal.orders*)

## Overview

### Available Operations

* [list](#list) - List Orders
* [get](#get) - Get Order
* [invoice](#invoice) - Get Order Invoice

## list

List orders of the authenticated customer or user.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_portal.orders.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                     | [OptionalNullable[models.CustomerPortalOrdersListQueryParamOrganizationIDFilter]](../../models/customerportalorderslistqueryparamorganizationidfilter.md)                             | :heavy_minus_sign:                                                                                                                                                                    | Filter by organization ID.                                                                                                                                                            |
| `product_id`                                                                                                                                                                          | [OptionalNullable[models.CustomerPortalOrdersListQueryParamProductIDFilter]](../../models/customerportalorderslistqueryparamproductidfilter.md)                                       | :heavy_minus_sign:                                                                                                                                                                    | Filter by product ID.                                                                                                                                                                 |
| `product_price_type`                                                                                                                                                                  | [OptionalNullable[models.QueryParamProductPriceTypeFilter]](../../models/queryparamproductpricetypefilter.md)                                                                         | :heavy_minus_sign:                                                                                                                                                                    | Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases. |
| `subscription_id`                                                                                                                                                                     | [OptionalNullable[models.CustomerPortalOrdersListQueryParamSubscriptionIDFilter]](../../models/customerportalorderslistqueryparamsubscriptionidfilter.md)                             | :heavy_minus_sign:                                                                                                                                                                    | Filter by subscription ID.                                                                                                                                                            |
| `query`                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Search by product or organization name.                                                                                                                                               |
| `page`                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Page number, defaults to 1.                                                                                                                                                           |
| `limit`                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Size of a page, defaults to 10. Maximum is 100.                                                                                                                                       |
| `sorting`                                                                                                                                                                             | List[[models.CustomerOrderSortProperty](../../models/customerordersortproperty.md)]                                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order.               |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.CustomerPortalOrdersListResponse](../../models/customerportalorderslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get an order by ID for the authenticated customer or user.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_portal.orders.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerOrder](../../models/customerorder.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## invoice

Get an order's invoice data.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_portal.orders.invoice(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerOrderInvoice](../../models/customerorderinvoice.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |