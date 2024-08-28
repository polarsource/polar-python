# polar-sh

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=polar-sh&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasy.com/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasy.com/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+<UNSET>.git
```

Poetry
```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import polar_sh
from polar_sh import Polar

async def main():
    s = Polar()
    res = await s.users.users_list_benefits_async(security=polar_sh.UsersListBenefitsSecurity(
        open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
    ))
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [users](docs/sdks/users/README.md)

* [users_list_benefits](docs/sdks/users/README.md#users_list_benefits) - List Benefits
* [users_get_benefit](docs/sdks/users/README.md#users_get_benefit) - Get Benefit
* [users_list_orders](docs/sdks/users/README.md#users_list_orders) - List Orders
* [users_get_order](docs/sdks/users/README.md#users_get_order) - Get Order
* [users_get_order_invoice](docs/sdks/users/README.md#users_get_order_invoice) - Get Order Invoice
* [users_list_subscriptions](docs/sdks/users/README.md#users_list_subscriptions) - List Subscriptions
* [users_create_subscription](docs/sdks/users/README.md#users_create_subscription) - Create Subscription
* [users_get_subscription](docs/sdks/users/README.md#users_get_subscription) - Get Subscription
* [users_cancel_subscription](docs/sdks/users/README.md#users_cancel_subscription) - Cancel Subscription
* [users_update_subscription](docs/sdks/users/README.md#users_update_subscription) - Update Subscription
* [users_list_advertisement_campaigns](docs/sdks/users/README.md#users_list_advertisement_campaigns) - List Advertisement Campaigns
* [users_create_advertisement_campaign](docs/sdks/users/README.md#users_create_advertisement_campaign) - Create Advertisement Campaign
* [users_get_advertisement_campaign](docs/sdks/users/README.md#users_get_advertisement_campaign) - Get Advertisement Campaign
* [users_delete_advertisement_campaign](docs/sdks/users/README.md#users_delete_advertisement_campaign) - Delete Advertisement Campaign
* [users_update_advertisement_campaign](docs/sdks/users/README.md#users_update_advertisement_campaign) - Update Advertisement Campaign
* [users_enable_advertisement_campaign](docs/sdks/users/README.md#users_enable_advertisement_campaign) - Enable Advertisement Campaign
* [users_list_downloadables](docs/sdks/users/README.md#users_list_downloadables) - List Downloadables
* [users_get_downloadable](docs/sdks/users/README.md#users_get_downloadable) - Get Downloadable

### [documented](docs/sdks/documented/README.md)

* [users_list_benefits](docs/sdks/documented/README.md#users_list_benefits) - List Benefits
* [users_get_benefit](docs/sdks/documented/README.md#users_get_benefit) - Get Benefit
* [users_list_orders](docs/sdks/documented/README.md#users_list_orders) - List Orders
* [users_get_order](docs/sdks/documented/README.md#users_get_order) - Get Order
* [users_get_order_invoice](docs/sdks/documented/README.md#users_get_order_invoice) - Get Order Invoice
* [users_list_subscriptions](docs/sdks/documented/README.md#users_list_subscriptions) - List Subscriptions
* [users_create_subscription](docs/sdks/documented/README.md#users_create_subscription) - Create Subscription
* [users_get_subscription](docs/sdks/documented/README.md#users_get_subscription) - Get Subscription
* [users_cancel_subscription](docs/sdks/documented/README.md#users_cancel_subscription) - Cancel Subscription
* [users_update_subscription](docs/sdks/documented/README.md#users_update_subscription) - Update Subscription
* [users_list_advertisement_campaigns](docs/sdks/documented/README.md#users_list_advertisement_campaigns) - List Advertisement Campaigns
* [users_create_advertisement_campaign](docs/sdks/documented/README.md#users_create_advertisement_campaign) - Create Advertisement Campaign
* [users_get_advertisement_campaign](docs/sdks/documented/README.md#users_get_advertisement_campaign) - Get Advertisement Campaign
* [users_delete_advertisement_campaign](docs/sdks/documented/README.md#users_delete_advertisement_campaign) - Delete Advertisement Campaign
* [users_update_advertisement_campaign](docs/sdks/documented/README.md#users_update_advertisement_campaign) - Update Advertisement Campaign
* [users_enable_advertisement_campaign](docs/sdks/documented/README.md#users_enable_advertisement_campaign) - Enable Advertisement Campaign
* [users_list_downloadables](docs/sdks/documented/README.md#users_list_downloadables) - List Downloadables
* [users_get_downloadable](docs/sdks/documented/README.md#users_get_downloadable) - Get Downloadable
* [external_organizations_list](docs/sdks/documented/README.md#external_organizations_list) - List External Organizations
* [repositories_list](docs/sdks/documented/README.md#repositories_list) - List Repositories
* [repositories_get](docs/sdks/documented/README.md#repositories_get) - Get Repository
* [repositories_update](docs/sdks/documented/README.md#repositories_update) - Update Repository
* [organizations_list](docs/sdks/documented/README.md#organizations_list) - List Organizations
* [organizations_create](docs/sdks/documented/README.md#organizations_create) - Create Organization
* [organizations_get](docs/sdks/documented/README.md#organizations_get) - Get Organization
* [organizations_update](docs/sdks/documented/README.md#organizations_update) - Update Organization
* [organizations_list_organization_customers](docs/sdks/documented/README.md#organizations_list_organization_customers) - List Organization Customers
* [subscriptions_list](docs/sdks/documented/README.md#subscriptions_list) - List Subscriptions
* [subscriptions_create](docs/sdks/documented/README.md#subscriptions_create) - Create Free Subscription
* [subscriptions_import](docs/sdks/documented/README.md#subscriptions_import) - Import Subscriptions
* [subscriptions_export](docs/sdks/documented/README.md#subscriptions_export) - Export Subscriptions
* [articles_list](docs/sdks/documented/README.md#articles_list) - List Articles
* [articles_create](docs/sdks/documented/README.md#articles_create) - Create Article
* [articles_get](docs/sdks/documented/README.md#articles_get) - Get Article
* [articles_delete](docs/sdks/documented/README.md#articles_delete) - Delete Article
* [articles_update](docs/sdks/documented/README.md#articles_update) - Update Article
* [articles_get_receivers](docs/sdks/documented/README.md#articles_get_receivers) - Get Article Receivers Count
* [articles_send_preview](docs/sdks/documented/README.md#articles_send_preview) - Send Article Preview
* [articles_send](docs/sdks/documented/README.md#articles_send) - Send Article
* [advertisements_list](docs/sdks/documented/README.md#advertisements_list) - List Campaigns
* [advertisements_get](docs/sdks/documented/README.md#advertisements_get) - Get Campaign
* [oauth2_list_clients](docs/sdks/documented/README.md#oauth2_list_clients) - List Clients
* [oauth2_oauth2_create_client](docs/sdks/documented/README.md#oauth2_oauth2_create_client) - Create Client
* [oauth2_oauth2_get_client](docs/sdks/documented/README.md#oauth2_oauth2_get_client) - Get Client
* [oauth2_oauth2_update_client](docs/sdks/documented/README.md#oauth2_oauth2_update_client) - Update Client
* [oauth2_oauth2_delete_client](docs/sdks/documented/README.md#oauth2_oauth2_delete_client) - Delete Client
* [oauth2_authorize](docs/sdks/documented/README.md#oauth2_authorize) - Authorize
* [oauth2_request_token](docs/sdks/documented/README.md#oauth2_request_token) - Request Token
* [oauth2_revoke_token](docs/sdks/documented/README.md#oauth2_revoke_token) - Revoke Token
* [oauth2_introspect_token](docs/sdks/documented/README.md#oauth2_introspect_token) - Introspect Token
* [oauth2_userinfo](docs/sdks/documented/README.md#oauth2_userinfo) - Get User Info
* [benefits_list](docs/sdks/documented/README.md#benefits_list) - List Benefits
* [benefits_create](docs/sdks/documented/README.md#benefits_create) - Create Benefit
* [benefits_get](docs/sdks/documented/README.md#benefits_get) - Get Benefit
* [benefits_delete](docs/sdks/documented/README.md#benefits_delete) - Delete Benefit
* [benefits_update](docs/sdks/documented/README.md#benefits_update) - Update Benefit
* [benefits_list_grants](docs/sdks/documented/README.md#benefits_list_grants) - List Benefit Grants
* [products_list](docs/sdks/documented/README.md#products_list) - List Products
* [products_create](docs/sdks/documented/README.md#products_create) - Create Product
* [products_get](docs/sdks/documented/README.md#products_get) - Get Product
* [products_update](docs/sdks/documented/README.md#products_update) - Update Product
* [products_update_benefits](docs/sdks/documented/README.md#products_update_benefits) - Update Product Benefits
* [orders_list](docs/sdks/documented/README.md#orders_list) - List Orders
* [orders_get](docs/sdks/documented/README.md#orders_get) - Get Order
* [orders_get_invoice](docs/sdks/documented/README.md#orders_get_invoice) - Get Order Invoice
* [checkouts_create](docs/sdks/documented/README.md#checkouts_create) - Create Checkout
* [checkouts_get](docs/sdks/documented/README.md#checkouts_get) - Get Checkout
* [files_list](docs/sdks/documented/README.md#files_list) - List Files
* [files_create](docs/sdks/documented/README.md#files_create) - Create File
* [files_uploaded](docs/sdks/documented/README.md#files_uploaded) - Complete File Upload
* [files_delete](docs/sdks/documented/README.md#files_delete) - Delete File
* [files_update](docs/sdks/documented/README.md#files_update) - Update File
* [metrics_get](docs/sdks/documented/README.md#metrics_get) - Get Metrics
* [metrics_get_limits](docs/sdks/documented/README.md#metrics_get_limits) - Get Metrics Limits

### [featured](docs/sdks/featured/README.md)

* [users_list_benefits](docs/sdks/featured/README.md#users_list_benefits) - List Benefits
* [users_get_benefit](docs/sdks/featured/README.md#users_get_benefit) - Get Benefit
* [users_list_orders](docs/sdks/featured/README.md#users_list_orders) - List Orders
* [users_get_order](docs/sdks/featured/README.md#users_get_order) - Get Order
* [users_get_order_invoice](docs/sdks/featured/README.md#users_get_order_invoice) - Get Order Invoice
* [users_list_subscriptions](docs/sdks/featured/README.md#users_list_subscriptions) - List Subscriptions
* [users_create_subscription](docs/sdks/featured/README.md#users_create_subscription) - Create Subscription
* [users_get_subscription](docs/sdks/featured/README.md#users_get_subscription) - Get Subscription
* [users_cancel_subscription](docs/sdks/featured/README.md#users_cancel_subscription) - Cancel Subscription
* [users_update_subscription](docs/sdks/featured/README.md#users_update_subscription) - Update Subscription
* [users_list_downloadables](docs/sdks/featured/README.md#users_list_downloadables) - List Downloadables
* [users_get_downloadable](docs/sdks/featured/README.md#users_get_downloadable) - Get Downloadable
* [organizations_list](docs/sdks/featured/README.md#organizations_list) - List Organizations
* [organizations_create](docs/sdks/featured/README.md#organizations_create) - Create Organization
* [organizations_get](docs/sdks/featured/README.md#organizations_get) - Get Organization
* [organizations_update](docs/sdks/featured/README.md#organizations_update) - Update Organization
* [articles_list](docs/sdks/featured/README.md#articles_list) - List Articles
* [articles_create](docs/sdks/featured/README.md#articles_create) - Create Article
* [articles_get](docs/sdks/featured/README.md#articles_get) - Get Article
* [articles_delete](docs/sdks/featured/README.md#articles_delete) - Delete Article
* [articles_update](docs/sdks/featured/README.md#articles_update) - Update Article
* [articles_get_receivers](docs/sdks/featured/README.md#articles_get_receivers) - Get Article Receivers Count
* [articles_send_preview](docs/sdks/featured/README.md#articles_send_preview) - Send Article Preview
* [articles_send](docs/sdks/featured/README.md#articles_send) - Send Article
* [oauth2_request_token](docs/sdks/featured/README.md#oauth2_request_token) - Request Token
* [oauth2_revoke_token](docs/sdks/featured/README.md#oauth2_revoke_token) - Revoke Token
* [oauth2_introspect_token](docs/sdks/featured/README.md#oauth2_introspect_token) - Introspect Token
* [oauth2_userinfo](docs/sdks/featured/README.md#oauth2_userinfo) - Get User Info
* [products_list](docs/sdks/featured/README.md#products_list) - List Products
* [products_create](docs/sdks/featured/README.md#products_create) - Create Product
* [products_get](docs/sdks/featured/README.md#products_get) - Get Product
* [products_update](docs/sdks/featured/README.md#products_update) - Update Product
* [products_update_benefits](docs/sdks/featured/README.md#products_update_benefits) - Update Product Benefits
* [checkouts_create](docs/sdks/featured/README.md#checkouts_create) - Create Checkout
* [checkouts_get](docs/sdks/featured/README.md#checkouts_get) - Get Checkout

### [funding](docs/sdks/fundingsdk/README.md)

* [funding_search](docs/sdks/fundingsdk/README.md#funding_search) - Search
* [funding_lookup](docs/sdks/fundingsdk/README.md#funding_lookup) - Lookup

### [external_organizations](docs/sdks/externalorganizations/README.md)

* [external_organizations_list](docs/sdks/externalorganizations/README.md#external_organizations_list) - List External Organizations

### [issue_funding](docs/sdks/issuefundingsdk/README.md)

* [external_organizations_list](docs/sdks/issuefundingsdk/README.md#external_organizations_list) - List External Organizations
* [repositories_list](docs/sdks/issuefundingsdk/README.md#repositories_list) - List Repositories
* [repositories_get](docs/sdks/issuefundingsdk/README.md#repositories_get) - Get Repository
* [repositories_update](docs/sdks/issuefundingsdk/README.md#repositories_update) - Update Repository

### [repositories](docs/sdks/repositories/README.md)

* [repositories_list](docs/sdks/repositories/README.md#repositories_list) - List Repositories
* [repositories_get](docs/sdks/repositories/README.md#repositories_get) - Get Repository
* [repositories_update](docs/sdks/repositories/README.md#repositories_update) - Update Repository

### [rewards](docs/sdks/rewards/README.md)

* [rewards_search](docs/sdks/rewards/README.md#rewards_search) - Search rewards
* [rewards_summary](docs/sdks/rewards/README.md#rewards_summary) - Get rewards summary

### [pull_requests](docs/sdks/pullrequests/README.md)

* [pull_requests_search](docs/sdks/pullrequests/README.md#pull_requests_search) - Search pull requests

### [accounts](docs/sdks/accounts/README.md)

* [accounts_search](docs/sdks/accounts/README.md#accounts_search) - Search
* [accounts_get](docs/sdks/accounts/README.md#accounts_get) - Get
* [accounts_onboarding_link](docs/sdks/accounts/README.md#accounts_onboarding_link) - Onboarding Link
* [accounts_dashboard_link](docs/sdks/accounts/README.md#accounts_dashboard_link) - Dashboard Link
* [accounts_create](docs/sdks/accounts/README.md#accounts_create) - Create

### [issues](docs/sdks/issues/README.md)

* [issues_list](docs/sdks/issues/README.md#issues_list) - List Issues
* [issues_lookup](docs/sdks/issues/README.md#issues_lookup) - Lookup
* [issues_get_body](docs/sdks/issues/README.md#issues_get_body) - Get Body
* [issues_get](docs/sdks/issues/README.md#issues_get) - Get issue
* [issues_update](docs/sdks/issues/README.md#issues_update) - Update issue.
* [issues_confirm](docs/sdks/issues/README.md#issues_confirm) - Mark an issue as confirmed solved.

### [pledges](docs/sdks/pledges/README.md)

* [pledges_search](docs/sdks/pledges/README.md#pledges_search) - Search pledges
* [pledges_summary](docs/sdks/pledges/README.md#pledges_summary) - Get pledges summary
* [pledges_spending](docs/sdks/pledges/README.md#pledges_spending) - Get user spending
* [pledges_get](docs/sdks/pledges/README.md#pledges_get) - Get pledge

### [organizations](docs/sdks/organizations/README.md)

* [organizations_list](docs/sdks/organizations/README.md#organizations_list) - List Organizations
* [organizations_create](docs/sdks/organizations/README.md#organizations_create) - Create Organization
* [organizations_get](docs/sdks/organizations/README.md#organizations_get) - Get Organization
* [organizations_update](docs/sdks/organizations/README.md#organizations_update) - Update Organization
* [organizations_list_organization_customers](docs/sdks/organizations/README.md#organizations_list_organization_customers) - List Organization Customers

### [subscriptions](docs/sdks/subscriptions/README.md)

* [subscriptions_list](docs/sdks/subscriptions/README.md#subscriptions_list) - List Subscriptions
* [subscriptions_create](docs/sdks/subscriptions/README.md#subscriptions_create) - Create Free Subscription
* [subscriptions_import](docs/sdks/subscriptions/README.md#subscriptions_import) - Import Subscriptions
* [subscriptions_export](docs/sdks/subscriptions/README.md#subscriptions_export) - Export Subscriptions

### [articles](docs/sdks/articles/README.md)

* [articles_list](docs/sdks/articles/README.md#articles_list) - List Articles
* [articles_create](docs/sdks/articles/README.md#articles_create) - Create Article
* [articles_get](docs/sdks/articles/README.md#articles_get) - Get Article
* [articles_delete](docs/sdks/articles/README.md#articles_delete) - Delete Article
* [articles_update](docs/sdks/articles/README.md#articles_update) - Update Article
* [articles_get_receivers](docs/sdks/articles/README.md#articles_get_receivers) - Get Article Receivers Count
* [articles_send_preview](docs/sdks/articles/README.md#articles_send_preview) - Send Article Preview
* [articles_send](docs/sdks/articles/README.md#articles_send) - Send Article

### [transactions](docs/sdks/transactions/README.md)

* [transactions_search_transactions](docs/sdks/transactions/README.md#transactions_search_transactions) - Search Transactions
* [transactions_lookup_transaction](docs/sdks/transactions/README.md#transactions_lookup_transaction) - Lookup Transaction
* [transactions_get_summary](docs/sdks/transactions/README.md#transactions_get_summary) - Get Summary
* [transactions_get_payout_estimate](docs/sdks/transactions/README.md#transactions_get_payout_estimate) - Get Payout Estimate
* [transactions_create_payout](docs/sdks/transactions/README.md#transactions_create_payout) - Create Payout
* [transactions_get_payout_csv](docs/sdks/transactions/README.md#transactions_get_payout_csv) - Get Payout Csv

### [advertisements](docs/sdks/advertisements/README.md)

* [advertisements_list](docs/sdks/advertisements/README.md#advertisements_list) - List Campaigns
* [advertisements_get](docs/sdks/advertisements/README.md#advertisements_get) - Get Campaign

### [donations](docs/sdks/donations/README.md)

* [donations_search_donations](docs/sdks/donations/README.md#donations_search_donations) - Search Donations
* [donations_create_payment_intent](docs/sdks/donations/README.md#donations_create_payment_intent) - Create Payment Intent
* [donations_update_payment_intent](docs/sdks/donations/README.md#donations_update_payment_intent) - Update Payment Intent
* [donations_statistics](docs/sdks/donations/README.md#donations_statistics) - Statistics
* [donations_donations_public_search](docs/sdks/donations/README.md#donations_donations_public_search) - Donations Public Search

### [oauth2](docs/sdks/oauth2/README.md)

* [oauth2_list_clients](docs/sdks/oauth2/README.md#oauth2_list_clients) - List Clients
* [oauth2_oauth2_create_client](docs/sdks/oauth2/README.md#oauth2_oauth2_create_client) - Create Client
* [oauth2_oauth2_get_client](docs/sdks/oauth2/README.md#oauth2_oauth2_get_client) - Get Client
* [oauth2_oauth2_update_client](docs/sdks/oauth2/README.md#oauth2_oauth2_update_client) - Update Client
* [oauth2_oauth2_delete_client](docs/sdks/oauth2/README.md#oauth2_oauth2_delete_client) - Delete Client
* [oauth2_authorize](docs/sdks/oauth2/README.md#oauth2_authorize) - Authorize
* [oauth2_request_token](docs/sdks/oauth2/README.md#oauth2_request_token) - Request Token
* [oauth2_revoke_token](docs/sdks/oauth2/README.md#oauth2_revoke_token) - Revoke Token
* [oauth2_introspect_token](docs/sdks/oauth2/README.md#oauth2_introspect_token) - Introspect Token
* [oauth2_userinfo](docs/sdks/oauth2/README.md#oauth2_userinfo) - Get User Info

### [benefits](docs/sdks/benefits/README.md)

* [benefits_list](docs/sdks/benefits/README.md#benefits_list) - List Benefits
* [benefits_create](docs/sdks/benefits/README.md#benefits_create) - Create Benefit
* [benefits_get](docs/sdks/benefits/README.md#benefits_get) - Get Benefit
* [benefits_delete](docs/sdks/benefits/README.md#benefits_delete) - Delete Benefit
* [benefits_update](docs/sdks/benefits/README.md#benefits_update) - Update Benefit
* [benefits_list_grants](docs/sdks/benefits/README.md#benefits_list_grants) - List Benefit Grants

### [webhooks](docs/sdks/webhooks/README.md)

* [webhooks_list_webhook_endpoints](docs/sdks/webhooks/README.md#webhooks_list_webhook_endpoints) - List Webhook Endpoints
* [webhooks_create_webhook_endpoint](docs/sdks/webhooks/README.md#webhooks_create_webhook_endpoint) - Create Webhook Endpoint
* [webhooks_get_webhook_endpoint](docs/sdks/webhooks/README.md#webhooks_get_webhook_endpoint) - Get Webhook Endpoint
* [webhooks_delete_webhook_endpoint](docs/sdks/webhooks/README.md#webhooks_delete_webhook_endpoint) - Delete Webhook Endpoint
* [webhooks_update_webhook_endpoint](docs/sdks/webhooks/README.md#webhooks_update_webhook_endpoint) - Update Webhook Endpoint
* [webhooks_list_webhook_deliveries](docs/sdks/webhooks/README.md#webhooks_list_webhook_deliveries) - List Webhook Deliveries
* [webhooks_redeliver_webhook_event](docs/sdks/webhooks/README.md#webhooks_redeliver_webhook_event) - Redeliver Webhook Event

### [products](docs/sdks/products/README.md)

* [products_list](docs/sdks/products/README.md#products_list) - List Products
* [products_create](docs/sdks/products/README.md#products_create) - Create Product
* [products_get](docs/sdks/products/README.md#products_get) - Get Product
* [products_update](docs/sdks/products/README.md#products_update) - Update Product
* [products_update_benefits](docs/sdks/products/README.md#products_update_benefits) - Update Product Benefits

### [orders](docs/sdks/orders/README.md)

* [orders_list](docs/sdks/orders/README.md#orders_list) - List Orders
* [orders_get](docs/sdks/orders/README.md#orders_get) - Get Order
* [orders_get_invoice](docs/sdks/orders/README.md#orders_get_invoice) - Get Order Invoice

### [checkouts](docs/sdks/checkouts/README.md)

* [checkouts_create](docs/sdks/checkouts/README.md#checkouts_create) - Create Checkout
* [checkouts_get](docs/sdks/checkouts/README.md#checkouts_get) - Get Checkout

### [files](docs/sdks/files/README.md)

* [files_list](docs/sdks/files/README.md#files_list) - List Files
* [files_create](docs/sdks/files/README.md#files_create) - Create File
* [files_uploaded](docs/sdks/files/README.md#files_uploaded) - Complete File Upload
* [files_delete](docs/sdks/files/README.md#files_delete) - Delete File
* [files_update](docs/sdks/files/README.md#files_update) - Update File

### [metrics](docs/sdks/metricssdk/README.md)

* [metrics_get](docs/sdks/metricssdk/README.md#metrics_get) - Get Metrics
* [metrics_get_limits](docs/sdks/metricssdk/README.md#metrics_get_limits) - Get Metrics Limits
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

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
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from polar.utils import BackoffStrategy, RetryConfig
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
),
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from polar.utils import BackoffStrategy, RetryConfig
import polar_sh
from polar_sh import Polar

s = Polar(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
)


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

### Example

```python
import polar_sh
from polar_sh import Polar, models

s = Polar()

res = None
try:
    res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

except models.HTTPValidationError as e:
    # handle exception
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.polar.sh` | None |

#### Example

```python
import polar_sh
from polar_sh import Polar

s = Polar(
    server_idx=0,
)


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import polar_sh
from polar_sh import Polar

s = Polar(
    server_url="https://api.polar.sh",
)


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from polar_sh import Polar
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Polar(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from polar_sh import Polar
from polar_sh.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Polar(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                     | Type                     | Scheme                   |
| ------------------------ | ------------------------ | ------------------------ |
| `open_id_connect`        | openIdConnect            | OpenID Connect Discovery |

To authenticate with the API the `open_id_connect` parameter must be set when initializing the SDK client instance. For example:
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

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
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
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from polar_sh import Polar
import logging

logging.basicConfig(level=logging.DEBUG)
s = Polar(debug_logger=logging.getLogger("polar_sh"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=polar-sh&utm_campaign=python)
