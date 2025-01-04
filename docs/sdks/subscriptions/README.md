# Subscriptions
(*subscriptions*)

## Overview

### Available Operations

* [list](#list) - List Subscriptions
* [export](#export) - Export Subscriptions
* [update](#update) - Update Subscription
* [revoke](#revoke) - Revoke Subscription

## list

List subscriptions.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.SubscriptionsListQueryParamOrganizationIDFilter]](../../models/subscriptionslistqueryparamorganizationidfilter.md)                             | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `product_id`                                                                                                                                                            | [OptionalNullable[models.ProductIDFilter]](../../models/productidfilter.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                      | Filter by product ID.                                                                                                                                                   |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.CustomerIDFilter]](../../models/customeridfilter.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `discount_id`                                                                                                                                                           | [OptionalNullable[models.DiscountIDFilter]](../../models/discountidfilter.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                      | Filter by discount ID.                                                                                                                                                  |
| `active`                                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                      | Filter by active or inactive subscription.                                                                                                                              |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.SubscriptionSortProperty](../../models/subscriptionsortproperty.md)]                                                                                       | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
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

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.export()

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

## update

Update a subscription.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.subscriptions.update(id="<value>", subscription_update={
        "revoke": True,
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
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## revoke

Revoke a subscription, i.e cancel immediately.

### Example Usage

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
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4XX, 5XX                           | \*/\*                              |