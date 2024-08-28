# PullRequests
(*pull_requests*)

## Overview

### Available Operations

* [pull_requests_search](#pull_requests_search) - Search pull requests

## pull_requests_search

Search pull requests.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.pull_requests.pull_requests_search(security=polar_sh.PullRequestsSearchSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.PullRequestsSearchSecurity](../../models/pullrequestssearchsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `references_issue_id`                                                           | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | Search pull requests that are mentioning this issue                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ListResourcePullRequest](../../models/listresourcepullrequest.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
