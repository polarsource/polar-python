# ExternalOrganizations
(*external_organizations*)

## Overview

### Available Operations

* [list](#list) - List External Organizations

## list

List external organizations.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.external_organizations.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `platform`                                                                                                                                                              | [OptionalNullable[models.PlatformFilter]](../../models/platformfilter.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by platform.                                                                                                                                                     |
| `name`                                                                                                                                                                  | [OptionalNullable[models.RepositoryNameFilter]](../../models/repositorynamefilter.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by name.                                                                                                                                                         |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.ExternalOrganizationsListQueryParamOrganizationIDFilter]](../../models/externalorganizationslistqueryparamorganizationidfilter.md)             | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.ExternalOrganizationSortProperty](../../models/externalorganizationsortproperty.md)]                                                                       | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.ExternalOrganizationsListResponse](../../models/externalorganizationslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
