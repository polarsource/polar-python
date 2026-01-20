# MemberSessions
(*member_sessions*)

## Overview

### Available Operations

* [create](#create) - Create Member Session

## create

Create a member session.

This endpoint is only available for organizations with `member_model_enabled`
and `seat_based_pricing_enabled` feature flags enabled.

**Scopes**: `member_sessions:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="member-sessions:create" method="post" path="/v1/member-sessions/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.member_sessions.create(request={
        "member_id": "<value>",
        "return_url": "https://example.com/account",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MemberSessionCreate](../../models/membersessioncreate.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MemberSession](../../models/membersession.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |