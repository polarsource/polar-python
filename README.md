# polar-sdk

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=polar-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install polar-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add polar-sdk
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
import dateutil.parser
import polar_sdk
from polar_sdk import Polar

with Polar() as polar:

    res = polar.endpointcheckout_created_post(request=polar_sdk.WebhookCheckoutCreatedPayload(
        data=polar_sdk.Checkout(
            created_at=dateutil.parser.isoparse("2024-11-12T14:26:42.882Z"),
            modified_at=dateutil.parser.isoparse("2023-05-28T05:08:06.235Z"),
            id="<value>",
            status=polar_sdk.CheckoutStatus.FAILED,
            client_secret="<value>",
            url="https://heavy-beret.com/",
            expires_at=dateutil.parser.isoparse("2022-02-25T02:26:48.460Z"),
            success_url="https://sardonic-final.info/",
            embed_origin="<value>",
            amount=962818,
            tax_amount=6400,
            currency="Yen",
            subtotal_amount=648726,
            total_amount=210702,
            product_id="<value>",
            product_price_id="<value>",
            discount_id="<value>",
            allow_discount_codes=True,
            is_discount_applicable=False,
            is_free_product_price=False,
            is_payment_required=False,
            is_payment_setup_required=False,
            is_payment_form_required=False,
            customer_id="<value>",
            customer_name="<value>",
            customer_email="Ryley_Erdman@hotmail.com",
            customer_ip_address="<value>",
            customer_billing_address={
                "country": "South Africa",
            },
            customer_tax_id="<id>",
            payment_processor_metadata={},
            metadata={
                "key": 18677,
                "key1": 95370,
            },
            product={
                "created_at": dateutil.parser.isoparse("2022-04-02T00:05:42.586Z"),
                "modified_at": dateutil.parser.isoparse("2023-12-16T03:02:38.803Z"),
                "id": "<value>",
                "name": "<value>",
                "description": "for embarrassment untidy long-term near honestly separate yet",
                "is_recurring": True,
                "is_archived": False,
                "organization_id": "<value>",
                "prices": [
                    {
                        "created_at": dateutil.parser.isoparse("2024-11-19T15:59:15.588Z"),
                        "modified_at": dateutil.parser.isoparse("2022-11-17T00:11:23.972Z"),
                        "id": "<value>",
                        "is_archived": False,
                        "product_id": "<value>",
                        "price_currency": "<value>",
                        "minimum_amount": 363560,
                        "maximum_amount": 75876,
                        "preset_amount": 82334,
                        "amount_type": polar_sdk.ProductPriceOneTimeCustomAmountType.CUSTOM,
                        "type": polar_sdk.ProductPriceOneTimeCustomType.ONE_TIME,
                    },
                ],
                "benefits": [
                    {
                        "created_at": dateutil.parser.isoparse("2023-08-22T00:47:02.059Z"),
                        "modified_at": dateutil.parser.isoparse("2023-06-04T10:32:44.101Z"),
                        "id": "<value>",
                        "type": polar_sdk.BenefitType.LICENSE_KEYS,
                        "description": "within jacket unless",
                        "selectable": False,
                        "deletable": False,
                        "organization_id": "<value>",
                    },
                ],
                "medias": [
                    {
                        "id": "<value>",
                        "organization_id": "<value>",
                        "name": "<value>",
                        "path": "/private/var",
                        "mime_type": "<value>",
                        "size": 245189,
                        "storage_version": "<value>",
                        "checksum_etag": "<value>",
                        "checksum_sha256_base64": "<value>",
                        "checksum_sha256_hex": "<value>",
                        "last_modified_at": dateutil.parser.isoparse("2022-11-03T15:00:03.276Z"),
                        "version": "<value>",
                        "is_uploaded": False,
                        "created_at": dateutil.parser.isoparse("2024-06-07T13:47:02.365Z"),
                        "size_readable": "<value>",
                        "public_url": "https://webbed-experience.name/",
                        "service": polar_sdk.Service.PRODUCT_MEDIA,
                    },
                ],
            },
            product_price={
                "created_at": dateutil.parser.isoparse("2024-02-15T09:22:19.644Z"),
                "modified_at": dateutil.parser.isoparse("2022-12-28T20:59:29.904Z"),
                "id": "<value>",
                "is_archived": False,
                "product_id": "<value>",
                "price_currency": "<value>",
                "minimum_amount": 417896,
                "maximum_amount": 962818,
                "preset_amount": 6400,
                "recurring_interval": polar_sdk.SubscriptionRecurringInterval.MONTH,
                "amount_type": polar_sdk.ProductPriceRecurringCustomAmountType.CUSTOM,
                "type": polar_sdk.ProductPriceRecurringCustomType.RECURRING,
            },
            discount={
                "duration": polar_sdk.DiscountDuration.REPEATING,
                "type": polar_sdk.DiscountType.FIXED,
                "basis_points": 341163,
                "id": "<value>",
                "name": "<value>",
                "code": "<value>",
            },
            subscription_id="<value>",
            attached_custom_fields=[
                {
                    "custom_field_id": "<value>",
                    "custom_field": {
                        "created_at": dateutil.parser.isoparse("2022-08-19T22:18:44.316Z"),
                        "modified_at": dateutil.parser.isoparse("2023-04-29T23:39:10.699Z"),
                        "id": "<value>",
                        "metadata": {
                            "key": False,
                        },
                        "slug": "<value>",
                        "name": "<value>",
                        "organization_id": "<value>",
                        "properties": {
                            "options": [
                                {
                                    "value": "<value>",
                                    "label": "<value>",
                                },
                            ],
                        },
                        "type": polar_sdk.CustomFieldSelectType.SELECT,
                    },
                    "order": 996863,
                    "required": False,
                },
                {
                    "custom_field_id": "<value>",
                    "custom_field": {
                        "created_at": dateutil.parser.isoparse("2023-07-03T09:46:29.338Z"),
                        "modified_at": dateutil.parser.isoparse("2024-01-25T18:08:49.597Z"),
                        "id": "<value>",
                        "metadata": {
                            "key": False,
                        },
                        "slug": "<value>",
                        "name": "<value>",
                        "organization_id": "<value>",
                        "properties": {},
                        "type": polar_sdk.CustomFieldNumberType.NUMBER,
                    },
                    "order": 72589,
                    "required": True,
                },
                {
                    "custom_field_id": "<value>",
                    "custom_field": {
                        "created_at": dateutil.parser.isoparse("2024-07-31T13:25:31.669Z"),
                        "modified_at": dateutil.parser.isoparse("2022-11-12T09:40:10.044Z"),
                        "id": "<value>",
                        "metadata": {
                            "key": "<value>",
                        },
                        "slug": "<value>",
                        "name": "<value>",
                        "organization_id": "<value>",
                        "properties": {},
                        "type": polar_sdk.CustomFieldTextType.TEXT,
                    },
                    "order": 161325,
                    "required": True,
                },
            ],
            payment_processor=polar_sdk.PaymentProcessor.STRIPE,
        ),
        type=polar_sdk.WebhookCheckoutCreatedPayloadType.CHECKOUT_CREATED,
    ))

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import dateutil.parser
import polar_sdk
from polar_sdk import Polar

