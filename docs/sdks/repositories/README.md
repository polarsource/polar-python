# Repositories
(*repositories*)

## Overview

### Available Operations

* [list](#list) - List Repositories
* [retrieve](#retrieve) - Get Repository
* [update](#update) - Update Repository

## list

List repositories.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.repositories.list(security=polar_sh.RepositoriesListSecurity(
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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.RepositoriesListRequest](../../models/repositorieslistrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `security`                                                                | [models.RepositoriesListSecurity](../../repositorieslistsecurity.md)      | :heavy_check_mark:                                                        | The security requirements to use for the request.                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.RepositoriesListResponse](../../models/repositorieslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get a repository by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.repositories.retrieve(security=polar_sh.RepositoriesGetSecurity(
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


## update

Update a repository.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.repositories.update(security=polar_sh.RepositoriesUpdateSecurity(
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
