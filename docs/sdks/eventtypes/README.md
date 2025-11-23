# EventTypes
(*event_types*)

## Overview

### Available Operations

* [update_event_type](#update_event_type) - Update Event Type

## update_event_type

Update an event type's label.

### Example Usage

<!-- UsageSnippet language="python" operationID="event_types:update_event_type" method="patch" path="/v1/event_types/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.event_types.update_event_type(id="<value>", event_type_update={
        "label": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The event type ID.                                                  |
| `event_type_update`                                                 | [models.EventTypeUpdate](../../models/eventtypeupdate.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EventType](../../models/eventtype.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |