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

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.list(page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                       | [OptionalNullable[models.LicenseKeysListQueryParamOrganizationIDFilter]](../../models/licensekeyslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                      | Filter by organization ID.                                                                                                              |
| `benefit_id`                                                                                                                            | [OptionalNullable[models.QueryParamBenefitIDFilter]](../../models/queryparambenefitidfilter.md)                                         | :heavy_minus_sign:                                                                                                                      | Filter by benefit ID.                                                                                                                   |
| `page`                                                                                                                                  | *Optional[int]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Page number, defaults to 1.                                                                                                             |
| `limit`                                                                                                                                 | *Optional[int]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                         |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.LicenseKeysListResponse](../../models/licensekeyslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a license key.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LicenseKeyWithActivations](../../models/licensekeywithactivations.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a license key.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.update(id="<value>", license_key_update={
        "usage": 0,
    })

    # Handle response
    print(res)

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_activation

Get a license key activation.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.get_activation(id="<value>", activation_id="<value>")

    # Handle response
    print(res)

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |