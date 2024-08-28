# Organizations
(*organizations*)

## Overview

### Available Operations

* [list](#list) - List Organizations
* [create](#create) - Create Organization
* [retrieve](#retrieve) - Get Organization
* [update](#update) - Update Organization
* [organizations_list_organization_customers](#organizations_list_organization_customers) - List Organization Customers

## list

List organizations.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.organizations.list(security=polar_sh.OrganizationsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.OrganizationsListRequest](../../models/organizationslistrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `security`                                                                  | [models.OrganizationsListSecurity](../../organizationslistsecurity.md)      | :heavy_check_mark:                                                          | The security requirements to use for the request.                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.OrganizationsListResponse](../../models/organizationslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create an organization.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.organizations.create(security=polar_sh.OrganizationsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "name": "<value>",
    "slug": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [models.OrganizationCreate](../../models/organizationcreate.md)            | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [models.OrganizationsCreateSecurity](../../organizationscreatesecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.OrganizationOutput](../../models/organizationoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get an organization by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.organizations.retrieve(security=polar_sh.OrganizationsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.OrganizationsGetSecurity](../../models/organizationsgetsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.OrganizationOutput](../../models/organizationoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update an organization.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.organizations.update(security=polar_sh.OrganizationsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", organization_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.OrganizationsUpdateSecurity](../../models/organizationsupdatesecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `organization_update`                                                             | [models.OrganizationUpdate](../../models/organizationupdate.md)                   | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.OrganizationOutput](../../models/organizationoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## organizations_list_organization_customers

List organization customers.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.organizations.organizations_list_organization_customers(security=polar_sh.OrganizationsListOrganizationCustomersSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                              | [models.OrganizationsListOrganizationCustomersSecurity](../../models/organizationslistorganizationcustomerssecurity.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `id`                                                                                                                    | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `customer_types`                                                                                                        | List[[models.OrganizationCustomerType](../../models/organizationcustomertype.md)]                                       | :heavy_minus_sign:                                                                                                      | Filter by the type of purchase the customer made.                                                                       |
| `page`                                                                                                                  | *Optional[int]*                                                                                                         | :heavy_minus_sign:                                                                                                      | Page number, defaults to 1.                                                                                             |
| `limit`                                                                                                                 | *Optional[int]*                                                                                                         | :heavy_minus_sign:                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                         |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.OrganizationsListOrganizationCustomersResponse](../../models/organizationslistorganizationcustomersresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
