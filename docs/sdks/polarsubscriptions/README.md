# PolarSubscriptions
(*users.subscriptions*)

## Overview

### Available Operations

* [list](#list) - List Subscriptions
* [create](#create) - Create Free Subscription
* [retrieve](#retrieve) - Get Subscription
* [update](#update) - Update Subscription
* [cancel](#cancel) - Cancel Subscription

## list

List my subscriptions.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.subscriptions.list()

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.UsersSubscriptionsListQueryParamOrganizationIDFilter]](../../models/userssubscriptionslistqueryparamorganizationidfilter.md)                   | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `product_id`                                                                                                                                                            | [OptionalNullable[models.QueryParamProductIDFilter]](../../models/queryparamproductidfilter.md)                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter by product ID.                                                                                                                                                   |
| `active`                                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                      | Filter by active or cancelled subscription.                                                                                                                             |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Search by product or organization name.                                                                                                                                 |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.UserSubscriptionSortProperty](../../models/usersubscriptionsortproperty.md)]                                                                               | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.UsersSubscriptionsListResponse](../../models/userssubscriptionslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create a subscription on a **free** tier.

If you want to subscribe to a paid tier, you need to create a checkout session.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.subscriptions.create(request={
    "product_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.UserFreeSubscriptionCreate](../../models/userfreesubscriptioncreate.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AlreadySubscribed   | 400                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get a subscription by ID.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.subscriptions.retrieve(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The subscription ID.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update a subscription.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.subscriptions.update(id="<value>", user_subscription_update={
    "product_price_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | The subscription ID.                                                    |
| `user_subscription_update`                                              | [models.UserSubscriptionUpdate](../../models/usersubscriptionupdate.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.FreeSubscriptionUpgrade | 403                            | application/json               |
| models.ResourceNotFound        | 404                            | application/json               |
| models.HTTPValidationError     | 422                            | application/json               |
| models.SDKError                | 4xx-5xx                        | */*                            |


## cancel

Cancel a subscription.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.subscriptions.cancel(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The subscription ID.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.AlreadyCanceledSubscription | 403                                | application/json                   |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4xx-5xx                            | */*                                |
