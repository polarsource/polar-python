# Events
(*events*)

## Overview

### Available Operations

* [list](#list) - List Events
* [get](#get) - Get Event
* [ingest](#ingest) - Ingest Events

## list

List events.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.events.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_timestamp`                                                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                    | :heavy_minus_sign:                                                                                                                                                      | Filter events after this timestamp.                                                                                                                                     |
| `end_timestamp`                                                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                    | :heavy_minus_sign:                                                                                                                                                      | Filter events before this timestamp.                                                                                                                                    |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.EventsListQueryParamOrganizationIDFilter]](../../models/eventslistqueryparamorganizationidfilter.md)                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.EventsListQueryParamCustomerIDFilter]](../../models/eventslistqueryparamcustomeridfilter.md)                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.ExternalCustomerIDFilter]](../../models/externalcustomeridfilter.md)                                                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by external customer ID.                                                                                                                                         |
| `source`                                                                                                                                                                | [OptionalNullable[models.SourceFilter]](../../models/sourcefilter.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by event source.                                                                                                                                                 |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.EventSortProperty](../../models/eventsortproperty.md)]                                                                                                     | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `metadata`                                                                                                                                                              | Dict[str, [models.MetadataQuery](../../models/metadataquery.md)]                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`.                                                                        |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.EventsListResponse](../../models/eventslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get an event by ID.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.events.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The event ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Event](../../models/event.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## ingest

Ingest batch of events.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.events.ingest(request={
        "events": [
            {
                "name": "<value>",
                "customer_id": "<value>",
            },
            {
                "name": "<value>",
                "external_customer_id": "<id>",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EventsIngest](../../models/eventsingest.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EventsIngestResponse](../../models/eventsingestresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |