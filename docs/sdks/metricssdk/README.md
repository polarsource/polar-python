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


res = s.metrics.retrieve(request={
    "start_date": dateutil.parser.parse("2023-02-11").date(),
    "end_date": dateutil.parser.parse("2024-11-01").date(),
    "interval": polar_sh.Interval.HOUR,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MetricsGetRequest](../../models/metricsgetrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
