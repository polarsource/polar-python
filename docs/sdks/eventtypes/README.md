# EventTypes
(*event_types*)

## Overview

### Available Operations

* [list](#list) - List Event Types
* [update](#update) - Update Event Type

## list

List event types with aggregated statistics.

**Scopes**: `events:read` `events:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="event-types:list" method="get" path="/v1/event-types/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.event_types.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", root_events=False, page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.EventTypesListQueryParamOrganizationIDFilter]](../../models/eventtypeslistqueryparamorganizationidfilter.md)                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.EventTypesListQueryParamCustomerIDFilter]](../../models/eventtypeslistqueryparamcustomeridfilter.md)                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.EventTypesListQueryParamExternalCustomerIDFilter]](../../models/eventtypeslistqueryparamexternalcustomeridfilter.md)                           | :heavy_minus_sign:                                                                                                                                                      | Filter by external customer ID.                                                                                                                                         |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Query to filter event types by name or label.                                                                                                                           |
| `root_events`                                                                                                                                                           | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | When true, only return event types with root events (parent_id IS NULL).                                                                                                |
| `parent_id`                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by specific parent event ID.                                                                                                                                     |
| `source`                                                                                                                                                                | [OptionalNullable[models.EventSource]](../../models/eventsource.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by event source (system or user).                                                                                                                                |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.EventTypesSortProperty](../../models/eventtypessortproperty.md)]                                                                                           | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.EventTypesListResponse](../../models/eventtypeslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update an event type's label.

### Example Usage

<!-- UsageSnippet language="python" operationID="event-types:update" method="patch" path="/v1/event-types/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.event_types.update(id="<value>", event_type_update={
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