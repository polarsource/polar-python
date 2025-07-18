# Downloadables
(*customer_portal.downloadables*)

## Overview

### Available Operations

* [list](#list) - List Downloadables

## list

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.downloadables.list(security=polar_sdk.CustomerPortalDownloadablesListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.CustomerPortalDownloadablesListSecurity](../../models/customerportaldownloadableslistsecurity.md)                                                               | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CustomerPortalDownloadablesListQueryParamOrganizationIDFilter]](../../models/customerportaldownloadableslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `benefit_id`                                                                                                                                                            | [OptionalNullable[models.CustomerPortalDownloadablesListQueryParamBenefitIDFilter]](../../models/customerportaldownloadableslistqueryparambenefitidfilter.md)           | :heavy_minus_sign:                                                                                                                                                      | Filter by benefit ID.                                                                                                                                                   |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomerPortalDownloadablesListResponse](../../models/customerportaldownloadableslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |