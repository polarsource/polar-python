# Orders
(*orders*)

## Overview

### Available Operations

* [list](#list) - List Orders
* [create](#create) - Create Order
* [export](#export) - Export Orders
* [get](#get) - Get Order
* [update](#update) - Update Order
* [finalize](#finalize) - Finalize Order
* [generate_invoice](#generate_invoice) - Generate Order Invoice
* [invoice](#invoice) - Get Order Invoice
* [receipt](#receipt) - Get Order Receipt

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
| `subscription_id`                                                                                                                                                                   | [OptionalNullable[models.SubscriptionIDFilter]](../../models/subscriptionidfilter.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                  | Filter by subscription ID.                                                                                                                                                          |
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

## create

Create a draft order for an off-session charge against a saved payment
method. The order is created with `status=draft` and no invoice number;
call `POST /v1/orders/{id}/finalize` to attempt the charge.

The organization must have the `off_session_charges_enabled` feature flag.

**Scopes**: `orders:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:create" method="post" path="/v1/orders/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.create(request={
        "organization_id": "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
        "customer_id": "<value>",
        "product_id": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.OrderCreate](../../models/ordercreate.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Order](../../models/order.md)**

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

**[str](../../models/.md)**

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
            "country": polar_sdk.AddressInputCountryAlpha2Input.US,
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

## finalize

Finalize a draft order and synchronously attempt an off-session charge.

On success, the order transitions to `paid` and benefit grants fire
before the response returns. On failure (decline, missing payment method,
SCA challenge), the order stays in `draft` and a 4xx error is returned.

The request fails with 412 if the order is not in `draft` status.

**Scopes**: `orders:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:finalize" method="post" path="/v1/orders/{id}/finalize" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.finalize(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `order_finalize`                                                    | [Optional[models.OrderFinalize]](../../models/orderfinalize.md)     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Order](../../models/order.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PaymentFailed                   | 402                                    | application/json                       |
| models.PaymentActionRequired           | 402                                    | application/json                       |
| models.OffSessionChargesNotEnabled     | 403                                    | application/json                       |
| models.OrganizationNotReadyForPayments | 403                                    | application/json                       |
| models.ResourceNotFound                | 404                                    | application/json                       |
| models.OrderNotDraft                   | 412                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

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
| models.ResourceNotFound             | 404                                 | application/json                    |
| models.OrderNotEligibleForInvoice   | 409                                 | application/json                    |
| models.MissingInvoiceBillingDetails | 422                                 | application/json                    |
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

## receipt

Get a presigned URL to download an order's receipt PDF.

**Scopes**: `orders:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="orders:receipt" method="get" path="/v1/orders/{id}/receipt" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.orders.receipt(id="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrderReceipt](../../models/orderreceipt.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |