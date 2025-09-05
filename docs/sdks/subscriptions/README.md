# Subscriptions
(*subscriptions*)

## Overview

### Available Operations

* [list](#list) - List Subscriptions
* [export](#export) - Export Subscriptions
* [get](#get) - Get Subscription
* [update](#update) - Update Subscription
* [revoke](#revoke) - Revoke Subscription

## list

List subscriptions.

**Scopes**: `subscriptions:read` `subscriptions:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="subscriptions:list" method="get" path="/v1/subscriptions/" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.OrganizationIDFilter]](../../models/organizationidfilter.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `product_id`                                                                                                                                                            | [OptionalNullable[models.ProductIDFilter]](../../models/productidfilter.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                      | Filter by product ID.                                                                                                                                                   |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.CustomerIDFilter]](../../models/customeridfilter.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `external_customer_id`                                                                                                                                                  | [OptionalNullable[models.ExternalCustomerIDFilter]](../../models/externalcustomeridfilter.md)                                                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by customer external ID.                                                                                                                                         |
| `discount_id`                                                                                                                                                           | [OptionalNullable[models.DiscountIDFilter]](../../models/discountidfilter.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by discount ID.                                                                                                                                                  |
| `active`                                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                      | Filter by active or inactive subscription.                                                                                                                              |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.SubscriptionSortProperty](../../models/subscriptionsortproperty.md)]                                                                                       | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `metadata`                                                                                                                                                              | Dict[str, [models.MetadataQuery](../../models/metadataquery.md)]                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Filter by metadata key-value pairs. It uses the `deepObject` style, e.g. `?metadata[key]=value`.                                                                        |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.SubscriptionsListResponse](../../models/subscriptionslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## export

Export subscriptions as a CSV file.

**Scopes**: `subscriptions:read` `subscriptions:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="subscriptions:export" method="get" path="/v1/subscriptions/export" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.export(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `organization_id`                                                         | [OptionalNullable[models.OrganizationID]](../../models/organizationid.md) | :heavy_minus_sign:                                                        | Filter by organization ID.                                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a subscription by ID.

**Scopes**: `subscriptions:read` `subscriptions:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="subscriptions:get" method="get" path="/v1/subscriptions/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The subscription ID.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Subscription](../../models/subscription.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a subscription.

**Scopes**: `subscriptions:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="subscriptions:update" method="patch" path="/v1/subscriptions/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.update(id="<value>", subscription_update={
        "product_id": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The subscription ID.                                                |
| `subscription_update`                                               | [models.SubscriptionUpdate](../../models/subscriptionupdate.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Subscription](../../models/subscription.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.AlreadyCanceledSubscription | 403                                | application/json                   |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.SubscriptionLocked          | 409                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## revoke

Revoke a subscription, i.e cancel immediately.

**Scopes**: `subscriptions:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="subscriptions:revoke" method="delete" path="/v1/subscriptions/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.revoke(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The subscription ID.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Subscription](../../models/subscription.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.AlreadyCanceledSubscription | 403                                | application/json                   |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.SubscriptionLocked          | 409                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |