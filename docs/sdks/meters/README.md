# Meters
(*meters*)

## Overview

### Available Operations

* [list](#list) - List Meters
* [create](#create) - Create Meter
* [get](#get) - Get Meter
* [update](#update) - Update Meter
* [quantities](#quantities) - Get Meter Quantities

## list

List meters.

**Scopes**: `meters:read` `meters:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="meters:list" method="get" path="/v1/meters/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.meters.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.MetersListQueryParamOrganizationIDFilter]](../../models/meterslistqueryparamorganizationidfilter.md)                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by name.                                                                                                                                                         |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.MeterSortProperty](../../models/metersortproperty.md)]                                                                                                     | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `metadata`                                                                                                                                                              | Dict[str, [models.MetadataQuery](../../models/metadataquery.md)]                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`.                                                                        |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.MetersListResponse](../../models/meterslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a meter.

**Scopes**: `meters:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="meters:create" method="post" path="/v1/meters/" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.meters.create(request={
        "name": "<value>",
        "filter_": {
            "conjunction": polar_sdk.FilterConjunction.OR,
            "clauses": [
                {
                    "property": "<value>",
                    "operator": polar_sdk.FilterOperator.NE,
                    "value": "<value>",
                },
            ],
        },
        "aggregation": {
            "func": polar_sdk.Func.SUM,
            "property": "<value>",
        },
        "organization_id": "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MeterCreate](../../models/metercreate.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Meter](../../models/meter.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a meter by ID.

**Scopes**: `meters:read` `meters:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="meters:get" method="get" path="/v1/meters/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.meters.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The meter ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Meter](../../models/meter.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a meter.

**Scopes**: `meters:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="meters:update" method="patch" path="/v1/meters/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.meters.update(id="<value>", meter_update={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The meter ID.                                                       |
| `meter_update`                                                      | [models.MeterUpdate](../../models/meterupdate.md)                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Meter](../../models/meter.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## quantities

Get quantities of a meter over a time period.

**Scopes**: `meters:read` `meters:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="meters:quantities" method="get" path="/v1/meters/{id}/quantities" -->
```python
import polar_sdk
from polar_sdk import Polar
from polar_sdk.utils import parse_datetime


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.meters.quantities(id="<value>", start_timestamp=parse_datetime("2025-11-25T04:37:16.823Z"), end_timestamp=parse_datetime("2025-11-26T17:06:00.727Z"), interval=polar_sdk.TimeInterval.DAY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                              | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The meter ID.                                                                                                                                     |
| `start_timestamp`                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                              | :heavy_check_mark:                                                                                                                                | Start timestamp.                                                                                                                                  |
| `end_timestamp`                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                              | :heavy_check_mark:                                                                                                                                | End timestamp.                                                                                                                                    |
| `interval`                                                                                                                                        | [models.TimeInterval](../../models/timeinterval.md)                                                                                               | :heavy_check_mark:                                                                                                                                | Interval between two timestamps.                                                                                                                  |
| `customer_id`                                                                                                                                     | [OptionalNullable[models.MetersQuantitiesQueryParamCustomerIDFilter]](../../models/metersquantitiesqueryparamcustomeridfilter.md)                 | :heavy_minus_sign:                                                                                                                                | Filter by customer ID.                                                                                                                            |
| `external_customer_id`                                                                                                                            | [OptionalNullable[models.MetersQuantitiesQueryParamExternalCustomerIDFilter]](../../models/metersquantitiesqueryparamexternalcustomeridfilter.md) | :heavy_minus_sign:                                                                                                                                | Filter by external customer ID.                                                                                                                   |
| `metadata`                                                                                                                                        | Dict[str, [models.MetadataQuery](../../models/metadataquery.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                | Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`.                                                  |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.MeterQuantities](../../models/meterquantities.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |