# MetricsSDK
(*metrics*)

## Overview

### Available Operations

* [retrieve](#retrieve) - Get Metrics
* [limits](#limits) - Get Metrics Limits

## retrieve

Get metrics about your orders and subscriptions.

### Example Usage

```python
import dateutil.parser
import polar_sh
from polar_sh import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.retrieve(start_date=dateutil.parser.parse("2023-02-11").date(), end_date=dateutil.parser.parse("2024-11-01").date(), interval=polar_sh.Interval.HOUR)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                         | Type                                                                                                                                                                              | Required                                                                                                                                                                          | Description                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                      | :heavy_check_mark:                                                                                                                                                                | Start date.                                                                                                                                                                       |
| `end_date`                                                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                      | :heavy_check_mark:                                                                                                                                                                | End date.                                                                                                                                                                         |
| `interval`                                                                                                                                                                        | [models.Interval](../../models/interval.md)                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                | Interval between two timestamps.                                                                                                                                                  |
| `organization_id`                                                                                                                                                                 | [OptionalNullable[models.MetricsGetQueryParamOrganizationIDFilter]](../../models/metricsgetqueryparamorganizationidfilter.md)                                                     | :heavy_minus_sign:                                                                                                                                                                | Filter by organization ID.                                                                                                                                                        |
| `product_id`                                                                                                                                                                      | [OptionalNullable[models.MetricsGetQueryParamProductIDFilter]](../../models/metricsgetqueryparamproductidfilter.md)                                                               | :heavy_minus_sign:                                                                                                                                                                | Filter by product ID.                                                                                                                                                             |
| `product_price_type`                                                                                                                                                              | [OptionalNullable[models.MetricsGetQueryParamProductPriceTypeFilter]](../../models/metricsgetqueryparamproductpricetypefilter.md)                                                 | :heavy_minus_sign:                                                                                                                                                                | Filter by product price type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases. |
| `retries`                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                               |

### Response

**[models.MetricsResponse](../../models/metricsresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## limits

Get the interval limits for the metrics endpoint.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.metrics.limits()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsLimits](../../models/metricslimits.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
