# LicenseKeys
(*license_keys*)

## Overview

### Available Operations

* [list](#list) - List License Keys
* [get](#get) - Get License Key
* [update](#update) - Update License Key
* [get_activation](#get_activation) - Get Activation

## list

Get license keys connected to the given organization & filters.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.license_keys.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                       | [OptionalNullable[models.LicenseKeysListQueryParamOrganizationIDFilter]](../../models/licensekeyslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                      | Filter by organization ID.                                                                                                              |
| `page`                                                                                                                                  | *Optional[int]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Page number, defaults to 1.                                                                                                             |
| `limit`                                                                                                                                 | *Optional[int]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                         |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.LicenseKeysListResponse](../../models/licensekeyslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## get

Get a license key.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.license_keys.get(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LicenseKeyWithActivations](../../models/licensekeywithactivations.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update a license key.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.license_keys.update(id="<value>", license_key_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `license_key_update`                                                | [models.LicenseKeyUpdate](../../models/licensekeyupdate.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LicenseKeyRead](../../models/licensekeyread.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## get_activation

Get a license key activation.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.license_keys.get_activation(id="<value>", activation_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `activation_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LicenseKeyActivationRead](../../models/licensekeyactivationread.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
