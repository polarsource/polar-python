# IssueFundingSDK
(*issue_funding*)

## Overview

Endpoints related to issue funding and rewards in the Polar API.

### Available Operations

* [external_organizations_list](#external_organizations_list) - List External Organizations
* [repositories_list](#repositories_list) - List Repositories
* [repositories_get](#repositories_get) - Get Repository
* [repositories_update](#repositories_update) - Update Repository

## external_organizations_list

List external organizations.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issue_funding.external_organizations_list(security=polar_sh.ExternalOrganizationsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.ExternalOrganizationsListRequest](../../models/externalorganizationslistrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `security`                                                                                  | [models.ExternalOrganizationsListSecurity](../../externalorganizationslistsecurity.md)      | :heavy_check_mark:                                                                          | The security requirements to use for the request.                                           |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListResourceExternalOrganization](../../models/listresourceexternalorganization.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## repositories_list

List repositories.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issue_funding.repositories_list(security=polar_sh.RepositoriesListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.RepositoriesListRequest](../../models/repositorieslistrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `security`                                                                | [models.RepositoriesListSecurity](../../repositorieslistsecurity.md)      | :heavy_check_mark:                                                        | The security requirements to use for the request.                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ListResourceRepository](../../models/listresourcerepository.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## repositories_get

Get a repository by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issue_funding.repositories_get(security=polar_sh.RepositoriesGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.RepositoriesGetSecurity](../../models/repositoriesgetsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.RepositoryOutput](../../models/repositoryoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## repositories_update

Update a repository.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issue_funding.repositories_update(security=polar_sh.RepositoriesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", repository_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.RepositoriesUpdateSecurity](../../models/repositoriesupdatesecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `repository_update`                                                             | [models.RepositoryUpdate](../../models/repositoryupdate.md)                     | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.RepositoryOutput](../../models/repositoryoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
