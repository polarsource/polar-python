# BenefitGrants
(*benefit_grants*)

## Overview

### Available Operations

* [list](#list) - List Benefit Grants

## list

List benefit grants across all benefits for the authenticated organization.

**Scopes**: `benefits:read` `benefits:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="benefit-grants:list" method="get" path="/v1/benefit-grants/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.benefit_grants.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.BenefitGrantsListQueryParamOrganizationIDFilter]](../../models/benefitgrantslistqueryparamorganizationidfilter.md)                             | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.BenefitGrantsListQueryParamCustomerIDFilter]](../../models/benefitgrantslistqueryparamcustomeridfilter.md)                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.QueryParamExternalCustomerIDFilter]](../../models/queryparamexternalcustomeridfilter.md)                                                       | :heavy_minus_sign:                                                                                                                                                      | Filter by customer external ID.                                                                                                                                         |
| `is_granted`                                                                                                                                                            | *OptionalNullable[bool]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                      | Filter by granted status. If `true`, only granted benefits will be returned. If `false`, only revoked benefits will be returned.                                        |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.BenefitGrantSortProperty](../../models/benefitgrantsortproperty.md)]                                                                                       | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.BenefitGrantsListResponse](../../models/benefitgrantslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |