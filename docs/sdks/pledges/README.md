# Pledges
(*pledges*)

## Overview

### Available Operations

* [pledges_search](#pledges_search) - Search pledges
* [pledges_summary](#pledges_summary) - Get pledges summary
* [pledges_spending](#pledges_spending) - Get user spending
* [pledges_get](#pledges_get) - Get pledge

## pledges_search

Search pledges. Requires authentication. The user can only read pledges that they have made (personally or via an organization) or received (to organizations that they are a member of).

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.pledges.pledges_search(security=polar_sh.PledgesSearchSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "repository_name": "my-repo",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PledgesSearchRequest](../../models/pledgessearchrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.PledgesSearchSecurity](../../pledgessearchsecurity.md)      | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourcePledge](../../models/listresourcepledge.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## pledges_summary

Get summary of pledges for resource.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.pledges.pledges_summary(security=polar_sh.PledgesSummarySecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), issue_id="d36bcfa5-77ef-4fab-9fc4-3223e9f462d7")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.PledgesSummarySecurity](../../models/pledgessummarysecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `issue_id`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.PledgePledgesSummary](../../models/pledgepledgessummary.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## pledges_spending

Get current user spending in the current period. Used together with spending limits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.pledges.pledges_spending(security=polar_sh.PledgesSpendingSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), organization_id="f5b079e3-c065-4014-8e07-c43211cf7d58")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.PledgesSpendingSecurity](../../models/pledgesspendingsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `organization_id`                                                         | *str*                                                                     | :heavy_check_mark:                                                        | Spending in this organization. Required.                                  |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.PledgeSpending](../../models/pledgespending.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## pledges_get

Get a pledge. Requires authentication.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.pledges.pledges_get(security=polar_sh.PledgesGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="2b2b40a4-cca1-4678-b830-ab47b57abccc")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.PledgesGetSecurity](../../models/pledgesgetsecurity.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PledgeOutput](../../models/pledgeoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
