# BenefitGrants
(*customer_portal.benefit_grants*)

## Overview

### Available Operations

* [list](#list) - List Benefit Grants
* [get](#get) - Get Benefit Grant
* [update](#update) - Update Benefit Grant

## list

List benefits grants of the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.benefit_grants.list(security=polar_sdk.CustomerPortalBenefitGrantsListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id=[
        "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
    ])

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.CustomerPortalBenefitGrantsListSecurity](../../models/customerportalbenefitgrantslistsecurity.md)                                                               | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `type_filter`                                                                                                                                                           | [OptionalNullable[models.QueryParamBenefitTypeFilter]](../../models/queryparambenefittypefilter.md)                                                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by benefit type.                                                                                                                                                 |
| `benefit_id`                                                                                                                                                            | [OptionalNullable[models.CustomerPortalBenefitGrantsListQueryParamBenefitIDFilter]](../../models/customerportalbenefitgrantslistqueryparambenefitidfilter.md)           | :heavy_minus_sign:                                                                                                                                                      | Filter by benefit ID.                                                                                                                                                   |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CustomerPortalBenefitGrantsListQueryParamOrganizationIDFilter]](../../models/customerportalbenefitgrantslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `checkout_id`                                                                                                                                                           | [OptionalNullable[models.QueryParamCheckoutIDFilter]](../../models/queryparamcheckoutidfilter.md)                                                                       | :heavy_minus_sign:                                                                                                                                                      | Filter by checkout ID.                                                                                                                                                  |
| `order_id`                                                                                                                                                              | [OptionalNullable[models.QueryParamOrderIDFilter]](../../models/queryparamorderidfilter.md)                                                                             | :heavy_minus_sign:                                                                                                                                                      | Filter by order ID.                                                                                                                                                     |
| `subscription_id`                                                                                                                                                       | [OptionalNullable[models.QueryParamSubscriptionIDFilter]](../../models/queryparamsubscriptionidfilter.md)                                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by subscription ID.                                                                                                                                              |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CustomerBenefitGrantSortProperty](../../models/customerbenefitgrantsortproperty.md)]                                                                       | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomerPortalBenefitGrantsListResponse](../../models/customerportalbenefitgrantslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a benefit grant by ID for the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.benefit_grants.get(security=polar_sdk.CustomerPortalBenefitGrantsGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.CustomerPortalBenefitGrantsGetSecurity](../../models/customerportalbenefitgrantsgetsecurity.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `id`                                                                                                    | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The benefit grant ID.                                                                                   |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.CustomerBenefitGrant](../../models/customerbenefitgrant.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a benefit grant for the authenticated customer.

**Scopes**: `customer_portal:write`

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.benefit_grants.update(security=polar_sdk.CustomerPortalBenefitGrantsUpdateSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>", customer_benefit_grant_update={
        "benefit_type": "license_keys",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                    | [models.CustomerPortalBenefitGrantsUpdateSecurity](../../models/customerportalbenefitgrantsupdatesecurity.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `id`                                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The benefit grant ID.                                                                                         |
| `customer_benefit_grant_update`                                                                               | [models.CustomerBenefitGrantUpdate](../../models/customerbenefitgrantupdate.md)                               | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CustomerBenefitGrant](../../models/customerbenefitgrant.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |