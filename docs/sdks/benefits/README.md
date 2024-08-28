# Benefits
(*benefits*)

## Overview

### Available Operations

* [list](#list) - List Benefits
* [create](#create) - Create Benefit
* [retrieve](#retrieve) - Get Benefit
* [delete](#delete) - Delete Benefit
* [update](#update) - Update Benefit
* [grants](#grants) - List Benefit Grants

## list

List benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.list(security=polar_sh.BenefitsListSecurity(
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

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                        | [models.BenefitsListSecurity](../../models/benefitslistsecurity.md)                                                               | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `organization_id`                                                                                                                 | [OptionalNullable[models.BenefitsListQueryParamOrganizationIDFilter]](../../models/benefitslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                | Filter by organization ID.                                                                                                        |
| `type`                                                                                                                            | [OptionalNullable[models.QueryParamBenefitTypeFilter]](../../models/queryparambenefittypefilter.md)                               | :heavy_minus_sign:                                                                                                                | Filter by benefit type.                                                                                                           |
| `page`                                                                                                                            | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Page number, defaults to 1.                                                                                                       |
| `limit`                                                                                                                           | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Size of a page, defaults to 10. Maximum is 100.                                                                                   |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.BenefitsListResponse](../../models/benefitslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.create(security=polar_sh.BenefitsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "description": "Multi-tiered motivating standardization",
    "properties": {
        "guild_token": "<value>",
        "role_id": "<value>",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.BenefitsCreateBenefitCreate](../../models/benefitscreatebenefitcreate.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `security`                                                                        | [models.BenefitsCreateSecurity](../../benefitscreatesecurity.md)                  | :heavy_check_mark:                                                                | The security requirements to use for the request.                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.BenefitsCreateResponseBenefitsCreate](../../models/benefitscreateresponsebenefitscreate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get a benefit by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.retrieve(security=polar_sh.BenefitsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.BenefitsGetSecurity](../../models/benefitsgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BenefitsGetResponseBenefitsGet](../../models/benefitsgetresponsebenefitsget.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## delete

Delete a benefit.

> [!WARNING]
> Every grants associated with the benefit will be revoked.
> Users will lose access to the benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.benefits.delete(security=polar_sh.BenefitsDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.BenefitsDeleteSecurity](../../models/benefitsdeletesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.update(security=polar_sh.BenefitsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.BenefitsUpdateSecurity](../../models/benefitsupdatesecurity.md)           | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `request_body`                                                                    | [models.BenefitsUpdateBenefitUpdate](../../models/benefitsupdatebenefitupdate.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.BenefitsUpdateResponseBenefitsUpdate](../../models/benefitsupdateresponsebenefitsupdate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## grants

List the individual grants for a benefit.

It's especially useful to check if a user has been granted a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.grants(security=polar_sh.BenefitsGrantsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "id": "<value>",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.BenefitsGrantsRequest](../../models/benefitsgrantsrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `security`                                                            | [models.BenefitsGrantsSecurity](../../benefitsgrantssecurity.md)      | :heavy_check_mark:                                                    | The security requirements to use for the request.                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.BenefitsGrantsResponse](../../models/benefitsgrantsresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
