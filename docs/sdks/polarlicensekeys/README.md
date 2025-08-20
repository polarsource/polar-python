# PolarLicenseKeys
(*customer_portal.license_keys*)

## Overview

### Available Operations

* [list](#list) - List License Keys
* [get](#get) - Get License Key
* [validate](#validate) - Validate License Key
* [activate](#activate) - Activate License Key
* [deactivate](#deactivate) - Deactivate License Key

## list

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:license_keys:list" method="get" path="/v1/customer-portal/license-keys/" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.license_keys.list(security=polar_sdk.CustomerPortalLicenseKeysListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                           | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                          | [models.CustomerPortalLicenseKeysListSecurity](../../models/customerportallicensekeyslistsecurity.md)                                                               | :heavy_check_mark:                                                                                                                                                  | N/A                                                                                                                                                                 |
| `organization_id`                                                                                                                                                   | [OptionalNullable[models.CustomerPortalLicenseKeysListQueryParamOrganizationIDFilter]](../../models/customerportallicensekeyslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                                  | Filter by organization ID.                                                                                                                                          |
| `benefit_id`                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                  | Filter by a specific benefit                                                                                                                                        |
| `page`                                                                                                                                                              | *Optional[int]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Page number, defaults to 1.                                                                                                                                         |
| `limit`                                                                                                                                                             | *Optional[int]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Size of a page, defaults to 10. Maximum is 100.                                                                                                                     |
| `retries`                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                 |

### Response

**[models.CustomerPortalLicenseKeysListResponse](../../models/customerportallicensekeyslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.Unauthorized        | 401                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a license key.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:license_keys:get" method="get" path="/v1/customer-portal/license-keys/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.license_keys.get(security=polar_sdk.CustomerPortalLicenseKeysGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.CustomerPortalLicenseKeysGetSecurity](../../models/customerportallicensekeysgetsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `id`                                                                                                | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.LicenseKeyWithActivations](../../models/licensekeywithactivations.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## validate

Validate a license key.

> This endpoint doesn't require authentication and can be safely used on a public
> client, like a desktop application or a mobile app.
> If you plan to validate a license key on a server, use the `/v1/license-keys/validate`
> endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:license_keys:validate" method="post" path="/v1/customer-portal/license-keys/validate" -->
```python
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.license_keys.validate(request={
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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## activate

Activate a license key instance.

> This endpoint doesn't require authentication and can be safely used on a public
> client, like a desktop application or a mobile app.
> If you plan to validate a license key on a server, use the `/v1/license-keys/activate`
> endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:license_keys:activate" method="post" path="/v1/customer-portal/license-keys/activate" -->
```python
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.license_keys.activate(request={
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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## deactivate

Deactivate a license key instance.

> This endpoint doesn't require authentication and can be safely used on a public
> client, like a desktop application or a mobile app.
> If you plan to validate a license key on a server, use the `/v1/license-keys/deactivate`
> endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:license_keys:deactivate" method="post" path="/v1/customer-portal/license-keys/deactivate" -->
```python
from polar_sdk import Polar


with Polar() as polar:

    polar.customer_portal.license_keys.deactivate(request={
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