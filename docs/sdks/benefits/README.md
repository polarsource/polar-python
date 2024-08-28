# Benefits
(*benefits*)

## Overview

### Available Operations

* [benefits_list](#benefits_list) - List Benefits
* [benefits_create](#benefits_create) - Create Benefit
* [benefits_get](#benefits_get) - Get Benefit
* [benefits_delete](#benefits_delete) - Delete Benefit
* [benefits_update](#benefits_update) - Update Benefit
* [benefits_list_grants](#benefits_list_grants) - List Benefit Grants

## benefits_list

List benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.benefits_list(security=polar_sh.BenefitsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

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

**[models.ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadables](../../models/listresourceunionbenefitarticlesbenefitadsbenefitcustombenefitdiscordbenefitgithubrepositorybenefitdownloadables.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## benefits_create

Create a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.benefits_create(security=polar_sh.BenefitsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "description": "Customer-focused client-driven groupware",
    "is_tax_applicable": False,
    "properties": {
        "note": "<value>",
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


## benefits_get

Get a benefit by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.benefits_get(security=polar_sh.BenefitsGetSecurity(
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


## benefits_delete

Delete a benefit.

> [!WARNING]
> Every grants associated with the benefit will be revoked.
> Users will lose access to the benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.benefits.benefits_delete(security=polar_sh.BenefitsDeleteSecurity(
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


## benefits_update

Update a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.benefits_update(security=polar_sh.BenefitsUpdateSecurity(
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


## benefits_list_grants

List the individual grants for a benefit.

It's especially useful to check if a user has been granted a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.benefits.benefits_list_grants(security=polar_sh.BenefitsListGrantsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.BenefitsListGrantsRequest](../../models/benefitslistgrantsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `security`                                                                    | [models.BenefitsListGrantsSecurity](../../benefitslistgrantssecurity.md)      | :heavy_check_mark:                                                            | The security requirements to use for the request.                             |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ListResourceBenefitGrant](../../models/listresourcebenefitgrant.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
