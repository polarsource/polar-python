# MetricsSDK
(*metrics*)

## Overview

### Available Operations

* [metrics_get](#metrics_get) - Get Metrics
* [metrics_get_limits](#metrics_get_limits) - Get Metrics Limits

## metrics_get

Get metrics about your orders and subscriptions.

### Example Usage

```python
import dateutil.parser
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.metrics.metrics_get(security=polar_sh.MetricsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "start_date": dateutil.parser.parse("2022-03-06").date(),
    "end_date": dateutil.parser.parse("2022-01-25").date(),
    "interval": polar_sh.Interval.DAY,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MetricsGetRequest](../../models/metricsgetrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.MetricsGetSecurity](../../metricsgetsecurity.md)            | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsResponse](../../models/metricsresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## metrics_get_limits

Get the interval limits for the metrics endpoint.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.metrics.metrics_get_limits(security=polar_sh.MetricsGetLimitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `security`                                                           | [models.MetricsGetLimitsSecurity](../../metricsgetlimitssecurity.md) | :heavy_check_mark:                                                   | The security requirements to use for the request.                    |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.MetricsLimits](../../models/metricslimits.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
