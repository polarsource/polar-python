# Benefits
(*benefits*)

## Overview

### Available Operations

* [list](#list) - List Benefits
* [create](#create) - Create Benefit
* [get](#get) - Get Benefit
* [update](#update) - Update Benefit
* [delete](#delete) - Delete Benefit
* [grants](#grants) - List Benefit Grants

## list

List benefits.

**Scopes**: `benefits:read` `benefits:write`

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.benefits.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                 | [OptionalNullable[models.BenefitsListQueryParamOrganizationIDFilter]](../../models/benefitslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                | Filter by organization ID.                                                                                                        |
| `type_filter`                                                                                                                     | [OptionalNullable[models.BenefitTypeFilter]](../../models/benefittypefilter.md)                                                   | :heavy_minus_sign:                                                                                                                | Filter by benefit type.                                                                                                           |
| `page`                                                                                                                            | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Page number, defaults to 1.                                                                                                       |
| `limit`                                                                                                                           | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Size of a page, defaults to 10. Maximum is 100.                                                                                   |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.BenefitsListResponse](../../models/benefitslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a benefit.

**Scopes**: `benefits:write`

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.benefits.create(request={
        "description": "delightfully fumigate convection though zowie up bulky electronics",
        "properties": {
            "guild_token": "<value>",
            "role_id": "<id>",
        },
        "type": "discord",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BenefitCreate](../../models/benefitcreate.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Benefit](../../models/benefit.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a benefit by ID.

**Scopes**: `benefits:read` `benefits:write`

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.benefits.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Benefit](../../models/benefit.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a benefit.

**Scopes**: `benefits:write`

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.benefits.update(id="<value>", request_body={
        "type": "license_keys",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `request_body`                                                                    | [models.BenefitsUpdateBenefitUpdate](../../models/benefitsupdatebenefitupdate.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Benefit](../../models/benefit.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a benefit.

> [!WARNING]
> Every grants associated with the benefit will be revoked.
> Users will lose access to the benefit.

**Scopes**: `benefits:write`

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.benefits.delete(id="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## grants

List the individual grants for a benefit.

It's especially useful to check if a user has been granted a benefit.

**Scopes**: `benefits:read` `benefits:write`

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.benefits.grants(id="<value>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                              | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `is_granted`                                                                                                                      | *OptionalNullable[bool]*                                                                                                          | :heavy_minus_sign:                                                                                                                | Filter by granted status. If `true`, only granted benefits will be returned. If `false`, only revoked benefits will be returned.  |
| `customer_id`                                                                                                                     | [OptionalNullable[models.QueryParamCustomerIDFilter]](../../models/queryparamcustomeridfilter.md)                                 | :heavy_minus_sign:                                                                                                                | Filter by customer.                                                                                                               |
| `page`                                                                                                                            | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Page number, defaults to 1.                                                                                                       |
| `limit`                                                                                                                           | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Size of a page, defaults to 10. Maximum is 100.                                                                                   |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.BenefitsGrantsResponse](../../models/benefitsgrantsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |