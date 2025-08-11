# PolarCustomers
(*customer_portal.customers*)

## Overview

### Available Operations

* [get](#get) - Get Customer
* [update](#update) - Update Customer
* [list_payment_methods](#list_payment_methods) - List Customer Payment Methods
* [add_payment_method](#add_payment_method) - Add Customer Payment Method
* [delete_payment_method](#delete_payment_method) - Delete Customer Payment Method

## get

Get authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:customers:get" method="get" path="/v1/customer-portal/customers/me" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.customers.get(security=polar_sdk.CustomerPortalCustomersGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [models.CustomerPortalCustomersGetSecurity](../../customerportalcustomersgetsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[models.CustomerPortalCustomer](../../models/customerportalcustomer.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update authenticated customer.

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:customers:update" method="patch" path="/v1/customer-portal/customers/me" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.customers.update(security=polar_sdk.CustomerPortalCustomersUpdateSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), request={
        "billing_address": {
            "country": "US",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [models.CustomerPortalCustomerUpdate](../../models/customerportalcustomerupdate.md)            | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [models.CustomerPortalCustomersUpdateSecurity](../../customerportalcustomersupdatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.CustomerPortalCustomer](../../models/customerportalcustomer.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_payment_methods

Get saved payment methods of the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:customers:list_payment_methods" method="get" path="/v1/customer-portal/customers/me/payment-methods" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.customers.list_payment_methods(security=polar_sdk.CustomerPortalCustomersListPaymentMethodsSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                    | [models.CustomerPortalCustomersListPaymentMethodsSecurity](../../models/customerportalcustomerslistpaymentmethodssecurity.md) | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `page`                                                                                                                        | *Optional[int]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Page number, defaults to 1.                                                                                                   |
| `limit`                                                                                                                       | *Optional[int]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Size of a page, defaults to 10. Maximum is 100.                                                                               |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.CustomerPortalCustomersListPaymentMethodsResponse](../../models/customerportalcustomerslistpaymentmethodsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## add_payment_method

Add a payment method to the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:customers:add_payment_method" method="post" path="/v1/customer-portal/customers/me/payment-methods" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.customers.add_payment_method(security=polar_sdk.CustomerPortalCustomersAddPaymentMethodSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), request={
        "confirmation_token_id": "<id>",
        "set_default": False,
        "return_url": "https://yearly-custom.net/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [models.CustomerPaymentMethodCreate](../../models/customerpaymentmethodcreate.md)                                  | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [models.CustomerPortalCustomersAddPaymentMethodSecurity](../../customerportalcustomersaddpaymentmethodsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.CustomerPaymentMethod](../../models/customerpaymentmethod.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_payment_method

Delete a payment method from the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:customers:delete_payment_method" method="delete" path="/v1/customer-portal/customers/me/payment-methods/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    polar.customer_portal.customers.delete_payment_method(security=polar_sdk.CustomerPortalCustomersDeletePaymentMethodSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                      | [models.CustomerPortalCustomersDeletePaymentMethodSecurity](../../models/customerportalcustomersdeletepaymentmethodsecurity.md) | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `id`                                                                                                                            | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |