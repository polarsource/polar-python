# PolarSubscriptions
(*users.subscriptions*)

## Overview

### Available Operations

* [list](#list) - List Subscriptions
* [create](#create) - Create Free Subscription
* [retrieve](#retrieve) - Get Subscription
* [cancel](#cancel) - Cancel Subscription
* [update](#update) - Update Subscription

## list

List my subscriptions.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.subscriptions.list(security=polar_sh.UsersSubscriptionsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.UsersSubscriptionsListRequest](../../models/userssubscriptionslistrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `security`                                                                            | [models.UsersSubscriptionsListSecurity](../../userssubscriptionslistsecurity.md)      | :heavy_check_mark:                                                                    | The security requirements to use for the request.                                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

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
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.subscriptions.create(security=polar_sh.UsersSubscriptionsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "product_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [models.UserFreeSubscriptionCreate](../../models/userfreesubscriptioncreate.md)      | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [models.UsersSubscriptionsCreateSecurity](../../userssubscriptionscreatesecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

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
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.subscriptions.retrieve(security=polar_sh.UsersSubscriptionsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.UsersSubscriptionsGetSecurity](../../models/userssubscriptionsgetsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | The subscription ID.                                                                  |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## cancel

Cancel a subscription.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.subscriptions.cancel(security=polar_sh.UsersSubscriptionsCancelSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.UsersSubscriptionsCancelSecurity](../../models/userssubscriptionscancelsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `id`                                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | The subscription ID.                                                                        |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.AlreadyCanceledSubscription | 403                                | application/json                   |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4xx-5xx                            | */*                                |


## update

Update a subscription.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.subscriptions.update(security=polar_sh.UsersSubscriptionsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", user_subscription_update={
    "product_price_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.UsersSubscriptionsUpdateSecurity](../../models/userssubscriptionsupdatesecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `id`                                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | The subscription ID.                                                                        |
| `user_subscription_update`                                                                  | [models.UserSubscriptionUpdate](../../models/usersubscriptionupdate.md)                     | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.FreeSubscriptionUpgrade | 403                            | application/json               |
| models.ResourceNotFound        | 404                            | application/json               |
| models.HTTPValidationError     | 422                            | application/json               |
| models.SDKError                | 4xx-5xx                        | */*                            |
