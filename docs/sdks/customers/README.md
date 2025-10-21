# Customers
(*customers*)

## Overview

### Available Operations

* [list](#list) - List Customers
* [create](#create) - Create Customer
* [export](#export) - Export Customers
* [get](#get) - Get Customer
* [update](#update) - Update Customer
* [delete](#delete) - Delete Customer
* [get_external](#get_external) - Get Customer by External ID
* [update_external](#update_external) - Update Customer by External ID
* [delete_external](#delete_external) - Delete Customer by External ID
* [get_state](#get_state) - Get Customer State
* [get_state_external](#get_state_external) - Get Customer State by External ID
* [get_balance](#get_balance) - Get Customer Balance

## list

List customers.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:list" method="get" path="/v1/customers/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CustomersListQueryParamOrganizationIDFilter]](../../models/customerslistqueryparamorganizationidfilter.md)                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `email`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by exact email.                                                                                                                                                  |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by name, email, or external ID.                                                                                                                                  |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CustomerSortProperty](../../models/customersortproperty.md)]                                                                                               | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `metadata`                                                                                                                                                              | Dict[str, [models.MetadataQuery](../../models/metadataquery.md)]                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`.                                                                        |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomersListResponse](../../models/customerslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a customer.

**Scopes**: `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:create" method="post" path="/v1/customers/" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.create(request={
        "external_id": "usr_1337",
        "email": "customer@example.com",
        "name": "John Doe",
        "billing_address": {
            "country": polar_sdk.CountryAlpha2Input.US,
        },
        "tax_id": [
            "911144442",
            "us_ein",
        ],
        "organization_id": "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CustomerCreate](../../models/customercreate.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Customer](../../models/customer.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## export

Export customers as a CSV file.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:export" method="get" path="/v1/customers/export" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.export(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                           | [OptionalNullable[models.CustomersExportQueryParamOrganizationID]](../../models/customersexportqueryparamorganizationid.md) | :heavy_minus_sign:                                                                                                          | Filter by organization ID.                                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a customer by ID.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:get" method="get" path="/v1/customers/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Customer](../../models/customer.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update a customer.

**Scopes**: `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:update" method="patch" path="/v1/customers/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.update(id="<value>", customer_update={
        "email": "customer@example.com",
        "name": "John Doe",
        "billing_address": {
            "country": polar_sdk.CountryAlpha2Input.US,
        },
        "tax_id": [
            "911144442",
            "us_ein",
        ],
        "external_id": "usr_1337",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `customer_update`                                                   | [models.CustomerUpdate](../../models/customerupdate.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Customer](../../models/customer.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a customer.

This action cannot be undone and will immediately:
- Cancel any active subscriptions for the customer
- Revoke all their benefits
- Clear any `external_id`

Use it only in the context of deleting a user within your
own service. Otherwise, use more granular API endpoints to cancel
a specific subscription or revoke certain benefits.

Note: The customers information will nonetheless be retained for historic
orders and subscriptions.

**Scopes**: `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:delete" method="delete" path="/v1/customers/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.customers.delete(id="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_external

Get a customer by external ID.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:get_external" method="get" path="/v1/customers/external/{external_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.get_external(external_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The customer external ID.                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Customer](../../models/customer.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## update_external

Update a customer by external ID.

**Scopes**: `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:update_external" method="patch" path="/v1/customers/external/{external_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.update_external(external_id="<id>", customer_update_external_id={
        "email": "customer@example.com",
        "name": "John Doe",
        "billing_address": None,
        "tax_id": [
            "911144442",
            "us_ein",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `external_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | The customer external ID.                                                   |
| `customer_update_external_id`                                               | [models.CustomerUpdateExternalID](../../models/customerupdateexternalid.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.Customer](../../models/customer.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## delete_external

Delete a customer by external ID.

Immediately cancels any active subscriptions and revokes any active benefits.

**Scopes**: `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:delete_external" method="delete" path="/v1/customers/external/{external_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.customers.delete_external(external_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The customer external ID.                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_state

Get a customer state by ID.

The customer state includes information about
the customer's active subscriptions and benefits.

It's the ideal endpoint to use when you need to get a full overview
of a customer's status.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:get_state" method="get" path="/v1/customers/{id}/state" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.get_state(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerState](../../models/customerstate.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_state_external

Get a customer state by external ID.

The customer state includes information about
the customer's active subscriptions and benefits.

It's the ideal endpoint to use when you need to get a full overview
of a customer's status.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:get_state_external" method="get" path="/v1/customers/external/{external_id}/state" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.get_state_external(external_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The customer external ID.                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerState](../../models/customerstate.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_balance

Get customer balance information.

**Scopes**: `customers:read` `customers:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:get_balance" method="get" path="/v1/customers/{id}/balance" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.get_balance(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerBalance](../../models/customerbalance.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |