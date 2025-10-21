# PolarSubscriptions
(*customer_portal.subscriptions*)

## Overview

### Available Operations

* [list](#list) - List Subscriptions
* [get](#get) - Get Subscription
* [update](#update) - Update Subscription
* [cancel](#cancel) - Cancel Subscription

## list

List subscriptions of the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:subscriptions:list" method="get" path="/v1/customer-portal/subscriptions/" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.subscriptions.list(security=polar_sdk.CustomerPortalSubscriptionsListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737", page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.CustomerPortalSubscriptionsListSecurity](../../models/customerportalsubscriptionslistsecurity.md)                                                               | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.CustomerPortalSubscriptionsListQueryParamOrganizationIDFilter]](../../models/customerportalsubscriptionslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `product_id`                                                                                                                                                            | [OptionalNullable[models.CustomerPortalSubscriptionsListQueryParamProductIDFilter]](../../models/customerportalsubscriptionslistqueryparamproductidfilter.md)           | :heavy_minus_sign:                                                                                                                                                      | Filter by product ID.                                                                                                                                                   |
| `active`                                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                      | Filter by active or cancelled subscription.                                                                                                                             |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Search by product or organization name.                                                                                                                                 |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CustomerSubscriptionSortProperty](../../models/customersubscriptionsortproperty.md)]                                                                       | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomerPortalSubscriptionsListResponse](../../models/customerportalsubscriptionslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a subscription for the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:subscriptions:get" method="get" path="/v1/customer-portal/subscriptions/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.subscriptions.get(security=polar_sdk.CustomerPortalSubscriptionsGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.CustomerPortalSubscriptionsGetSecurity](../../models/customerportalsubscriptionsgetsecurity.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `id`                                                                                                    | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The subscription ID.                                                                                    |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.CustomerSubscription](../../models/customersubscription.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.PolarExceptionsResourceNotFound | 404                                    | application/json                       |
| models.HTTPValidationError             | 422                                    | application/json                       |
| models.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update a subscription of the authenticated customer.

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:subscriptions:update" method="patch" path="/v1/customer-portal/subscriptions/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.subscriptions.update(security=polar_sdk.CustomerPortalSubscriptionsUpdateSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>", customer_subscription_update={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                    | [models.CustomerPortalSubscriptionsUpdateSecurity](../../models/customerportalsubscriptionsupdatesecurity.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `id`                                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The subscription ID.                                                                                          |
| `customer_subscription_update`                                                                                | [models.CustomerSubscriptionUpdate](../../models/customersubscriptionupdate.md)                               | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CustomerSubscription](../../models/customersubscription.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.PolarExceptionsAlreadyCanceledSubscription | 403                                               | application/json                                  |
| models.PolarExceptionsResourceNotFound            | 404                                               | application/json                                  |
| models.HTTPValidationError                        | 422                                               | application/json                                  |
| models.SDKError                                   | 4XX, 5XX                                          | \*/\*                                             |

## cancel

Cancel a subscription of the authenticated customer.

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:subscriptions:cancel" method="delete" path="/v1/customer-portal/subscriptions/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.subscriptions.cancel(security=polar_sdk.CustomerPortalSubscriptionsCancelSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                    | [models.CustomerPortalSubscriptionsCancelSecurity](../../models/customerportalsubscriptionscancelsecurity.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `id`                                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The subscription ID.                                                                                          |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CustomerSubscription](../../models/customersubscription.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.PolarExceptionsAlreadyCanceledSubscription | 403                                               | application/json                                  |
| models.PolarExceptionsResourceNotFound            | 404                                               | application/json                                  |
| models.HTTPValidationError                        | 422                                               | application/json                                  |
| models.SDKError                                   | 4XX, 5XX                                          | \*/\*                                             |