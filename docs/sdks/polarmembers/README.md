# PolarMembers
(*customers.members*)

## Overview

### Available Operations

* [create](#create) - Create Member
* [create_external](#create_external) - Create Member by Customer External ID
* [get](#get) - Get Member
* [update](#update) - Update Member
* [delete](#delete) - Delete Member
* [get_external](#get_external) - Get Member by External ID
* [update_external](#update_external) - Update Member by External ID
* [delete_external](#delete_external) - Delete Member by External ID

## create

Create a new member for a customer.

Only B2B customers with the member management feature enabled can add members.
The authenticated user or organization must have access to the customer's organization.

**Scopes**: `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:create" method="post" path="/v1/customers/{id}/members" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.members.create(id="<value>", member_create_from_customer={
        "email": "member@example.com",
        "name": "Jane Doe",
        "external_id": "usr_1337",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The customer ID.                                                            |
| `member_create_from_customer`                                               | [models.MemberCreateFromCustomer](../../models/membercreatefromcustomer.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.Member](../../models/member.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_external

Create a new member for a customer identified by its external ID.

**Scopes**: `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:create_external" method="post" path="/v1/customers/external/{external_id}/members" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.members.create_external(external_id="<id>", member_create_from_customer={
        "email": "member@example.com",
        "name": "Jane Doe",
        "external_id": "usr_1337",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `external_id`                                                               | *str*                                                                       | :heavy_check_mark:                                                          | The customer external ID.                                                   |
| `member_create_from_customer`                                               | [models.MemberCreateFromCustomer](../../models/membercreatefromcustomer.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.Member](../../models/member.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.NotPermitted                | 403                                | application/json                   |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.AmbiguousExternalCustomerID | 409                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get

Get a member of a customer by its ID.

**Scopes**: `members:read` `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:get" method="get" path="/v1/customers/{id}/members/{member_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.members.get(id="<value>", member_id="a794a9c8-dc43-40b4-b2f5-ed16145e28ac")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `member_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Member](../../models/member.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a member of a customer.

Only name, email and role can be updated.

**Scopes**: `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:update" method="patch" path="/v1/customers/{id}/members/{member_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.members.update(id="<value>", member_id="f48ea05d-6a60-4bb1-b3d9-4b3cd7194f3a", member_update={
        "name": "Jane Doe",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `member_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `member_update`                                                     | [models.MemberUpdate](../../models/memberupdate.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Member](../../models/member.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a member of a customer.

**Scopes**: `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:delete" method="delete" path="/v1/customers/{id}/members/{member_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.customers.members.delete(id="<value>", member_id="a6d6f519-f76e-49a0-9868-b346c98100a6")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer ID.                                                    |
| `member_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_external

Get a member by external ID for a customer identified by its external ID.

**Scopes**: `members:read` `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:get_external" method="get" path="/v1/customers/external/{external_id}/members/{member_external_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.members.get_external(external_id="<id>", member_external_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The customer external ID.                                           |
| `member_external_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The member external ID.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Member](../../models/member.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.AmbiguousExternalCustomerID | 409                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## update_external

Update a member by external ID for a customer identified by its external ID.

**Scopes**: `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:update_external" method="patch" path="/v1/customers/external/{external_id}/members/{member_external_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customers.members.update_external(external_id="<id>", member_external_id="<id>", member_update={
        "name": "Jane Doe",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The customer external ID.                                           |
| `member_external_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The member external ID.                                             |
| `member_update`                                                     | [models.MemberUpdate](../../models/memberupdate.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Member](../../models/member.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.AmbiguousExternalCustomerID | 409                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## delete_external

Delete a member by external ID for a customer identified by its external ID.

**Scopes**: `members:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customers:members:delete_external" method="delete" path="/v1/customers/external/{external_id}/members/{member_external_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.customers.members.delete_external(external_id="<id>", member_external_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The customer external ID.                                           |
| `member_external_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The member external ID.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.AmbiguousExternalCustomerID | 409                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |