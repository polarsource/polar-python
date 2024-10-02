# PolarLicenseKeys
(*users.license_keys*)

## Overview

### Available Operations

* [list](#list) - List License Keys
* [get](#get) - Get License Key
* [validate](#validate) - Validate License Key
* [activate](#activate) - Activate License Key
* [deactivate](#deactivate) - Deactivate License Key

## list

List License Keys

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.license_keys.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                 | [OptionalNullable[models.UsersLicenseKeysListQueryParamOrganizationIDFilter]](../../models/userslicensekeyslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                | Filter by organization ID.                                                                                                                        |
| `benefit_id`                                                                                                                                      | *OptionalNullable[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                                | Filter by a specific benefit                                                                                                                      |
| `page`                                                                                                                                            | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Page number, defaults to 1.                                                                                                                       |
| `limit`                                                                                                                                           | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Size of a page, defaults to 10. Maximum is 100.                                                                                                   |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.UsersLicenseKeysListResponse](../../models/userslicensekeyslistresponse.md)**

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

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.license_keys.get(id="<value>")

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## validate

Validate a license key.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.license_keys.validate(request={
    "key": "<key>",
    "organization_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LicenseKeyValidate](../../models/licensekeyvalidate.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ValidatedLicenseKey](../../models/validatedlicensekey.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## activate

Activate a license key instance.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.users.license_keys.activate(request={
    "key": "<key>",
    "organization_id": "<value>",
    "label": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LicenseKeyActivate](../../models/licensekeyactivate.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LicenseKeyActivationRead](../../models/licensekeyactivationread.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## deactivate

Deactivate a license key instance.

### Example Usage

```python
from polar_sdk import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)

s.users.license_keys.deactivate(request={
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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |