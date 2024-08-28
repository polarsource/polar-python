# Documented
(*documented*)

## Overview

Endpoints shown and documented in the Polar API documentation.

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
* [external_organizations_list](#external_organizations_list) - List External Organizations
* [repositories_list](#repositories_list) - List Repositories
* [repositories_get](#repositories_get) - Get Repository
* [repositories_update](#repositories_update) - Update Repository
* [organizations_list](#organizations_list) - List Organizations
* [organizations_create](#organizations_create) - Create Organization
* [organizations_get](#organizations_get) - Get Organization
* [organizations_update](#organizations_update) - Update Organization
* [organizations_list_organization_customers](#organizations_list_organization_customers) - List Organization Customers
* [subscriptions_list](#subscriptions_list) - List Subscriptions
* [subscriptions_create](#subscriptions_create) - Create Free Subscription
* [subscriptions_import](#subscriptions_import) - Import Subscriptions
* [subscriptions_export](#subscriptions_export) - Export Subscriptions
* [articles_list](#articles_list) - List Articles
* [articles_create](#articles_create) - Create Article
* [articles_get](#articles_get) - Get Article
* [articles_delete](#articles_delete) - Delete Article
* [articles_update](#articles_update) - Update Article
* [articles_get_receivers](#articles_get_receivers) - Get Article Receivers Count
* [articles_send_preview](#articles_send_preview) - Send Article Preview
* [articles_send](#articles_send) - Send Article
* [advertisements_list](#advertisements_list) - List Campaigns
* [advertisements_get](#advertisements_get) - Get Campaign
* [oauth2_list_clients](#oauth2_list_clients) - List Clients
* [oauth2_oauth2_create_client](#oauth2_oauth2_create_client) - Create Client
* [oauth2_oauth2_get_client](#oauth2_oauth2_get_client) - Get Client
* [oauth2_oauth2_update_client](#oauth2_oauth2_update_client) - Update Client
* [oauth2_oauth2_delete_client](#oauth2_oauth2_delete_client) - Delete Client
* [oauth2_authorize](#oauth2_authorize) - Authorize
* [oauth2_request_token](#oauth2_request_token) - Request Token
* [oauth2_revoke_token](#oauth2_revoke_token) - Revoke Token
* [oauth2_introspect_token](#oauth2_introspect_token) - Introspect Token
* [oauth2_userinfo](#oauth2_userinfo) - Get User Info
* [benefits_list](#benefits_list) - List Benefits
* [benefits_create](#benefits_create) - Create Benefit
* [benefits_get](#benefits_get) - Get Benefit
* [benefits_delete](#benefits_delete) - Delete Benefit
* [benefits_update](#benefits_update) - Update Benefit
* [benefits_list_grants](#benefits_list_grants) - List Benefit Grants
* [products_list](#products_list) - List Products
* [products_create](#products_create) - Create Product
* [products_get](#products_get) - Get Product
* [products_update](#products_update) - Update Product
* [products_update_benefits](#products_update_benefits) - Update Product Benefits
* [orders_list](#orders_list) - List Orders
* [orders_get](#orders_get) - Get Order
* [orders_get_invoice](#orders_get_invoice) - Get Order Invoice
* [checkouts_create](#checkouts_create) - Create Checkout
* [checkouts_get](#checkouts_get) - Get Checkout
* [files_list](#files_list) - List Files
* [files_create](#files_create) - Create File
* [files_uploaded](#files_uploaded) - Complete File Upload
* [files_delete](#files_delete) - Delete File
* [files_update](#files_update) - Update File
* [metrics_get](#metrics_get) - Get Metrics
* [metrics_get_limits](#metrics_get_limits) - Get Metrics Limits

## users_list_benefits

List my granted benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
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


res = s.documented.users_get_benefit(security=polar_sh.UsersGetBenefitSecurity(
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


res = s.documented.users_list_orders(security=polar_sh.UsersListOrdersSecurity(
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


res = s.documented.users_get_order(security=polar_sh.UsersGetOrderSecurity(
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


res = s.documented.users_get_order_invoice(security=polar_sh.UsersGetOrderInvoiceSecurity(
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


res = s.documented.users_list_subscriptions(security=polar_sh.UsersListSubscriptionsSecurity(
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


res = s.documented.users_create_subscription(security=polar_sh.UsersCreateSubscriptionSecurity(
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


res = s.documented.users_get_subscription(security=polar_sh.UsersGetSubscriptionSecurity(
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


res = s.documented.users_cancel_subscription(security=polar_sh.UsersCancelSubscriptionSecurity(
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


res = s.documented.users_update_subscription(security=polar_sh.UsersUpdateSubscriptionSecurity(
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


res = s.documented.users_list_advertisement_campaigns(security=polar_sh.UsersListAdvertisementCampaignsSecurity(
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


res = s.documented.users_create_advertisement_campaign(security=polar_sh.UsersCreateAdvertisementCampaignSecurity(
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


res = s.documented.users_get_advertisement_campaign(security=polar_sh.UsersGetAdvertisementCampaignSecurity(
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


res = s.documented.users_delete_advertisement_campaign(security=polar_sh.UsersDeleteAdvertisementCampaignSecurity(
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


res = s.documented.users_update_advertisement_campaign(security=polar_sh.UsersUpdateAdvertisementCampaignSecurity(
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


s.documented.users_enable_advertisement_campaign(security=polar_sh.UsersEnableAdvertisementCampaignSecurity(
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


res = s.documented.users_list_downloadables(security=polar_sh.UsersListDownloadablesSecurity(
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


res = s.documented.users_get_downloadable(security=polar_sh.UsersGetDownloadableSecurity(
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


## external_organizations_list

List external organizations.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.external_organizations_list(security=polar_sh.ExternalOrganizationsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.ExternalOrganizationsListRequest](../../models/externalorganizationslistrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `security`                                                                                  | [models.ExternalOrganizationsListSecurity](../../externalorganizationslistsecurity.md)      | :heavy_check_mark:                                                                          | The security requirements to use for the request.                                           |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListResourceExternalOrganization](../../models/listresourceexternalorganization.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## repositories_list

List repositories.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.repositories_list(security=polar_sh.RepositoriesListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.RepositoriesListRequest](../../models/repositorieslistrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `security`                                                                | [models.RepositoriesListSecurity](../../repositorieslistsecurity.md)      | :heavy_check_mark:                                                        | The security requirements to use for the request.                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ListResourceRepository](../../models/listresourcerepository.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## repositories_get

Get a repository by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.repositories_get(security=polar_sh.RepositoriesGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.RepositoriesGetSecurity](../../models/repositoriesgetsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.RepositoryOutput](../../models/repositoryoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## repositories_update

Update a repository.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.repositories_update(security=polar_sh.RepositoriesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", repository_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.RepositoriesUpdateSecurity](../../models/repositoriesupdatesecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `repository_update`                                                             | [models.RepositoryUpdate](../../models/repositoryupdate.md)                     | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.RepositoryOutput](../../models/repositoryoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## organizations_list

List organizations.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.organizations_list(security=polar_sh.OrganizationsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.OrganizationsListRequest](../../models/organizationslistrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `security`                                                                  | [models.OrganizationsListSecurity](../../organizationslistsecurity.md)      | :heavy_check_mark:                                                          | The security requirements to use for the request.                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ListResourceOrganization](../../models/listresourceorganization.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## organizations_create

Create an organization.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.organizations_create(security=polar_sh.OrganizationsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "name": "<value>",
    "slug": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [models.OrganizationCreate](../../models/organizationcreate.md)            | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [models.OrganizationsCreateSecurity](../../organizationscreatesecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.OrganizationOutput](../../models/organizationoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## organizations_get

Get an organization by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.organizations_get(security=polar_sh.OrganizationsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.OrganizationsGetSecurity](../../models/organizationsgetsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.OrganizationOutput](../../models/organizationoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## organizations_update

Update an organization.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.organizations_update(security=polar_sh.OrganizationsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", organization_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.OrganizationsUpdateSecurity](../../models/organizationsupdatesecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `organization_update`                                                             | [models.OrganizationUpdate](../../models/organizationupdate.md)                   | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.OrganizationOutput](../../models/organizationoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## organizations_list_organization_customers

List organization customers.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.organizations_list_organization_customers(security=polar_sh.OrganizationsListOrganizationCustomersSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                              | [models.OrganizationsListOrganizationCustomersSecurity](../../models/organizationslistorganizationcustomerssecurity.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `id`                                                                                                                    | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `customer_types`                                                                                                        | List[[models.OrganizationCustomerType](../../models/organizationcustomertype.md)]                                       | :heavy_minus_sign:                                                                                                      | Filter by the type of purchase the customer made.                                                                       |
| `page`                                                                                                                  | *Optional[int]*                                                                                                         | :heavy_minus_sign:                                                                                                      | Page number, defaults to 1.                                                                                             |
| `limit`                                                                                                                 | *Optional[int]*                                                                                                         | :heavy_minus_sign:                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                         |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.ListResourceOrganizationCustomer](../../models/listresourceorganizationcustomer.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_list

List subscriptions.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.subscriptions_list(security=polar_sh.SubscriptionsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.SubscriptionsListRequest](../../models/subscriptionslistrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `security`                                                                  | [models.SubscriptionsListSecurity](../../subscriptionslistsecurity.md)      | :heavy_check_mark:                                                          | The security requirements to use for the request.                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ListResourceSubscription](../../models/listresourcesubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_create

Create a subscription on the free tier for a given email.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.subscriptions_create(security=polar_sh.SubscriptionsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "email": "Paxton_Schaden@hotmail.com",
    "product_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [models.SubscriptionCreateEmail](../../models/subscriptioncreateemail.md)  | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [models.SubscriptionsCreateSecurity](../../subscriptionscreatesecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.SubscriptionOutput](../../models/subscriptionoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_import

Import subscriptions from a CSV file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.subscriptions_import(security=polar_sh.SubscriptionsImportSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
    "organization_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [models.BodySubscriptionsImport](../../models/bodysubscriptionsimport.md)  | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [models.SubscriptionsImportSecurity](../../subscriptionsimportsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.SubscriptionsImported](../../models/subscriptionsimported.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_export

Export subscriptions as a CSV file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.subscriptions_export(security=polar_sh.SubscriptionsExportSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.SubscriptionsExportSecurity](../../models/subscriptionsexportsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `organization_id`                                                                 | [OptionalNullable[models.OrganizationID]](../../models/organizationid.md)         | :heavy_minus_sign:                                                                | Filter by organization ID.                                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_list

List articles.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_list(security=polar_sh.ArticlesListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ArticlesListRequest](../../models/articleslistrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.ArticlesListSecurity](../../articleslistsecurity.md)        | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceArticle](../../models/listresourcearticle.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_create

Create an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_create(security=polar_sh.ArticlesCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "title": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ArticleCreate](../../models/articlecreate.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.ArticlesCreateSecurity](../../articlescreatesecurity.md)    | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Article](../../models/article.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_get

Get an article by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_get(security=polar_sh.ArticlesGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ArticlesGetSecurity](../../models/articlesgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Article](../../models/article.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_delete

Delete an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.documented.articles_delete(security=polar_sh.ArticlesDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ArticlesDeleteSecurity](../../models/articlesdeletesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_update

Update an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_update(security=polar_sh.ArticlesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", article_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ArticlesUpdateSecurity](../../models/articlesupdatesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `article_update`                                                        | [models.ArticleUpdate](../../models/articleupdate.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.Article](../../models/article.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_get_receivers

Get number of potential receivers for an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_get_receivers(security=polar_sh.ArticlesGetReceiversSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.ArticlesGetReceiversSecurity](../../models/articlesgetreceiverssecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ArticleReceivers](../../models/articlereceivers.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_send_preview

Send an article preview by email.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_send_preview(security=polar_sh.ArticlesSendPreviewSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", article_preview={
    "email": "Emily_Ryan@hotmail.com",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.ArticlesSendPreviewSecurity](../../models/articlessendpreviewsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `article_preview`                                                                 | [models.ArticlePreview](../../models/articlepreview.md)                           | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## articles_send

Send an article by email to all subscribers.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.articles_send(security=polar_sh.ArticlesSendSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ArticlesSendSecurity](../../models/articlessendsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## advertisements_list

List active advertisement campaigns for a benefit.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.advertisements_list(benefit_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `benefit_id`                                                                                                                                                            | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | [OptionalNullable[models.AdvertisementsListQueryParamSorting]](../../models/advertisementslistqueryparamsorting.md)                                                     | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.AdvertisementCampaignListResource](../../models/advertisementcampaignlistresource.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## advertisements_get

Get an advertisement campaign by ID.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.advertisements_get(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The advertisement campaign ID.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AdvertisementCampaign](../../models/advertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_list_clients

List OAuth2 clients.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.oauth2_list_clients(security=polar_sh.Oauth2ListClientsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.Oauth2ListClientsSecurity](../../models/oauth2listclientssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `page`                                                                        | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | Page number, defaults to 1.                                                   |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | Size of a page, defaults to 10. Maximum is 100.                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ListResourceOAuth2Client](../../models/listresourceoauth2client.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_create_client

Create an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.oauth2_oauth2_create_client(security=polar_sh.Oauth2Oauth2CreateClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "redirect_uris": [
        "https://showy-food.com",
    ],
    "client_name": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [models.OAuth2ClientConfiguration](../../models/oauth2clientconfiguration.md)        | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [models.Oauth2Oauth2CreateClientSecurity](../../oauth2oauth2createclientsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_get_client

Get an OAuth2 client by Client ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.oauth2_oauth2_get_client(security=polar_sh.Oauth2Oauth2GetClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.Oauth2Oauth2GetClientSecurity](../../models/oauth2oauth2getclientsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `client_id`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_update_client

Update an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.oauth2_oauth2_update_client(security=polar_sh.Oauth2Oauth2UpdateClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>", o_auth2_client_configuration_update={
    "redirect_uris": [
        "http://assured-generosity.net",
    ],
    "client_name": "<value>",
    "client_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.Oauth2Oauth2UpdateClientSecurity](../../models/oauth2oauth2updateclientsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `client_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `o_auth2_client_configuration_update`                                                       | [models.OAuth2ClientConfigurationUpdate](../../models/oauth2clientconfigurationupdate.md)   | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_delete_client

Delete an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.oauth2_oauth2_delete_client(security=polar_sh.Oauth2Oauth2DeleteClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.Oauth2Oauth2DeleteClientSecurity](../../models/oauth2oauth2deleteclientsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `client_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_authorize

Authorize

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.oauth2_authorize(security=polar_sh.Oauth2AuthorizeSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.Oauth2AuthorizeSecurity](../../oauth2authorizesecurity.md)  | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Oauth2AuthorizeResponseOauth2Authorize](../../models/oauth2authorizeresponseoauth2authorize.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_request_token

Request an access token using a valid grant.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.oauth2_request_token(request={
    "client_id": "<value>",
    "client_secret": "<value>",
    "refresh_token": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.Oauth2RequestTokenRequestBody](../../models/oauth2requesttokenrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_revoke_token

Revoke an access token or a refresh token.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.oauth2_revoke_token(request={
    "token": "<value>",
    "client_id": "<value>",
    "client_secret": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.Oauth2RevokeTokenRevokeTokenRequest](../../models/oauth2revoketokenrevoketokenrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.RevokeTokenResponse](../../models/revoketokenresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_introspect_token

Get information about an access token.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.oauth2_introspect_token(request={
    "token": "<value>",
    "client_id": "<value>",
    "client_secret": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [models.Oauth2IntrospectTokenIntrospectTokenRequest](../../models/oauth2introspecttokenintrospecttokenrequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.IntrospectTokenResponse](../../models/introspecttokenresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_userinfo

Get information about the authenticated user.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.oauth2_userinfo()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Oauth2UserinfoResponseOauth2Userinfo](../../models/oauth2userinforesponseoauth2userinfo.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## benefits_list

List benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.benefits_list(security=polar_sh.BenefitsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                        | [models.BenefitsListSecurity](../../models/benefitslistsecurity.md)                                                               | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `organization_id`                                                                                                                 | [OptionalNullable[models.BenefitsListQueryParamOrganizationIDFilter]](../../models/benefitslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                                | Filter by organization ID.                                                                                                        |
| `type`                                                                                                                            | [OptionalNullable[models.QueryParamBenefitTypeFilter]](../../models/queryparambenefittypefilter.md)                               | :heavy_minus_sign:                                                                                                                | Filter by benefit type.                                                                                                           |
| `page`                                                                                                                            | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Page number, defaults to 1.                                                                                                       |
| `limit`                                                                                                                           | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Size of a page, defaults to 10. Maximum is 100.                                                                                   |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadables](../../models/listresourceunionbenefitarticlesbenefitadsbenefitcustombenefitdiscordbenefitgithubrepositorybenefitdownloadables.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## benefits_create

Create a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.benefits_create(security=polar_sh.BenefitsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "description": "Customer-focused client-driven groupware",
    "is_tax_applicable": False,
    "properties": {
        "note": "<value>",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.BenefitsCreateBenefitCreate](../../models/benefitscreatebenefitcreate.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `security`                                                                        | [models.BenefitsCreateSecurity](../../benefitscreatesecurity.md)                  | :heavy_check_mark:                                                                | The security requirements to use for the request.                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.BenefitsCreateResponseBenefitsCreate](../../models/benefitscreateresponsebenefitscreate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## benefits_get

Get a benefit by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.benefits_get(security=polar_sh.BenefitsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.BenefitsGetSecurity](../../models/benefitsgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BenefitsGetResponseBenefitsGet](../../models/benefitsgetresponsebenefitsget.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## benefits_delete

Delete a benefit.

> [!WARNING]
> Every grants associated with the benefit will be revoked.
> Users will lose access to the benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.documented.benefits_delete(security=polar_sh.BenefitsDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.BenefitsDeleteSecurity](../../models/benefitsdeletesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## benefits_update

Update a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.benefits_update(security=polar_sh.BenefitsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.BenefitsUpdateSecurity](../../models/benefitsupdatesecurity.md)           | :heavy_check_mark:                                                                | N/A                                                                               |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `request_body`                                                                    | [models.BenefitsUpdateBenefitUpdate](../../models/benefitsupdatebenefitupdate.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.BenefitsUpdateResponseBenefitsUpdate](../../models/benefitsupdateresponsebenefitsupdate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## benefits_list_grants

List the individual grants for a benefit.

It's especially useful to check if a user has been granted a benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.benefits_list_grants(security=polar_sh.BenefitsListGrantsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.BenefitsListGrantsRequest](../../models/benefitslistgrantsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `security`                                                                    | [models.BenefitsListGrantsSecurity](../../benefitslistgrantssecurity.md)      | :heavy_check_mark:                                                            | The security requirements to use for the request.                             |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ListResourceBenefitGrant](../../models/listresourcebenefitgrant.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_list

List products.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.products_list(security=polar_sh.ProductsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ProductsListRequest](../../models/productslistrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.ProductsListSecurity](../../productslistsecurity.md)        | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceProduct](../../models/listresourceproduct.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_create

Create a product.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.products_create(security=polar_sh.ProductsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "name": "<value>",
    "prices": [
        {
            "recurring_interval": polar_sh.ProductPriceRecurringInterval.YEAR,
            "price_amount": 978594,
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.ProductsCreateProductCreate](../../models/productscreateproductcreate.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `security`                                                                        | [models.ProductsCreateSecurity](../../productscreatesecurity.md)                  | :heavy_check_mark:                                                                | The security requirements to use for the request.                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_get

Get a product by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.products_get(security=polar_sh.ProductsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ProductsGetSecurity](../../models/productsgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_update

Update a product.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.products_update(security=polar_sh.ProductsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", product_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ProductsUpdateSecurity](../../models/productsupdatesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `product_update`                                                        | [models.ProductUpdate](../../models/productupdate.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## products_update_benefits

Update benefits granted by a product.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.products_update_benefits(security=polar_sh.ProductsUpdateBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", product_benefits_update={
    "benefits": [
        "<value>",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.ProductsUpdateBenefitsSecurity](../../models/productsupdatebenefitssecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `product_benefits_update`                                                               | [models.ProductBenefitsUpdate](../../models/productbenefitsupdate.md)                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ProductOutput](../../models/productoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## orders_list

List orders.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.orders_list(security=polar_sh.OrdersListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.OrdersListRequest](../../models/orderslistrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.OrdersListSecurity](../../orderslistsecurity.md)            | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceOrder](../../models/listresourceorder.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## orders_get

Get an order by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.orders_get(security=polar_sh.OrdersGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.OrdersGetSecurity](../../models/ordersgetsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrderOutput](../../models/orderoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## orders_get_invoice

Get an order's invoice data.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.orders_get_invoice(security=polar_sh.OrdersGetInvoiceSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.OrdersGetInvoiceSecurity](../../models/ordersgetinvoicesecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The order ID.                                                               |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.OrderInvoice](../../models/orderinvoice.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## checkouts_create

Create a checkout session.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.checkouts_create(security=polar_sh.CheckoutsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "product_price_id": "<value>",
    "success_url": "http://unsung-scow.com",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CheckoutCreate](../../models/checkoutcreate.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.CheckoutsCreateSecurity](../../checkoutscreatesecurity.md)  | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Checkout](../../models/checkout.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## checkouts_get

Get an active checkout session by ID.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.documented.checkouts_get(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Checkout](../../models/checkout.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## files_list

List files.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.files_list(security=polar_sh.FilesListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.FilesListSecurity](../../models/fileslistsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `organization_id`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ids`                                                               | List[*str*]                                                         | :heavy_minus_sign:                                                  | List of file IDs to get.                                            |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number, defaults to 1.                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Size of a page, defaults to 10. Maximum is 100.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchema](../../models/listresourceannotateduniondownloadablefilereadproductmediafilereadorganizationavatarfilereaddiscriminatormergejsonschema.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## files_create

Create a file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.files_create(security=polar_sh.FilesCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "name": "<value>",
    "mime_type": "<value>",
    "size": 4212,
    "upload": {
        "parts": [
            {
                "number": 369186,
                "chunk_start": 547093,
                "chunk_end": 85233,
            },
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.FilesCreateFileCreate](../../models/filescreatefilecreate.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `security`                                                            | [models.FilesCreateSecurity](../../filescreatesecurity.md)            | :heavy_check_mark:                                                    | The security requirements to use for the request.                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.FileUpload](../../models/fileupload.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## files_uploaded

Complete a file upload.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.files_uploaded(security=polar_sh.FilesUploadedSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", file_upload_completed={
    "id": "<id>",
    "path": "/private/tmp",
    "parts": [
        {
            "number": 944087,
            "checksum_etag": "<value>",
            "checksum_sha256_base64": "<value>",
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.FilesUploadedSecurity](../../models/filesuploadedsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | The file ID.                                                          |
| `file_upload_completed`                                               | [models.FileUploadCompleted](../../models/fileuploadcompleted.md)     | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.FilesUploadedResponseFilesUploaded](../../models/filesuploadedresponsefilesuploaded.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## files_delete

Delete a file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.documented.files_delete(security=polar_sh.FilesDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.FilesDeleteSecurity](../../models/filesdeletesecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.FileNotFound        | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## files_update

Update a file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.files_update(security=polar_sh.FilesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", file_patch={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.FilesUpdateSecurity](../../models/filesupdatesecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The file ID.                                                        |
| `file_patch`                                                        | [models.FilePatch](../../models/filepatch.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesUpdateResponseFilesUpdate](../../models/filesupdateresponsefilesupdate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## metrics_get

Get metrics about your orders and subscriptions.

### Example Usage

```python
import dateutil.parser
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.metrics_get(security=polar_sh.MetricsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "start_date": dateutil.parser.parse("2022-03-06").date(),
    "end_date": dateutil.parser.parse("2022-01-25").date(),
    "interval": polar_sh.Interval.DAY,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MetricsGetRequest](../../models/metricsgetrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.MetricsGetSecurity](../../metricsgetsecurity.md)            | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsResponse](../../models/metricsresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## metrics_get_limits

Get the interval limits for the metrics endpoint.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.documented.metrics_get_limits(security=polar_sh.MetricsGetLimitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `security`                                                           | [models.MetricsGetLimitsSecurity](../../metricsgetlimitssecurity.md) | :heavy_check_mark:                                                   | The security requirements to use for the request.                    |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.MetricsLimits](../../models/metricslimits.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