async def main():
    async with Polar() as polar:

        res = await polar.endpointcheckout_created_post_async(request=polar_sdk.WebhookCheckoutCreatedPayload(
            data=polar_sdk.Checkout(
                created_at=dateutil.parser.isoparse("2024-11-12T14:26:42.882Z"),
                modified_at=dateutil.parser.isoparse("2023-05-28T05:08:06.235Z"),
                id="<value>",
                status=polar_sdk.CheckoutStatus.FAILED,
                client_secret="<value>",
                url="https://heavy-beret.com/",
                expires_at=dateutil.parser.isoparse("2022-02-25T02:26:48.460Z"),
                success_url="https://sardonic-final.info/",
                embed_origin="<value>",
                amount=962818,
                tax_amount=6400,
                currency="Yen",
                subtotal_amount=648726,
                total_amount=210702,
                product_id="<value>",
                product_price_id="<value>",
                discount_id="<value>",
                allow_discount_codes=True,
                is_discount_applicable=False,
                is_free_product_price=False,
                is_payment_required=False,
                is_payment_setup_required=False,
                is_payment_form_required=False,
                customer_id="<value>",
                customer_name="<value>",
                customer_email="Ryley_Erdman@hotmail.com",
                customer_ip_address="<value>",
                customer_billing_address={
                    "country": "South Africa",
                },
                customer_tax_id="<id>",
                payment_processor_metadata={},
                metadata={
                    "key": 18677,
                    "key1": 95370,
                },
                product={
                    "created_at": dateutil.parser.isoparse("2022-04-02T00:05:42.586Z"),
                    "modified_at": dateutil.parser.isoparse("2023-12-16T03:02:38.803Z"),
                    "id": "<value>",
                    "name": "<value>",
                    "description": "for embarrassment untidy long-term near honestly separate yet",
                    "is_recurring": True,
                    "is_archived": False,
                    "organization_id": "<value>",
                    "prices": [
                        {
                            "created_at": dateutil.parser.isoparse("2023-02-07T04:30:48.802Z"),
                            "modified_at": dateutil.parser.isoparse("2024-06-25T22:47:14.264Z"),
                            "id": "<value>",
                            "is_archived": False,
                            "product_id": "<value>",
                            "price_currency": "<value>",
                            "minimum_amount": 691423,
                            "maximum_amount": 499526,
                            "preset_amount": 18677,
                            "amount_type": polar_sdk.ProductPriceOneTimeCustomAmountType.CUSTOM,
                            "type": polar_sdk.ProductPriceOneTimeCustomType.ONE_TIME,
                        },
                    ],
                    "benefits": [
                        {
                            "created_at": dateutil.parser.isoparse("2023-08-22T00:47:02.059Z"),
                            "modified_at": dateutil.parser.isoparse("2023-06-04T10:32:44.101Z"),
                            "id": "<value>",
                            "type": polar_sdk.BenefitType.LICENSE_KEYS,
                            "description": "within jacket unless",
                            "selectable": False,
                            "deletable": False,
                            "organization_id": "<value>",
                        },
                    ],
                    "medias": [
                        {
                            "id": "<value>",
                            "organization_id": "<value>",
                            "name": "<value>",
                            "path": "/private/var",
                            "mime_type": "<value>",
                            "size": 245189,
                            "storage_version": "<value>",
                            "checksum_etag": "<value>",
                            "checksum_sha256_base64": "<value>",
                            "checksum_sha256_hex": "<value>",
                            "last_modified_at": dateutil.parser.isoparse("2022-11-03T15:00:03.276Z"),
                            "version": "<value>",
                            "is_uploaded": False,
                            "created_at": dateutil.parser.isoparse("2024-06-07T13:47:02.365Z"),
                            "size_readable": "<value>",
                            "public_url": "https://webbed-experience.name/",
                            "service": polar_sdk.Service.PRODUCT_MEDIA,
                        },
                    ],
                },
                product_price={
                    "created_at": dateutil.parser.isoparse("2022-04-02T00:05:42.586Z"),
                    "modified_at": dateutil.parser.isoparse("2023-12-16T03:02:38.803Z"),
                    "id": "<value>",
                    "is_archived": False,
                    "product_id": "<value>",
                    "price_currency": "<value>",
                    "price_amount": 740296,
                    "amount_type": polar_sdk.ProductPriceOneTimeFixedAmountType.FIXED,
                    "type": polar_sdk.ProductPriceOneTimeFixedType.ONE_TIME,
                },
                discount={
                    "duration": polar_sdk.DiscountDuration.REPEATING,
                    "type": polar_sdk.DiscountType.FIXED,
                    "basis_points": 341163,
                    "id": "<value>",
                    "name": "<value>",
                    "code": "<value>",
                },
                subscription_id="<value>",
                attached_custom_fields=[
                    {
                        "custom_field_id": "<value>",
                        "custom_field": {
                            "created_at": dateutil.parser.isoparse("2024-06-23T16:57:50.081Z"),
                            "modified_at": dateutil.parser.isoparse("2023-12-14T18:25:33.693Z"),
                            "id": "<value>",
                            "metadata": {
                                "key": "<value>",
                            },
                            "slug": "<value>",
                            "name": "<value>",
                            "organization_id": "<value>",
                            "properties": {},
                            "type": polar_sdk.CustomFieldNumberType.NUMBER,
                        },
                        "order": 996863,
                        "required": False,
                    },
                    {
                        "custom_field_id": "<value>",
                        "custom_field": {
                            "created_at": dateutil.parser.isoparse("2022-04-26T22:34:57.487Z"),
                            "modified_at": dateutil.parser.isoparse("2022-08-07T19:57:51.694Z"),
                            "id": "<value>",
                            "metadata": {
                                "key": 856200,
                            },
                            "slug": "<value>",
                            "name": "<value>",
                            "organization_id": "<value>",
                            "properties": {
                                "options": [
                                    {
                                        "value": "<value>",
                                        "label": "<value>",
                                    },
                                ],
                            },
                            "type": polar_sdk.CustomFieldSelectType.SELECT,
                        },
                        "order": 72589,
                        "required": True,
                    },
                    {
                        "custom_field_id": "<value>",
                        "custom_field": {
                            "created_at": dateutil.parser.isoparse("2024-05-25T15:20:50.694Z"),
                            "modified_at": dateutil.parser.isoparse("2023-11-28T14:29:40.329Z"),
                            "id": "<value>",
                            "metadata": {
                                "key": False,
                            },
                            "slug": "<value>",
                            "name": "<value>",
                            "organization_id": "<value>",
                            "properties": {},
                            "type": polar_sdk.CustomFieldCheckboxType.CHECKBOX,
                        },
                        "order": 161325,
                        "required": True,
                    },
                ],
                payment_processor=polar_sdk.PaymentProcessor.STRIPE,
            ),
            type=polar_sdk.WebhookCheckoutCreatedPayloadType.CHECKOUT_CREATED,
        ))

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

