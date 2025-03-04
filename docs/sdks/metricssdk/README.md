# MetricsSDK
(*metrics*)

## Overview

### Available Operations

* [get](#get) - Get Metrics
* [limits](#limits) - Get Metrics Limits

## get

Get metrics about your orders and subscriptions.

Currency values are output in cents.

**Scopes**: `metrics:read`

### Example Usage

```python
import dateutil.parser
import polar_sdk
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.get(start_date=dateutil.parser.parse("2025-02-06").date(), end_date=dateutil.parser.parse("2024-09-04").date(), interval=polar_sdk.TimeInterval.WEEK)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                                                                                | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                | :heavy_check_mark:                                                                                                                                                          | Start date.                                                                                                                                                                 |
| `end_date`                                                                                                                                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                | :heavy_check_mark:                                                                                                                                                          | End date.                                                                                                                                                                   |
| `interval`                                                                                                                                                                  | [models.TimeInterval](../../models/timeinterval.md)                                                                                                                         | :heavy_check_mark:                                                                                                                                                          | Interval between two timestamps.                                                                                                                                            |
| `organization_id`                                                                                                                                                           | [OptionalNullable[models.MetricsGetQueryParamOrganizationIDFilter]](../../models/metricsgetqueryparamorganizationidfilter.md)                                               | :heavy_minus_sign:                                                                                                                                                          | Filter by organization ID.                                                                                                                                                  |
| `product_id`                                                                                                                                                                | [OptionalNullable[models.MetricsGetQueryParamProductIDFilter]](../../models/metricsgetqueryparamproductidfilter.md)                                                         | :heavy_minus_sign:                                                                                                                                                          | Filter by product ID.                                                                                                                                                       |
| `billing_type`                                                                                                                                                              | [OptionalNullable[models.QueryParamProductBillingTypeFilter]](../../models/queryparamproductbillingtypefilter.md)                                                           | :heavy_minus_sign:                                                                                                                                                          | Filter by billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases. |
| `customer_id`                                                                                                                                                               | [OptionalNullable[models.MetricsGetQueryParamCustomerIDFilter]](../../models/metricsgetqueryparamcustomeridfilter.md)                                                       | :heavy_minus_sign:                                                                                                                                                          | Filter by customer ID.                                                                                                                                                      |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |

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