# ExternalOrganizations
(*external_organizations*)

## Overview

### Available Operations

* [list](#list) - List External Organizations

## list

List external organizations.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.external_organizations.list(security=polar_sh.ExternalOrganizationsListSecurity(
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

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.ExternalOrganizationsListRequest](../../models/externalorganizationslistrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `security`                                                                                  | [models.ExternalOrganizationsListSecurity](../../externalorganizationslistsecurity.md)      | :heavy_check_mark:                                                                          | The security requirements to use for the request.                                           |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ExternalOrganizationsListResponse](../../models/externalorganizationslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
