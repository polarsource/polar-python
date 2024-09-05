# Downloadables
(*users.downloadables*)

## Overview

### Available Operations

* [list](#list) - List Downloadables
* [get](#get) - Get Downloadable

## list

List Downloadables

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.downloadables.list()

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                     | [OptionalNullable[models.UsersDownloadablesListQueryParamOrganizationIDFilter]](../../models/usersdownloadableslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                    | Filter by organization ID.                                                                                                                            |
| `benefit_id`                                                                                                                                          | [OptionalNullable[models.BenefitIDFilter]](../../models/benefitidfilter.md)                                                                           | :heavy_minus_sign:                                                                                                                                    | Filter by given benefit ID.                                                                                                                           |
| `page`                                                                                                                                                | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Page number, defaults to 1.                                                                                                                           |
| `limit`                                                                                                                                               | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Size of a page, defaults to 10. Maximum is 100.                                                                                                       |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.UsersDownloadablesListResponse](../../models/usersdownloadableslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## get

Get Downloadable

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.downloadables.get(token="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
