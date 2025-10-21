# LicenseKeys
(*license_keys*)

## Overview

### Available Operations

* [list](#list) - List License Keys
* [get](#get) - Get License Key
* [update](#update) - Update License Key
* [get_activation](#get_activation) - Get Activation
* [validate](#validate) - Validate License Key
* [activate](#activate) - Activate License Key
* [deactivate](#deactivate) - Deactivate License Key

## list

Get license keys connected to the given organization & filters.

**Scopes**: `license_keys:read` `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:list" method="get" path="/v1/license-keys/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.Unauthorized                    | 401                                    | application/json                       |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get

Get a license key.

**Scopes**: `license_keys:read` `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:get" method="get" path="/v1/license-keys/{id}" -->
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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.Unauthorized                    | 401                                    | application/json                       |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update a license key.

**Scopes**: `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:update" method="patch" path="/v1/license-keys/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.update(id="<value>", license_key_update={})

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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.Unauthorized                    | 401                                    | application/json                       |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_activation

Get a license key activation.

**Scopes**: `license_keys:read` `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:get_activation" method="get" path="/v1/license-keys/{id}/activations/{activation_id}" -->
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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.Unauthorized                    | 401                                    | application/json                       |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## validate

Validate a license key.

**Scopes**: `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:validate" method="post" path="/v1/license-keys/validate" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.validate(request={
        "key": "<key>",
        "organization_id": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LicenseKeyValidate](../../models/licensekeyvalidate.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ValidatedLicenseKey](../../models/validatedlicensekey.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## activate

Activate a license key instance.

**Scopes**: `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:activate" method="post" path="/v1/license-keys/activate" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.license_keys.activate(request={
        "key": "<key>",
        "organization_id": "<value>",
        "label": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LicenseKeyActivate](../../models/licensekeyactivate.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LicenseKeyActivationRead](../../models/licensekeyactivationread.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsNotPermitted     | 403                                    | application/json                       |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## deactivate

Deactivate a license key instance.

**Scopes**: `license_keys:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="license_keys:deactivate" method="post" path="/v1/license-keys/deactivate" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.license_keys.deactivate(request={
        "key": "<key>",
        "organization_id": "<value>",
        "activation_id": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LicenseKeyDeactivate](../../models/licensekeydeactivate.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |