# Featured
(*featured*)

## Overview

Endpoints featured in the Polar API documentation for their interest in common use-cases.

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
* [users_list_downloadables](#users_list_downloadables) - List Downloadables
* [users_get_downloadable](#users_get_downloadable) - Get Downloadable
* [organizations_list](#organizations_list) - List Organizations
* [organizations_create](#organizations_create) - Create Organization
* [organizations_get](#organizations_get) - Get Organization
* [organizations_update](#organizations_update) - Update Organization
* [articles_list](#articles_list) - List Articles
* [articles_create](#articles_create) - Create Article
* [articles_get](#articles_get) - Get Article
* [articles_delete](#articles_delete) - Delete Article
* [articles_update](#articles_update) - Update Article
* [articles_get_receivers](#articles_get_receivers) - Get Article Receivers Count
* [articles_send_preview](#articles_send_preview) - Send Article Preview
* [articles_send](#articles_send) - Send Article
* [oauth2_request_token](#oauth2_request_token) - Request Token
* [oauth2_revoke_token](#oauth2_revoke_token) - Revoke Token
* [oauth2_introspect_token](#oauth2_introspect_token) - Introspect Token
* [oauth2_userinfo](#oauth2_userinfo) - Get User Info
* [products_list](#products_list) - List Products
* [products_create](#products_create) - Create Product
* [products_get](#products_get) - Get Product
* [products_update](#products_update) - Update Product
* [products_update_benefits](#products_update_benefits) - Update Product Benefits
* [checkouts_create](#checkouts_create) - Create Checkout
* [checkouts_get](#checkouts_get) - Get Checkout

## users_list_benefits

List my granted benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.featured.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
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


res = s.featured.users_get_benefit(security=polar_sh.UsersGetBenefitSecurity(
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


res = s.featured.users_list_orders(security=polar_sh.UsersListOrdersSecurity(
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


res = s.featured.users_get_order(security=polar_sh.UsersGetOrderSecurity(
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


res = s.featured.users_get_order_invoice(security=polar_sh.UsersGetOrderInvoiceSecurity(
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


res = s.featured.users_list_subscriptions(security=polar_sh.UsersListSubscriptionsSecurity(
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


res = s.featured.users_create_subscription(security=polar_sh.UsersCreateSubscriptionSecurity(
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


res = s.featured.users_get_subscription(security=polar_sh.UsersGetSubscriptionSecurity(
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


res = s.featured.users_cancel_subscription(security=polar_sh.UsersCancelSubscriptionSecurity(
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


res = s.featured.users_update_subscription(security=polar_sh.UsersUpdateSubscriptionSecurity(
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


## users_list_downloadables

List Downloadables

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.featured.users_list_downloadables(security=polar_sh.UsersListDownloadablesSecurity(
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


res = s.featured.users_get_downloadable(security=polar_sh.UsersGetDownloadableSecurity(
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


## organizations_list

List organizations.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.featured.organizations_list(security=polar_sh.OrganizationsListSecurity(
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


res = s.featured.organizations_create(security=polar_sh.OrganizationsCreateSecurity(
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


res = s.featured.organizations_get(security=polar_sh.OrganizationsGetSecurity(
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


res = s.featured.organizations_update(security=polar_sh.OrganizationsUpdateSecurity(
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


## articles_list

List articles.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.featured.articles_list(security=polar_sh.ArticlesListSecurity(
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


res = s.featured.articles_create(security=polar_sh.ArticlesCreateSecurity(
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


res = s.featured.articles_get(security=polar_sh.ArticlesGetSecurity(
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


s.featured.articles_delete(security=polar_sh.ArticlesDeleteSecurity(
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


res = s.featured.articles_update(security=polar_sh.ArticlesUpdateSecurity(
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


res = s.featured.articles_get_receivers(security=polar_sh.ArticlesGetReceiversSecurity(
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


res = s.featured.articles_send_preview(security=polar_sh.ArticlesSendPreviewSecurity(
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


res = s.featured.articles_send(security=polar_sh.ArticlesSendSecurity(
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


## oauth2_request_token

Request an access token using a valid grant.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.featured.oauth2_request_token(request={
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


res = s.featured.oauth2_revoke_token(request={
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


res = s.featured.oauth2_introspect_token(request={
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


res = s.featured.oauth2_userinfo()

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


## products_list

List products.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.featured.products_list(security=polar_sh.ProductsListSecurity(
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


res = s.featured.products_create(security=polar_sh.ProductsCreateSecurity(
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


res = s.featured.products_get(security=polar_sh.ProductsGetSecurity(
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


res = s.featured.products_update(security=polar_sh.ProductsUpdateSecurity(
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


res = s.featured.products_update_benefits(security=polar_sh.ProductsUpdateBenefitsSecurity(
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


## checkouts_create

Create a checkout session.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.featured.checkouts_create(security=polar_sh.CheckoutsCreateSecurity(
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


res = s.featured.checkouts_get(id="<value>")

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
