# Users
(*users*)

## Overview

### Available Operations

* [users_list_benefits](#users_list_benefits) - List Benefits
* [users_get_benefit](#users_get_benefit) - Get Benefit
* [users_list_orders](#users_list_orders) - List Orders
* [users_get_order](#users_get_order) - Get Order
* [users_get_order_invoice](#users_get_order_invoice) - Get Order Invoice
* [users_list_subscriptions](#users_list_subscriptions) - List Subscriptions
* [users_create_subscription](#users_create_subscription) - Create Subscription
* [users_get_subscription](#users_get_subscription) - Get Subscription
* [users_cancel_subscription](#users_cancel_subscription) - Cancel Subscription
* [users_update_subscription](#users_update_subscription) - Update Subscription
* [users_list_advertisement_campaigns](#users_list_advertisement_campaigns) - List Advertisement Campaigns
* [users_create_advertisement_campaign](#users_create_advertisement_campaign) - Create Advertisement Campaign
* [users_get_advertisement_campaign](#users_get_advertisement_campaign) - Get Advertisement Campaign
* [users_delete_advertisement_campaign](#users_delete_advertisement_campaign) - Delete Advertisement Campaign
* [users_update_advertisement_campaign](#users_update_advertisement_campaign) - Update Advertisement Campaign
* [users_enable_advertisement_campaign](#users_enable_advertisement_campaign) - Enable Advertisement Campaign
* [users_list_downloadables](#users_list_downloadables) - List Downloadables
* [users_get_downloadable](#users_get_downloadable) - Get Downloadable

## users_list_benefits

List my granted benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.UsersListBenefitsRequest](../../models/userslistbenefitsrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `security`                                                                  | [models.UsersListBenefitsSecurity](../../userslistbenefitssecurity.md)      | :heavy_check_mark:                                                          | The security requirements to use for the request.                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ListResourceAnnotatedUnionBenefitArticlesSubscriberBenefitAdsSubscriberBenefitDiscordSubscriberBenefitCustomSubscriberBenefitGitHubRepositorySubscriberBenefitDownloadablesSubscriberDiscriminatorMergeJSONSchema](../../models/listresourceannotatedunionbenefitarticlessubscriberbenefitadssubscriberbenefitdiscordsubscriberbenefitcustomsubscriberbenefitgithubrepositorysubscriberbenefitdownloadablessubscriberdiscriminatormergejsonschema.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_get_benefit

Get a granted benefit by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_get_benefit(security=polar_sh.UsersGetBenefitSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.UsersGetBenefitSecurity](../../models/usersgetbenefitsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | The benefit ID.                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.UsersGetBenefitResponseUsersGetBenefit](../../models/usersgetbenefitresponseusersgetbenefit.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_list_orders

List my orders.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_orders(security=polar_sh.UsersListOrdersSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.UsersListOrdersRequest](../../models/userslistordersrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `security`                                                              | [models.UsersListOrdersSecurity](../../userslistorderssecurity.md)      | :heavy_check_mark:                                                      | The security requirements to use for the request.                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ListResourceUserOrder](../../models/listresourceuserorder.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_get_order

Get an order by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_get_order(security=polar_sh.UsersGetOrderSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.UsersGetOrderSecurity](../../models/usersgetordersecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | The order ID.                                                         |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.UserOrder](../../models/userorder.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_get_order_invoice

Get an order's invoice data.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_get_order_invoice(security=polar_sh.UsersGetOrderInvoiceSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.UsersGetOrderInvoiceSecurity](../../models/usersgetorderinvoicesecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The order ID.                                                                       |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UserOrderInvoice](../../models/userorderinvoice.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_list_subscriptions

List my subscriptions.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_subscriptions(security=polar_sh.UsersListSubscriptionsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.UsersListSubscriptionsRequest](../../models/userslistsubscriptionsrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `security`                                                                            | [models.UsersListSubscriptionsSecurity](../../userslistsubscriptionssecurity.md)      | :heavy_check_mark:                                                                    | The security requirements to use for the request.                                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ListResourceUserSubscription](../../models/listresourceusersubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_create_subscription

Create a subscription on a **free** tier.

If you want to subscribe to a paid tier, you need to create a checkout session.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_create_subscription(security=polar_sh.UsersCreateSubscriptionSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "product_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [models.UserFreeSubscriptionCreate](../../models/userfreesubscriptioncreate.md)    | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [models.UsersCreateSubscriptionSecurity](../../userscreatesubscriptionsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.AlreadySubscribed   | 400                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_get_subscription

Get a subscription by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_get_subscription(security=polar_sh.UsersGetSubscriptionSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.UsersGetSubscriptionSecurity](../../models/usersgetsubscriptionsecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The subscription ID.                                                                |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_cancel_subscription

Cancel a subscription.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_cancel_subscription(security=polar_sh.UsersCancelSubscriptionSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.UsersCancelSubscriptionSecurity](../../models/userscancelsubscriptionsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `id`                                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | The subscription ID.                                                                      |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.AlreadyCanceledSubscription | 403                                | application/json                   |
| models.ResourceNotFound            | 404                                | application/json                   |
| models.HTTPValidationError         | 422                                | application/json                   |
| models.SDKError                    | 4xx-5xx                            | */*                                |


## users_update_subscription

Update a subscription.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_update_subscription(security=polar_sh.UsersUpdateSubscriptionSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", user_subscription_update={
    "product_price_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.UsersUpdateSubscriptionSecurity](../../models/usersupdatesubscriptionsecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `id`                                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | The subscription ID.                                                                      |
| `user_subscription_update`                                                                | [models.UserSubscriptionUpdate](../../models/usersubscriptionupdate.md)                   | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.UserSubscription](../../models/usersubscription.md)**

### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.FreeSubscriptionUpgrade | 403                            | application/json               |
| models.ResourceNotFound        | 404                            | application/json               |
| models.HTTPValidationError     | 422                            | application/json               |
| models.SDKError                | 4xx-5xx                        | */*                            |


## users_list_advertisement_campaigns

List advertisement campaigns.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_advertisement_campaigns(security=polar_sh.UsersListAdvertisementCampaignsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.UsersListAdvertisementCampaignsSecurity](../../models/userslistadvertisementcampaignssecurity.md)                                                               | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | [OptionalNullable[models.UsersListAdvertisementCampaignsQueryParamSorting]](../../models/userslistadvertisementcampaignsqueryparamsorting.md)                           | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.ListResourceUserAdvertisementCampaign](../../models/listresourceuseradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_create_advertisement_campaign

Create an advertisement campaign.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_create_advertisement_campaign(security=polar_sh.UsersCreateAdvertisementCampaignSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "image_url": "http://fruitful-aid.com",
    "text": "<value>",
    "link_url": "http://snoopy-bit.org",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [models.UserAdvertisementCampaignCreate](../../models/useradvertisementcampaigncreate.md)            | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [models.UsersCreateAdvertisementCampaignSecurity](../../userscreateadvertisementcampaignsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[models.UserAdvertisementCampaign](../../models/useradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_get_advertisement_campaign

Get an advertisement campaign by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_get_advertisement_campaign(security=polar_sh.UsersGetAdvertisementCampaignSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.UsersGetAdvertisementCampaignSecurity](../../models/usersgetadvertisementcampaignsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The advertisement campaign ID.                                                                        |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.UserAdvertisementCampaign](../../models/useradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_delete_advertisement_campaign

Delete an advertisement campaign.

It'll be automatically disabled on all granted benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_delete_advertisement_campaign(security=polar_sh.UsersDeleteAdvertisementCampaignSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                  | [models.UsersDeleteAdvertisementCampaignSecurity](../../models/usersdeleteadvertisementcampaignsecurity.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `id`                                                                                                        | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The advertisement campaign ID.                                                                              |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_update_advertisement_campaign

Update an advertisement campaign.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_update_advertisement_campaign(security=polar_sh.UsersUpdateAdvertisementCampaignSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", user_advertisement_campaign_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                  | [models.UsersUpdateAdvertisementCampaignSecurity](../../models/usersupdateadvertisementcampaignsecurity.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `id`                                                                                                        | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The advertisement campaign ID.                                                                              |
| `user_advertisement_campaign_update`                                                                        | [models.UserAdvertisementCampaignUpdate](../../models/useradvertisementcampaignupdate.md)                   | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.UserAdvertisementCampaign](../../models/useradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_enable_advertisement_campaign

Enable an advertisement campaign on a granted benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.users.users_enable_advertisement_campaign(security=polar_sh.UsersEnableAdvertisementCampaignSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", user_advertisement_campaign_enable={
    "benefit_id": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                  | [models.UsersEnableAdvertisementCampaignSecurity](../../models/usersenableadvertisementcampaignsecurity.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `id`                                                                                                        | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The advertisement campaign ID.                                                                              |
| `user_advertisement_campaign_enable`                                                                        | [models.UserAdvertisementCampaignEnable](../../models/useradvertisementcampaignenable.md)                   | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_list_downloadables

List Downloadables

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_downloadables(security=polar_sh.UsersListDownloadablesSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                            | [models.UsersListDownloadablesSecurity](../../models/userslistdownloadablessecurity.md)                                                               | :heavy_check_mark:                                                                                                                                    | N/A                                                                                                                                                   |
| `organization_id`                                                                                                                                     | [OptionalNullable[models.UsersListDownloadablesQueryParamOrganizationIDFilter]](../../models/userslistdownloadablesqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                                    | Filter by organization ID.                                                                                                                            |
| `benefit_id`                                                                                                                                          | [OptionalNullable[models.BenefitIDFilter]](../../models/benefitidfilter.md)                                                                           | :heavy_minus_sign:                                                                                                                                    | Filter by given benefit ID.                                                                                                                           |
| `page`                                                                                                                                                | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Page number, defaults to 1.                                                                                                                           |
| `limit`                                                                                                                                               | *Optional[int]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Size of a page, defaults to 10. Maximum is 100.                                                                                                       |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.ListResourceDownloadableRead](../../models/listresourcedownloadableread.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## users_get_downloadable

Get Downloadable

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_get_downloadable(security=polar_sh.UsersGetDownloadableSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), token="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.UsersGetDownloadableSecurity](../../models/usersgetdownloadablesecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `token`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
