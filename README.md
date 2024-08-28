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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break

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
        while True:
            # handle items
    
            res = res.Next()
            if res is None:
                break

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

### [external_organizations](docs/sdks/externalorganizations/README.md)

* [list](docs/sdks/externalorganizations/README.md#list) - List External Organizations

### [repositories](docs/sdks/repositories/README.md)

* [list](docs/sdks/repositories/README.md#list) - List Repositories
* [retrieve](docs/sdks/repositories/README.md#retrieve) - Get Repository
* [update](docs/sdks/repositories/README.md#update) - Update Repository

### [organizations](docs/sdks/organizations/README.md)

* [list](docs/sdks/organizations/README.md#list) - List Organizations
* [create](docs/sdks/organizations/README.md#create) - Create Organization
* [retrieve](docs/sdks/organizations/README.md#retrieve) - Get Organization
* [update](docs/sdks/organizations/README.md#update) - Update Organization
* [organizations_list_organization_customers](docs/sdks/organizations/README.md#organizations_list_organization_customers) - List Organization Customers

### [subscriptions](docs/sdks/subscriptions/README.md)

* [list](docs/sdks/subscriptions/README.md#list) - List Subscriptions
* [create](docs/sdks/subscriptions/README.md#create) - Create Free Subscription
* [subscriptions_import](docs/sdks/subscriptions/README.md#subscriptions_import) - Import Subscriptions
* [subscriptions_export](docs/sdks/subscriptions/README.md#subscriptions_export) - Export Subscriptions

### [articles](docs/sdks/articles/README.md)

* [list](docs/sdks/articles/README.md#list) - List Articles
* [create](docs/sdks/articles/README.md#create) - Create Article
* [retrieve](docs/sdks/articles/README.md#retrieve) - Get Article
* [delete](docs/sdks/articles/README.md#delete) - Delete Article
* [update](docs/sdks/articles/README.md#update) - Update Article
* [articles_get_receivers](docs/sdks/articles/README.md#articles_get_receivers) - Get Article Receivers Count
* [articles_send_preview](docs/sdks/articles/README.md#articles_send_preview) - Send Article Preview
* [articles_send](docs/sdks/articles/README.md#articles_send) - Send Article

### [advertisements](docs/sdks/advertisements/README.md)

* [list](docs/sdks/advertisements/README.md#list) - List Campaigns
* [retrieve](docs/sdks/advertisements/README.md#retrieve) - Get Campaign

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

* [list](docs/sdks/benefits/README.md#list) - List Benefits
* [create](docs/sdks/benefits/README.md#create) - Create Benefit
* [retrieve](docs/sdks/benefits/README.md#retrieve) - Get Benefit
* [delete](docs/sdks/benefits/README.md#delete) - Delete Benefit
* [update](docs/sdks/benefits/README.md#update) - Update Benefit
* [benefits_list_grants](docs/sdks/benefits/README.md#benefits_list_grants) - List Benefit Grants

### [products](docs/sdks/products/README.md)

* [list](docs/sdks/products/README.md#list) - List Products
* [create](docs/sdks/products/README.md#create) - Create Product
* [retrieve](docs/sdks/products/README.md#retrieve) - Get Product
* [update](docs/sdks/products/README.md#update) - Update Product
* [products_update_benefits](docs/sdks/products/README.md#products_update_benefits) - Update Product Benefits

### [orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - List Orders
* [retrieve](docs/sdks/orders/README.md#retrieve) - Get Order
* [orders_get_invoice](docs/sdks/orders/README.md#orders_get_invoice) - Get Order Invoice

### [checkouts](docs/sdks/checkouts/README.md)

* [create](docs/sdks/checkouts/README.md#create) - Create Checkout
* [retrieve](docs/sdks/checkouts/README.md#retrieve) - Get Checkout

### [files](docs/sdks/files/README.md)

* [list](docs/sdks/files/README.md#list) - List Files
* [create](docs/sdks/files/README.md#create) - Create File
* [files_uploaded](docs/sdks/files/README.md#files_uploaded) - Complete File Upload
* [delete](docs/sdks/files/README.md#delete) - Delete File
* [update](docs/sdks/files/README.md#update) - Update File

### [metrics](docs/sdks/metricssdk/README.md)

* [retrieve](docs/sdks/metricssdk/README.md#retrieve) - Get Metrics
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


res = s.subscriptions.subscriptions_import(security=polar_sh.SubscriptionsImportSecurity(
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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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


res = s.advertisements.list(benefit_id="<value>")

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


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

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```
<!-- End Pagination [pagination] -->

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
