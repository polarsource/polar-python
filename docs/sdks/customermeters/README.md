# CustomerMeters
(*customer_meters*)

## Overview

### Available Operations

* [list](#list) - List Customer Meters
* [get](#get) - Get Customer Meter

## list

List customer meters.

**Scopes**: `customer_meters:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_meters:list" method="get" path="/v1/customer-meters/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_meters.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CustomerMetersListQueryParamOrganizationIDFilter]](../../models/customermeterslistqueryparamorganizationidfilter.md)                           | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.CustomerMetersListQueryParamCustomerIDFilter]](../../models/customermeterslistqueryparamcustomeridfilter.md)                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.CustomerMetersListQueryParamExternalCustomerIDFilter]](../../models/customermeterslistqueryparamexternalcustomeridfilter.md)                   | :heavy_minus_sign:                                                                                                                                                      | Filter by external customer ID.                                                                                                                                         |
| `meter_id`                                                                                                                                                              | [OptionalNullable[models.QueryParamMeterIDFilter]](../../models/queryparammeteridfilter.md)                                                                             | :heavy_minus_sign:                                                                                                                                                      | Filter by meter ID.                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CustomerMeterSortProperty](../../models/customermetersortproperty.md)]                                                                                     | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomerMetersListResponse](../../models/customermeterslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a customer meter by ID.

**Scopes**: `customer_meters:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_meters:get" method="get" path="/v1/customer-meters/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_meters.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The customer meter ID.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerMeter](../../models/customermeter.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |