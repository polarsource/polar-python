# PolarBenefits
(*users.benefits*)

## Overview

### Available Operations

* [list](#list) - List Benefits
* [retrieve](#retrieve) - Get Benefit

## list

List my granted benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.benefits.list(security=polar_sh.UsersBenefitsListSecurity(
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

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.UsersBenefitsListRequest](../../models/usersbenefitslistrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `security`                                                                  | [models.UsersBenefitsListSecurity](../../usersbenefitslistsecurity.md)      | :heavy_check_mark:                                                          | The security requirements to use for the request.                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.UsersBenefitsListResponse](../../models/usersbenefitslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get a granted benefit by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.benefits.retrieve(security=polar_sh.UsersBenefitsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.UsersBenefitsGetSecurity](../../models/usersbenefitsgetsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The benefit ID.                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.UsersBenefitsGetResponseUsersBenefitsGet](../../models/usersbenefitsgetresponseusersbenefitsget.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
