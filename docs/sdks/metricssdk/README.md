# MetricsSDK
(*metrics*)

## Overview

### Available Operations

* [get](#get) - Get Metrics
* [limits](#limits) - Get Metrics Limits
* [list_dashboards](#list_dashboards) - List Metric Dashboards
* [create_dashboard](#create_dashboard) - Create Metric Dashboard
* [get_dashboard](#get_dashboard) - Get Metric Dashboard
* [update_dashboard](#update_dashboard) - Update Metric Dashboard
* [delete_dashboard](#delete_dashboard) - Delete Metric Dashboard

## get

Get metrics about your orders and subscriptions.

Currency values are output in cents.

**Scopes**: `metrics:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:get" method="get" path="/v1/metrics/" -->
```python
from datetime import date
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.get(start_date=date.fromisoformat("2025-03-14"), end_date=date.fromisoformat("2025-03-18"), interval=polar_sdk.TimeInterval.HOUR, timezone="UTC", organization_id=None)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `start_date`                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                   | :heavy_check_mark:                                                                                                                                                             | Start date.                                                                                                                                                                    |
| `end_date`                                                                                                                                                                     | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                   | :heavy_check_mark:                                                                                                                                                             | End date.                                                                                                                                                                      |
| `interval`                                                                                                                                                                     | [models.TimeInterval](../../models/timeinterval.md)                                                                                                                            | :heavy_check_mark:                                                                                                                                                             | Interval between two timestamps.                                                                                                                                               |
| `timezone`                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                             | Timezone to use for the timestamps. Default is UTC.                                                                                                                            |
| `organization_id`                                                                                                                                                              | [OptionalNullable[models.MetricsGetQueryParamOrganizationIDFilter]](../../models/metricsgetqueryparamorganizationidfilter.md)                                                  | :heavy_minus_sign:                                                                                                                                                             | Filter by organization ID.                                                                                                                                                     |
| `product_id`                                                                                                                                                                   | [OptionalNullable[models.MetricsGetQueryParamProductIDFilter]](../../models/metricsgetqueryparamproductidfilter.md)                                                            | :heavy_minus_sign:                                                                                                                                                             | Filter by product ID.                                                                                                                                                          |
| `billing_type`                                                                                                                                                                 | [OptionalNullable[models.QueryParamProductBillingTypeFilter]](../../models/queryparamproductbillingtypefilter.md)                                                              | :heavy_minus_sign:                                                                                                                                                             | Filter by billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases.    |
| `customer_id`                                                                                                                                                                  | [OptionalNullable[models.MetricsGetQueryParamCustomerIDFilter]](../../models/metricsgetqueryparamcustomeridfilter.md)                                                          | :heavy_minus_sign:                                                                                                                                                             | Filter by customer ID.                                                                                                                                                         |
| `metrics`                                                                                                                                                                      | List[*str*]                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                             | List of metric slugs to focus on. When provided, only the queries needed for these metrics will be executed, improving performance. If not provided, all metrics are returned. |
| `retries`                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                            |

### Response

**[models.MetricsResponse](../../models/metricsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## limits

Get the interval limits for the metrics endpoint.

**Scopes**: `metrics:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:limits" method="get" path="/v1/metrics/limits" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.limits()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsLimits](../../models/metricslimits.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## list_dashboards

List user-defined metric dashboards.

**Scopes**: `metrics:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:list_dashboards" method="get" path="/v1/metrics/dashboards" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.list_dashboards(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                   | [OptionalNullable[models.MetricsListDashboardsQueryParamOrganizationIDFilter]](../../models/metricslistdashboardsqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                  | Filter by organization ID.                                                                                                                          |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |

### Response

**[List[models.MetricDashboardSchema]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_dashboard

Create a user-defined metric dashboard.

**Scopes**: `metrics:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:create_dashboard" method="post" path="/v1/metrics/dashboards" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.create_dashboard(request={
        "name": "<value>",
        "organization_id": "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.MetricDashboardCreate](../../models/metricdashboardcreate.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.MetricDashboardSchema](../../models/metricdashboardschema.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_dashboard

Get a user-defined metric dashboard by ID.

**Scopes**: `metrics:read`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:get_dashboard" method="get" path="/v1/metrics/dashboards/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.get_dashboard(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The metric dashboard ID.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricDashboardSchema](../../models/metricdashboardschema.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_dashboard

Update a user-defined metric dashboard.

**Scopes**: `metrics:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:update_dashboard" method="patch" path="/v1/metrics/dashboards/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.update_dashboard(id="<value>", metric_dashboard_update={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | The metric dashboard ID.                                              |
| `metric_dashboard_update`                                             | [models.MetricDashboardUpdate](../../models/metricdashboardupdate.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.MetricDashboardSchema](../../models/metricdashboardschema.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_dashboard

Delete a user-defined metric dashboard.

**Scopes**: `metrics:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="metrics:delete_dashboard" method="delete" path="/v1/metrics/dashboards/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.metrics.delete_dashboard(id="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The metric dashboard ID.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |