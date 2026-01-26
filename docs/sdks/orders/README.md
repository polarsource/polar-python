# Orders
(*orders*)

## Overview

### Available Operations

* [list](#list) - List Orders
* [export](#export) - Export Subscriptions
* [get](#get) - Get Order
* [update](#update) - Update Order
* [generate_invoice](#generate_invoice) - Generate Order Invoice
* [invoice](#invoice) - Get Order Invoice

## list

List orders.

**Scopes**: `orders:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:list" method="get" path="/v1/orders/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                           | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                   | [OptionalNullable[models.OrdersListQueryParamOrganizationIDFilter]](../../models/orderslistqueryparamorganizationidfilter.md)                                                       | :heavy_minus_sign:                                                                                                                                                                  | Filter by organization ID.                                                                                                                                                          |
| `product_id`                                                                                                                                                                        | [OptionalNullable[models.OrdersListQueryParamProductIDFilter]](../../models/orderslistqueryparamproductidfilter.md)                                                                 | :heavy_minus_sign:                                                                                                                                                                  | Filter by product ID.                                                                                                                                                               |
| `product_billing_type`                                                                                                                                                              | [OptionalNullable[models.ProductBillingTypeFilter]](../../models/productbillingtypefilter.md)                                                                                       | :heavy_minus_sign:                                                                                                                                                                  | Filter by product billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases. |
| `discount_id`                                                                                                                                                                       | [OptionalNullable[models.QueryParamDiscountIDFilter]](../../models/queryparamdiscountidfilter.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                                  | Filter by discount ID.                                                                                                                                                              |
| `customer_id`                                                                                                                                                                       | [OptionalNullable[models.OrdersListQueryParamCustomerIDFilter]](../../models/orderslistqueryparamcustomeridfilter.md)                                                               | :heavy_minus_sign:                                                                                                                                                                  | Filter by customer ID.                                                                                                                                                              |
| `external_customer_id`                                                                                                                                                              | [OptionalNullable[models.OrdersListQueryParamExternalCustomerIDFilter]](../../models/orderslistqueryparamexternalcustomeridfilter.md)                                               | :heavy_minus_sign:                                                                                                                                                                  | Filter by customer external ID.                                                                                                                                                     |
| `checkout_id`                                                                                                                                                                       | [OptionalNullable[models.CheckoutIDFilter]](../../models/checkoutidfilter.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                                  | Filter by checkout ID.                                                                                                                                                              |
| `page`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | Page number, defaults to 1.                                                                                                                                                         |
| `limit`                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | Size of a page, defaults to 10. Maximum is 100.                                                                                                                                     |
| `sorting`                                                                                                                                                                           | List[[models.OrderSortProperty](../../models/ordersortproperty.md)]                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                  | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order.             |
| `metadata`                                                                                                                                                                          | Dict[str, [models.MetadataQuery](../../models/metadataquery.md)]                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`.                                                                                    |
| `retries`                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                 |

### Response

**[models.OrdersListResponse](../../models/orderslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## export

Export orders as a CSV file.

**Scopes**: `orders:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:export" method="get" path="/v1/orders/export" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.export(organization_id=None)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                 | [OptionalNullable[models.OrdersExportQueryParamOrganizationIDFilter]](../../models/ordersexportqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                | Filter by organization ID.                                                                                                        |
| `product_id`                                                                                                                      | [OptionalNullable[models.OrdersExportQueryParamProductIDFilter]](../../models/ordersexportqueryparamproductidfilter.md)           | :heavy_minus_sign:                                                                                                                | Filter by product ID.                                                                                                             |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get an order by ID.

**Scopes**: `orders:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:get" method="get" path="/v1/orders/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Order](../../models/order.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an order.

**Scopes**: `orders:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:update" method="patch" path="/v1/orders/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.update(id="<value>", order_update={
        "billing_address": {
            "country": polar_sdk.CountryAlpha2Input.US,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `order_update`                                                      | [models.OrderUpdate](../../models/orderupdate.md)                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Order](../../models/order.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## generate_invoice

Trigger generation of an order's invoice.

**Scopes**: `orders:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:generate_invoice" method="post" path="/v1/orders/{id}/invoice" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.generate_invoice(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.MissingInvoiceBillingDetails | 422                                 | application/json                    |
| models.NotPaidOrder                 | 422                                 | application/json                    |
| models.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## invoice

Get an order's invoice data.

**Scopes**: `orders:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:invoice" method="get" path="/v1/orders/{id}/invoice" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.invoice(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrderInvoice](../../models/orderinvoice.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |