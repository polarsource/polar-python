# PolarOrders
(*customer_portal.orders*)

## Overview

### Available Operations

* [list](#list) - List Orders
* [get](#get) - Get Order
* [update](#update) - Update Order
* [generate_invoice](#generate_invoice) - Generate Order Invoice
* [invoice](#invoice) - Get Order Invoice
* [get_payment_status](#get_payment_status) - Get Order Payment Status
* [confirm_retry_payment](#confirm_retry_payment) - Confirm Retry Payment

## list

List orders of the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:list" method="get" path="/v1/customer-portal/orders/" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.list(security=polar_sdk.CustomerPortalOrdersListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                           | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                          | [models.CustomerPortalOrdersListSecurity](../../models/customerportalorderslistsecurity.md)                                                                                         | :heavy_check_mark:                                                                                                                                                                  | N/A                                                                                                                                                                                 |
| `organization_id`                                                                                                                                                                   | [OptionalNullable[models.CustomerPortalOrdersListQueryParamOrganizationIDFilter]](../../models/customerportalorderslistqueryparamorganizationidfilter.md)                           | :heavy_minus_sign:                                                                                                                                                                  | Filter by organization ID.                                                                                                                                                          |
| `product_id`                                                                                                                                                                        | [OptionalNullable[models.CustomerPortalOrdersListQueryParamProductIDFilter]](../../models/customerportalorderslistqueryparamproductidfilter.md)                                     | :heavy_minus_sign:                                                                                                                                                                  | Filter by product ID.                                                                                                                                                               |
| `product_billing_type`                                                                                                                                                              | [OptionalNullable[models.CustomerPortalOrdersListQueryParamProductBillingTypeFilter]](../../models/customerportalorderslistqueryparamproductbillingtypefilter.md)                   | :heavy_minus_sign:                                                                                                                                                                  | Filter by product billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases. |
| `subscription_id`                                                                                                                                                                   | [OptionalNullable[models.CustomerPortalOrdersListQueryParamSubscriptionIDFilter]](../../models/customerportalorderslistqueryparamsubscriptionidfilter.md)                           | :heavy_minus_sign:                                                                                                                                                                  | Filter by subscription ID.                                                                                                                                                          |
| `query`                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                  | Search by product or organization name.                                                                                                                                             |
| `page`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | Page number, defaults to 1.                                                                                                                                                         |
| `limit`                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                  | Size of a page, defaults to 10. Maximum is 100.                                                                                                                                     |
| `sorting`                                                                                                                                                                           | List[[models.CustomerOrderSortProperty](../../models/customerordersortproperty.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                                  | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order.             |
| `retries`                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                 |

### Response

**[models.CustomerPortalOrdersListResponse](../../models/customerportalorderslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get an order by ID for the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:get" method="get" path="/v1/customer-portal/orders/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.get(security=polar_sdk.CustomerPortalOrdersGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.CustomerPortalOrdersGetSecurity](../../models/customerportalordersgetsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `id`                                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | The order ID.                                                                             |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.CustomerOrder](../../models/customerorder.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an order for the authenticated customer.

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:update" method="patch" path="/v1/customer-portal/orders/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.update(security=polar_sdk.CustomerPortalOrdersUpdateSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>", customer_order_update={
        "billing_name": "<value>",
        "billing_address": {
            "country": polar_sdk.CountryAlpha2Input.US,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.CustomerPortalOrdersUpdateSecurity](../../models/customerportalordersupdatesecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `id`                                                                                            | *str*                                                                                           | :heavy_check_mark:                                                                              | The order ID.                                                                                   |
| `customer_order_update`                                                                         | [models.CustomerOrderUpdate](../../models/customerorderupdate.md)                               | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CustomerOrder](../../models/customerorder.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## generate_invoice

Trigger generation of an order's invoice.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:generate_invoice" method="post" path="/v1/customer-portal/orders/{id}/invoice" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.generate_invoice(security=polar_sdk.CustomerPortalOrdersGenerateInvoiceSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.CustomerPortalOrdersGenerateInvoiceSecurity](../../models/customerportalordersgenerateinvoicesecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `id`                                                                                                              | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The order ID.                                                                                                     |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

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

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:invoice" method="get" path="/v1/customer-portal/orders/{id}/invoice" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.invoice(security=polar_sdk.CustomerPortalOrdersInvoiceSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.CustomerPortalOrdersInvoiceSecurity](../../models/customerportalordersinvoicesecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `id`                                                                                              | *str*                                                                                             | :heavy_check_mark:                                                                                | The order ID.                                                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.CustomerOrderInvoice](../../models/customerorderinvoice.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_payment_status

Get the current payment status for an order.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:get_payment_status" method="get" path="/v1/customer-portal/orders/{id}/payment-status" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.get_payment_status(security=polar_sdk.CustomerPortalOrdersGetPaymentStatusSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                          | [models.CustomerPortalOrdersGetPaymentStatusSecurity](../../models/customerportalordersgetpaymentstatussecurity.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `id`                                                                                                                | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The order ID.                                                                                                       |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.CustomerOrderPaymentStatus](../../models/customerorderpaymentstatus.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## confirm_retry_payment

Confirm a retry payment using a Stripe confirmation token.

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:orders:confirm_retry_payment" method="post" path="/v1/customer-portal/orders/{id}/confirm-payment" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.orders.confirm_retry_payment(security=polar_sdk.CustomerPortalOrdersConfirmRetryPaymentSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>", customer_order_confirm_payment={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                | [models.CustomerPortalOrdersConfirmRetryPaymentSecurity](../../models/customerportalordersconfirmretrypaymentsecurity.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `id`                                                                                                                      | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The order ID.                                                                                                             |
| `customer_order_confirm_payment`                                                                                          | [models.CustomerOrderConfirmPayment](../../models/customerorderconfirmpayment.md)                                         | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.CustomerOrderPaymentConfirmation](../../models/customerorderpaymentconfirmation.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ResourceNotFound         | 404                             | application/json                |
| models.PaymentAlreadyInProgress | 409                             | application/json                |
| models.OrderNotEligibleForRetry | 422                             | application/json                |
| models.SDKError                 | 4XX, 5XX                        | \*/\*                           |