## Webhook support

The SDK has built-in support to validate webhook events. Here is an example with Flask:

```py
from flask import Flask, request
from polar_sdk.webhooks import validate_event, WebhookVerificationError

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        event = validate_event(
            payload=request.data,
            headers=request.headers,
            secret='<YOUR_WEBHOOK_SECRET>',
        )

        # Process the event

        return "", 202
    except WebhookVerificationError as e:
        return "", 403
```

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [advertisements](docs/sdks/advertisements/README.md)

* [list](docs/sdks/advertisements/README.md#list) - List Campaigns
* [get](docs/sdks/advertisements/README.md#get) - Get Campaign

### [benefits](docs/sdks/benefits/README.md)

* [list](docs/sdks/benefits/README.md#list) - List Benefits
* [create](docs/sdks/benefits/README.md#create) - Create Benefit
* [get](docs/sdks/benefits/README.md#get) - Get Benefit
* [update](docs/sdks/benefits/README.md#update) - Update Benefit
* [delete](docs/sdks/benefits/README.md#delete) - Delete Benefit
* [grants](docs/sdks/benefits/README.md#grants) - List Benefit Grants

### [checkout_links](docs/sdks/checkoutlinks/README.md)

* [list](docs/sdks/checkoutlinks/README.md#list) - List Checkout Links
* [create](docs/sdks/checkoutlinks/README.md#create) - Create Checkout Link
* [get](docs/sdks/checkoutlinks/README.md#get) - Get Checkout Link
* [update](docs/sdks/checkoutlinks/README.md#update) - Update Checkout Link
* [delete](docs/sdks/checkoutlinks/README.md#delete) - Delete Checkout Link

### [checkouts](docs/sdks/checkouts/README.md)

* [~~create~~](docs/sdks/checkouts/README.md#create) - Create Checkout :warning: **Deprecated** Use [create](docs/sdks/custom/README.md#create) instead.
* [~~get~~](docs/sdks/checkouts/README.md#get) - Get Checkout :warning: **Deprecated**

#### [checkouts.custom](docs/sdks/custom/README.md)

* [list](docs/sdks/custom/README.md#list) - List Checkout Sessions
* [create](docs/sdks/custom/README.md#create) - Create Checkout Session
* [get](docs/sdks/custom/README.md#get) - Get Checkout Session
* [update](docs/sdks/custom/README.md#update) - Update Checkout Session
* [client_get](docs/sdks/custom/README.md#client_get) - Get Checkout Session from Client
* [client_update](docs/sdks/custom/README.md#client_update) - Update Checkout Session from Client
* [client_confirm](docs/sdks/custom/README.md#client_confirm) - Confirm Checkout Session from Client

### [custom_fields](docs/sdks/customfields/README.md)

* [list](docs/sdks/customfields/README.md#list) - List Custom Fields
* [create](docs/sdks/customfields/README.md#create) - Create Custom Field
* [get](docs/sdks/customfields/README.md#get) - Get Custom Field
* [update](docs/sdks/customfields/README.md#update) - Update Custom Field
* [delete](docs/sdks/customfields/README.md#delete) - Delete Custom Field

### [customer_portal](docs/sdks/customerportal/README.md)


#### [customer_portal.benefit_grants](docs/sdks/benefitgrants/README.md)

* [list](docs/sdks/benefitgrants/README.md#list) - List Benefit Grants
* [get](docs/sdks/benefitgrants/README.md#get) - Get Benefit Grant
* [update](docs/sdks/benefitgrants/README.md#update) - Update Benefit Grant

#### [customer_portal.customers](docs/sdks/polarcustomers/README.md)

* [get](docs/sdks/polarcustomers/README.md#get) - Get Customer

#### [customer_portal.downloadables](docs/sdks/downloadables/README.md)

* [list](docs/sdks/downloadables/README.md#list) - List Downloadables
* [get](docs/sdks/downloadables/README.md#get) - Get Downloadable

#### [customer_portal.license_keys](docs/sdks/polarlicensekeys/README.md)

* [list](docs/sdks/polarlicensekeys/README.md#list) - List License Keys
* [get](docs/sdks/polarlicensekeys/README.md#get) - Get License Key
* [validate](docs/sdks/polarlicensekeys/README.md#validate) - Validate License Key
* [activate](docs/sdks/polarlicensekeys/README.md#activate) - Activate License Key
* [deactivate](docs/sdks/polarlicensekeys/README.md#deactivate) - Deactivate License Key

#### [customer_portal.orders](docs/sdks/polarorders/README.md)

* [list](docs/sdks/polarorders/README.md#list) - List Orders
* [get](docs/sdks/polarorders/README.md#get) - Get Order
* [invoice](docs/sdks/polarorders/README.md#invoice) - Get Order Invoice

#### [customer_portal.organizations](docs/sdks/polarorganizations/README.md)

* [get](docs/sdks/polarorganizations/README.md#get) - Get Organization

#### [customer_portal.subscriptions](docs/sdks/polarsubscriptions/README.md)

* [list](docs/sdks/polarsubscriptions/README.md#list) - List Subscriptions
* [get](docs/sdks/polarsubscriptions/README.md#get) - Get Subscription
* [update](docs/sdks/polarsubscriptions/README.md#update) - Update Subscription
* [cancel](docs/sdks/polarsubscriptions/README.md#cancel) - Cancel Subscription

### [customers](docs/sdks/customers/README.md)

* [list](docs/sdks/customers/README.md#list) - List Customers
* [create](docs/sdks/customers/README.md#create) - Create Customer
* [get](docs/sdks/customers/README.md#get) - Get Customer
* [update](docs/sdks/customers/README.md#update) - Update Customer
* [delete](docs/sdks/customers/README.md#delete) - Delete Customer

### [discounts](docs/sdks/discounts/README.md)

* [list](docs/sdks/discounts/README.md#list) - List Discounts
* [create](docs/sdks/discounts/README.md#create) - Create Discount
* [get](docs/sdks/discounts/README.md#get) - Get Discount
* [update](docs/sdks/discounts/README.md#update) - Update Discount
* [delete](docs/sdks/discounts/README.md#delete) - Delete Discount

### [external_organizations](docs/sdks/externalorganizations/README.md)

* [list](docs/sdks/externalorganizations/README.md#list) - List External Organizations

### [files](docs/sdks/files/README.md)

* [list](docs/sdks/files/README.md#list) - List Files
* [create](docs/sdks/files/README.md#create) - Create File
* [uploaded](docs/sdks/files/README.md#uploaded) - Complete File Upload
* [update](docs/sdks/files/README.md#update) - Update File
* [delete](docs/sdks/files/README.md#delete) - Delete File

### [license_keys](docs/sdks/licensekeys/README.md)

* [list](docs/sdks/licensekeys/README.md#list) - List License Keys
* [get](docs/sdks/licensekeys/README.md#get) - Get License Key
* [update](docs/sdks/licensekeys/README.md#update) - Update License Key
* [get_activation](docs/sdks/licensekeys/README.md#get_activation) - Get Activation

### [metrics](docs/sdks/metricssdk/README.md)

* [get](docs/sdks/metricssdk/README.md#get) - Get Metrics
* [limits](docs/sdks/metricssdk/README.md#limits) - Get Metrics Limits

### [oauth2](docs/sdks/oauth2/README.md)

* [authorize](docs/sdks/oauth2/README.md#authorize) - Authorize
* [token](docs/sdks/oauth2/README.md#token) - Request Token
* [revoke](docs/sdks/oauth2/README.md#revoke) - Revoke Token
* [introspect](docs/sdks/oauth2/README.md#introspect) - Introspect Token
* [userinfo](docs/sdks/oauth2/README.md#userinfo) - Get User Info

#### [oauth2.clients](docs/sdks/clients/README.md)

* [list](docs/sdks/clients/README.md#list) - List Clients
* [create](docs/sdks/clients/README.md#create) - Create Client
* [get](docs/sdks/clients/README.md#get) - Get Client
* [update](docs/sdks/clients/README.md#update) - Update Client
* [delete](docs/sdks/clients/README.md#delete) - Delete Client

### [orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - List Orders
* [get](docs/sdks/orders/README.md#get) - Get Order
* [invoice](docs/sdks/orders/README.md#invoice) - Get Order Invoice

### [organizations](docs/sdks/organizations/README.md)

* [list](docs/sdks/organizations/README.md#list) - List Organizations
* [create](docs/sdks/organizations/README.md#create) - Create Organization
* [get](docs/sdks/organizations/README.md#get) - Get Organization
* [update](docs/sdks/organizations/README.md#update) - Update Organization


### [products](docs/sdks/products/README.md)

* [list](docs/sdks/products/README.md#list) - List Products
* [create](docs/sdks/products/README.md#create) - Create Product
* [get](docs/sdks/products/README.md#get) - Get Product
* [update](docs/sdks/products/README.md#update) - Update Product
* [update_benefits](docs/sdks/products/README.md#update_benefits) - Update Product Benefits

### [repositories](docs/sdks/repositories/README.md)

* [list](docs/sdks/repositories/README.md#list) - List Repositories
* [get](docs/sdks/repositories/README.md#get) - Get Repository
* [update](docs/sdks/repositories/README.md#update) - Update Repository

### [subscriptions](docs/sdks/subscriptions/README.md)

* [list](docs/sdks/subscriptions/README.md#list) - List Subscriptions
* [export](docs/sdks/subscriptions/README.md#export) - Export Subscriptions

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from polar_sdk import Polar
from polar_sdk.utils import BackoffStrategy, RetryConfig

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    while res is not None:
        # Handle items

        res = res.next()

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from polar_sdk import Polar
from polar_sdk.utils import BackoffStrategy, RetryConfig

with Polar(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| models.HTTPValidationError | 422         | application/json |
| models.SDKError            | 4XX, 5XX    | \*/\*            |

### Example

```python
from polar_sdk import Polar, models

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = None
    try:

        res = polar.external_organizations.list()

        while res is not None:
            # Handle items

            res = res.next()

    except models.HTTPValidationError as e:
        # handle e.data: models.HTTPValidationErrorData
        raise(e)
    except models.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name         | Server                         |
| ------------ | ------------------------------ |
| `production` | `https://api.polar.sh`         |
| `sandbox`    | `https://sandbox-api.polar.sh` |

#### Example

```python
from polar_sdk import Polar

with Polar(
    server="sandbox",
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from polar_sdk import Polar

with Polar(
    server_url="https://api.polar.sh",
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from polar_sdk import Polar
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Polar(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from polar_sdk import Polar
from polar_sdk.httpclient import AsyncHttpClient
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

| Name           | Type | Scheme      |
| -------------- | ---- | ----------- |
| `access_token` | http | HTTP Bearer |

To authenticate with the API the `access_token` parameter must be set when initializing the SDK client instance. For example:
```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from polar_sdk import Polar
import logging

logging.basicConfig(level=logging.DEBUG)
s = Polar(debug_logger=logging.getLogger("polar_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Summary [summary] -->
## Summary

Polar API: Polar HTTP and Webhooks API

Read the docs at https://docs.polar.sh/api
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [polar-sdk](#polar-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Webhook support](#webhook-support)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Debugging](#debugging)
  * [Pagination](#pagination)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=polar-sdk&utm_campaign=python)
