# Issues
(*issues*)

## Overview

### Available Operations

* [issues_list](#issues_list) - List Issues
* [issues_lookup](#issues_lookup) - Lookup
* [issues_get_body](#issues_get_body) - Get Body
* [issues_get](#issues_get) - Get issue
* [issues_update](#issues_update) - Update issue.
* [issues_confirm](#issues_confirm) - Mark an issue as confirmed solved.

## issues_list

List issues.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issues.issues_list(security=polar_sh.IssuesListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.IssuesListRequest](../../models/issueslistrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.IssuesListSecurity](../../issueslistsecurity.md)            | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceIssue](../../models/listresourceissue.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## issues_lookup

Lookup

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issues.issues_lookup(security=polar_sh.IssuesLookupSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), external_url="https://github.com/polarsource/polar/issues/897")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.IssuesLookupSecurity](../../models/issueslookupsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `external_url`                                                      | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | URL to issue on external source                                     | https://github.com/polarsource/polar/issues/897                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.IssueOutput](../../models/issueoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## issues_get_body

Get Body

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issues.issues_get_body(security=polar_sh.IssuesGetBodySecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="cc17566b-318d-4f5b-bef3-273c1681131a")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.IssuesGetBodySecurity](../../models/issuesgetbodysecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## issues_get

Get issue

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issues.issues_get(security=polar_sh.IssuesGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="761356d1-2aba-4ee6-bcf2-28e5e369cee3")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.IssuesGetSecurity](../../models/issuesgetsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IssueOutput](../../models/issueoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## issues_update

Update issue. Requires authentication.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issues.issues_update(security=polar_sh.IssuesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="55711a9c-39f6-48f8-afa2-a008ee1c6fb7", update_issue={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.IssuesUpdateSecurity](../../models/issuesupdatesecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `update_issue`                                                      | [models.UpdateIssue](../../models/updateissue.md)                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IssueOutput](../../models/issueoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## issues_confirm

Mark an issue as confirmed solved, and configure issue reward splits. Enables payouts of pledges. Can only be done once per issue. Requires authentication.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.issues.issues_confirm(security=polar_sh.IssuesConfirmSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="d77597b0-1d22-4c52-815a-449b1e4bf7ee", confirm_issue={
    "splits": [
        {
            "share_thousands": 116457,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.IssuesConfirmSecurity](../../models/issuesconfirmsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `confirm_issue`                                                       | [models.ConfirmIssue](../../models/confirmissue.md)                   | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.IssueOutput](../../models/issueoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
