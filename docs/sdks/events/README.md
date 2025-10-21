# Events
(*events*)

## Overview

### Available Operations

* [list](#list) - List Events
* [list_names](#list_names) - List Event Names
* [get](#get) - Get Event
* [ingest](#ingest) - Ingest Events

## list

List events.

**Scopes**: `events:read` `events:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="events:list" method="get" path="/v1/events/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.events.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter events following filter clauses. JSON string following the same schema a meter filter clause.                                                                    |
| `start_timestamp`                                                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                    | :heavy_minus_sign:                                                                                                                                                      | Filter events after this timestamp.                                                                                                                                     |
| `end_timestamp`                                                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                    | :heavy_minus_sign:                                                                                                                                                      | Filter events before this timestamp.                                                                                                                                    |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.EventsListQueryParamOrganizationIDFilter]](../../models/eventslistqueryparamorganizationidfilter.md)                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.EventsListQueryParamCustomerIDFilter]](../../models/eventslistqueryparamcustomeridfilter.md)                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.QueryParamExternalCustomerIDFilter]](../../models/queryparamexternalcustomeridfilter.md)                                                       | :heavy_minus_sign:                                                                                                                                                      | Filter by external customer ID.                                                                                                                                         |
| `meter_id`                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by a meter filter clause.                                                                                                                                        |
| `name`                                                                                                                                                                  | [OptionalNullable[models.NameFilter]](../../models/namefilter.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                      | Filter by event name.                                                                                                                                                   |
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

## list_names

List event names.

**Scopes**: `events:read` `events:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="events:list_names" method="get" path="/v1/events/names" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.events.list_names(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.EventsListNamesQueryParamOrganizationIDFilter]](../../models/eventslistnamesqueryparamorganizationidfilter.md)                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.EventsListNamesQueryParamCustomerIDFilter]](../../models/eventslistnamesqueryparamcustomeridfilter.md)                                         | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.EventsListNamesQueryParamExternalCustomerIDFilter]](../../models/eventslistnamesqueryparamexternalcustomeridfilter.md)                         | :heavy_minus_sign:                                                                                                                                                      | Filter by external customer ID.                                                                                                                                         |
| `source`                                                                                                                                                                | [OptionalNullable[models.QueryParamSourceFilter]](../../models/queryparamsourcefilter.md)                                                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by event source.                                                                                                                                                 |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Query to filter event names.                                                                                                                                            |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.EventNamesSortProperty](../../models/eventnamessortproperty.md)]                                                                                           | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.EventsListNamesResponse](../../models/eventslistnamesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get an event by ID.

**Scopes**: `events:read` `events:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="events:get" method="get" path="/v1/events/{id}" -->
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

**Scopes**: `events:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="events:ingest" method="post" path="/v1/events/ingest" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.events.ingest(request={
        "events": [],
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