# FundingSDK
(*funding*)

## Overview

### Available Operations

* [funding_search](#funding_search) - Search
* [funding_lookup](#funding_lookup) - Lookup

## funding_search

Search

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.funding.funding_search(security=polar_sh.FundingSearchSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "organization_id": "<value>",
    "repository_name": "my-repo",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FundingSearchRequest](../../models/fundingsearchrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.FundingSearchSecurity](../../fundingsearchsecurity.md)      | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceIssueFunding](../../models/listresourceissuefunding.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## funding_lookup

Lookup

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.funding.funding_lookup(security=polar_sh.FundingLookupSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), issue_id="31cc6ec0-0d59-40bd-ad99-a0d795bc1b6e")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.FundingLookupSecurity](../../models/fundinglookupsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `issue_id`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.IssueFunding](../../models/issuefunding.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
