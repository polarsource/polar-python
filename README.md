# polar-sdk

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=polar-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

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
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [Pagination](#pagination)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

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

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from polar-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "polar-sdk",
# ]
# ///

from polar_sdk import Polar

sdk = Polar(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
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
import polar_sdk
from polar_sdk import Polar
from polar_sdk.utils import parse_datetime


with Polar() as polar:

    res = polar.endpointcheckout_created_post(request=polar_sdk.WebhookCheckoutCreatedPayload(
        data=polar_sdk.Checkout(
            created_at=parse_datetime("2023-02-15T15:44:21.478Z"),
            modified_at=parse_datetime("2023-09-13T08:36:46.434Z"),
            id="<value>",
            payment_processor=polar_sdk.PaymentProcessor.STRIPE,
            status=polar_sdk.CheckoutStatus.EXPIRED,
            client_secret="<value>",
            url="https://whole-aftermath.net/",
            expires_at=parse_datetime("2023-12-28T10:30:56.042Z"),
            success_url="https://moral-premier.name/",
            embed_origin="<value>",
            amount=929514,
            discount_amount=323773,
            net_amount=115799,
            tax_amount=97012,
            total_amount=859980,
            currency="Fiji Dollar",
            product_id="<value>",
            product_price_id="<value>",
            discount_id=None,
            allow_discount_codes=True,
            require_billing_address=True,
            is_discount_applicable=True,
            is_free_product_price=True,
            is_payment_required=True,
            is_payment_setup_required=True,
            is_payment_form_required=True,
            customer_id="<value>",
            is_business_customer=False,
            customer_name="<value>",
            customer_email=None,
            customer_ip_address=None,
            customer_billing_name="<value>",
            customer_billing_address=polar_sdk.Address(
                country="US",
            ),
            customer_tax_id="<id>",
            payment_processor_metadata={
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
            customer_billing_address_fields=polar_sdk.CheckoutCustomerBillingAddressFields(
                country=True,
                state=False,
                city=False,
                postal_code=True,
                line1=True,
                line2=False,
            ),
            metadata={
                "key": False,
                "key1": False,
            },
            external_customer_id=None,
            customer_external_id="<id>",
            products=[
                polar_sdk.CheckoutProduct(
                    created_at=parse_datetime("2025-07-23T17:21:51.405Z"),
                    modified_at=parse_datetime("2024-01-17T03:32:08.030Z"),
                    id="<value>",
                    name="<value>",
                    description="funny abscond fairly except slight",
                    recurring_interval=None,
                    is_recurring=True,
                    is_archived=True,
                    organization_id="<value>",
                    prices=[
                        polar_sdk.LegacyRecurringProductPriceFree(),
                    ],
                    benefits=[],
                    medias=[
                        polar_sdk.ProductMediaFileRead(
                            id="<value>",
                            organization_id="<value>",
                            name="<value>",
                            path="/var/log",
                            mime_type="<value>",
                            size=982910,
                            storage_version="<value>",
                            checksum_etag="<value>",
                            checksum_sha256_base64="<value>",
                            checksum_sha256_hex="<value>",
                            last_modified_at=parse_datetime("2024-09-13T03:57:17.676Z"),
                            version="<value>",
                            is_uploaded=False,
                            created_at=parse_datetime("2023-03-23T06:47:50.944Z"),
                            size_readable="<value>",
                            public_url="https://yummy-ocelot.biz/",
                        ),
                        polar_sdk.ProductMediaFileRead(
                            id="<value>",
                            organization_id="<value>",
                            name="<value>",
                            path="/var/log",
                            mime_type="<value>",
                            size=982910,
                            storage_version="<value>",
                            checksum_etag="<value>",
                            checksum_sha256_base64="<value>",
                            checksum_sha256_hex="<value>",
                            last_modified_at=parse_datetime("2024-09-13T03:57:17.676Z"),
                            version="<value>",
                            is_uploaded=False,
                            created_at=parse_datetime("2023-03-23T06:47:50.944Z"),
                            size_readable="<value>",
                            public_url="https://yummy-ocelot.biz/",
                        ),
                        polar_sdk.ProductMediaFileRead(
                            id="<value>",
                            organization_id="<value>",
                            name="<value>",
                            path="/var/log",
                            mime_type="<value>",
                            size=982910,
                            storage_version="<value>",
                            checksum_etag="<value>",
                            checksum_sha256_base64="<value>",
                            checksum_sha256_hex="<value>",
                            last_modified_at=parse_datetime("2024-09-13T03:57:17.676Z"),
                            version="<value>",
                            is_uploaded=False,
                            created_at=parse_datetime("2023-03-23T06:47:50.944Z"),
                            size_readable="<value>",
                            public_url="https://yummy-ocelot.biz/",
                        ),
                    ],
                ),
            ],
            product=polar_sdk.CheckoutProduct(
                created_at=parse_datetime("2023-03-01T03:35:30.257Z"),
                modified_at=parse_datetime("2024-12-19T15:40:11.887Z"),
                id="<value>",
                name="<value>",
                description="until joyful how",
                recurring_interval=polar_sdk.SubscriptionRecurringInterval.MONTH,
                is_recurring=True,
                is_archived=False,
                organization_id="<value>",
                prices=[
                    polar_sdk.LegacyRecurringProductPriceCustom(),
                    polar_sdk.LegacyRecurringProductPriceCustom(),
                    polar_sdk.ProductPriceMeteredUnit(),
                ],
                benefits=[
                    polar_sdk.BenefitPublic(
                        id="<value>",
                        created_at=parse_datetime("2023-11-22T11:07:53.319Z"),
                        modified_at=parse_datetime("2025-09-17T18:38:51.288Z"),
                        type=polar_sdk.BenefitType.DISCORD,
                        description="brr now psst",
                        selectable=True,
                        deletable=True,
                        organization_id="<value>",
                    ),
                    polar_sdk.BenefitPublic(
                        id="<value>",
                        created_at=parse_datetime("2023-11-22T11:07:53.319Z"),
                        modified_at=parse_datetime("2025-09-17T18:38:51.288Z"),
                        type=polar_sdk.BenefitType.DISCORD,
                        description="brr now psst",
                        selectable=True,
                        deletable=True,
                        organization_id="<value>",
                    ),
                ],
                medias=[],
            ),
            product_price=polar_sdk.ProductPriceMeteredUnit(),
            discount=polar_sdk.CheckoutDiscountPercentageRepeatDuration(
                duration=polar_sdk.DiscountDuration.REPEATING,
                duration_in_months=470604,
                type=polar_sdk.DiscountType.FIXED,
                basis_points=567071,
                id="<value>",
                name="<value>",
                code="<value>",
            ),
            subscription_id="<value>",
            attached_custom_fields=[
                polar_sdk.AttachedCustomField(
                    custom_field_id="<value>",
                    custom_field=polar_sdk.CustomFieldNumber(
                        created_at=parse_datetime("2024-01-27T12:44:05.844Z"),
                        modified_at=parse_datetime("2023-11-12T13:10:44.040Z"),
                        id="<value>",
                        metadata={
                            "key": 833527,
                            "key1": False,
                        },
                        slug="<value>",
                        name="<value>",
                        organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737",
                        properties=polar_sdk.CustomFieldNumberProperties(),
                    ),
                    order=786803,
                    required=False,
                ),
                polar_sdk.AttachedCustomField(
                    custom_field_id="<value>",
                    custom_field=polar_sdk.CustomFieldNumber(
                        created_at=parse_datetime("2024-01-27T12:44:05.844Z"),
                        modified_at=parse_datetime("2023-11-12T13:10:44.040Z"),
                        id="<value>",
                        metadata={
                            "key": 833527,
                            "key1": False,
                        },
                        slug="<value>",
                        name="<value>",
                        organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737",
                        properties=polar_sdk.CustomFieldNumberProperties(),
                    ),
                    order=786803,
                    required=False,
                ),
            ],
            customer_metadata={

            },
        ),
    ))

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import polar_sdk
from polar_sdk import Polar
from polar_sdk.utils import parse_datetime

async def main():

    async with Polar() as polar:

        res = await polar.endpointcheckout_created_post_async(request=polar_sdk.WebhookCheckoutCreatedPayload(
            data=polar_sdk.Checkout(
                created_at=parse_datetime("2023-02-15T15:44:21.478Z"),
                modified_at=parse_datetime("2023-09-13T08:36:46.434Z"),
                id="<value>",
                payment_processor=polar_sdk.PaymentProcessor.STRIPE,
                status=polar_sdk.CheckoutStatus.EXPIRED,
                client_secret="<value>",
                url="https://whole-aftermath.net/",
                expires_at=parse_datetime("2023-12-28T10:30:56.042Z"),
                success_url="https://moral-premier.name/",
                embed_origin="<value>",
                amount=929514,
                discount_amount=323773,
                net_amount=115799,
                tax_amount=97012,
                total_amount=859980,
                currency="Fiji Dollar",
                product_id="<value>",
                product_price_id="<value>",
                discount_id=None,
                allow_discount_codes=True,
                require_billing_address=True,
                is_discount_applicable=True,
                is_free_product_price=True,
                is_payment_required=True,
                is_payment_setup_required=True,
                is_payment_form_required=True,
                customer_id="<value>",
                is_business_customer=False,
                customer_name="<value>",
                customer_email=None,
                customer_ip_address=None,
                customer_billing_name="<value>",
                customer_billing_address=polar_sdk.Address(
                    country="US",
                ),
                customer_tax_id="<id>",
                payment_processor_metadata={
                    "key": "<value>",
                    "key1": "<value>",
                    "key2": "<value>",
                },
                customer_billing_address_fields=polar_sdk.CheckoutCustomerBillingAddressFields(
                    country=True,
                    state=False,
                    city=False,
                    postal_code=True,
                    line1=True,
                    line2=False,
                ),
                metadata={
                    "key": False,
                    "key1": False,
                },
                external_customer_id=None,
                customer_external_id="<id>",
                products=[
                    polar_sdk.CheckoutProduct(
                        created_at=parse_datetime("2025-07-23T17:21:51.405Z"),
                        modified_at=parse_datetime("2024-01-17T03:32:08.030Z"),
                        id="<value>",
                        name="<value>",
                        description="funny abscond fairly except slight",
                        recurring_interval=None,
                        is_recurring=True,
                        is_archived=True,
                        organization_id="<value>",
                        prices=[
                            polar_sdk.LegacyRecurringProductPriceFree(),
                        ],
                        benefits=[],
                        medias=[
                            polar_sdk.ProductMediaFileRead(
                                id="<value>",
                                organization_id="<value>",
                                name="<value>",
                                path="/var/log",
                                mime_type="<value>",
                                size=982910,
                                storage_version="<value>",
                                checksum_etag="<value>",
                                checksum_sha256_base64="<value>",
                                checksum_sha256_hex="<value>",
                                last_modified_at=parse_datetime("2024-09-13T03:57:17.676Z"),
                                version="<value>",
                                is_uploaded=False,
                                created_at=parse_datetime("2023-03-23T06:47:50.944Z"),
                                size_readable="<value>",
                                public_url="https://yummy-ocelot.biz/",
                            ),
                            polar_sdk.ProductMediaFileRead(
                                id="<value>",
                                organization_id="<value>",
                                name="<value>",
                                path="/var/log",
                                mime_type="<value>",
                                size=982910,
                                storage_version="<value>",
                                checksum_etag="<value>",
                                checksum_sha256_base64="<value>",
                                checksum_sha256_hex="<value>",
                                last_modified_at=parse_datetime("2024-09-13T03:57:17.676Z"),
                                version="<value>",
                                is_uploaded=False,
                                created_at=parse_datetime("2023-03-23T06:47:50.944Z"),
                                size_readable="<value>",
                                public_url="https://yummy-ocelot.biz/",
                            ),
                            polar_sdk.ProductMediaFileRead(
                                id="<value>",
                                organization_id="<value>",
                                name="<value>",
                                path="/var/log",
                                mime_type="<value>",
                                size=982910,
                                storage_version="<value>",
                                checksum_etag="<value>",
                                checksum_sha256_base64="<value>",
                                checksum_sha256_hex="<value>",
                                last_modified_at=parse_datetime("2024-09-13T03:57:17.676Z"),
                                version="<value>",
                                is_uploaded=False,
                                created_at=parse_datetime("2023-03-23T06:47:50.944Z"),
                                size_readable="<value>",
                                public_url="https://yummy-ocelot.biz/",
                            ),
                        ],
                    ),
                ],
                product=polar_sdk.CheckoutProduct(
                    created_at=parse_datetime("2023-03-01T03:35:30.257Z"),
                    modified_at=parse_datetime("2024-12-19T15:40:11.887Z"),
                    id="<value>",
                    name="<value>",
                    description="until joyful how",
                    recurring_interval=polar_sdk.SubscriptionRecurringInterval.MONTH,
                    is_recurring=True,
                    is_archived=False,
                    organization_id="<value>",
                    prices=[
                        polar_sdk.ProductPriceFixed(),
                        polar_sdk.ProductPriceMeteredUnit(),
                        polar_sdk.ProductPriceCustom(),
                    ],
                    benefits=[
                        polar_sdk.BenefitPublic(
                            id="<value>",
                            created_at=parse_datetime("2023-11-22T11:07:53.319Z"),
                            modified_at=parse_datetime("2025-09-17T18:38:51.288Z"),
                            type=polar_sdk.BenefitType.DISCORD,
                            description="brr now psst",
                            selectable=True,
                            deletable=True,
                            organization_id="<value>",
                        ),
                        polar_sdk.BenefitPublic(
                            id="<value>",
                            created_at=parse_datetime("2023-11-22T11:07:53.319Z"),
                            modified_at=parse_datetime("2025-09-17T18:38:51.288Z"),
                            type=polar_sdk.BenefitType.DISCORD,
                            description="brr now psst",
                            selectable=True,
                            deletable=True,
                            organization_id="<value>",
                        ),
                    ],
                    medias=[],
                ),
                product_price=polar_sdk.LegacyRecurringProductPriceFixed(),
                discount=polar_sdk.CheckoutDiscountPercentageRepeatDuration(
                    duration=polar_sdk.DiscountDuration.REPEATING,
                    duration_in_months=470604,
                    type=polar_sdk.DiscountType.FIXED,
                    basis_points=567071,
                    id="<value>",
                    name="<value>",
                    code="<value>",
                ),
                subscription_id="<value>",
                attached_custom_fields=[
                    polar_sdk.AttachedCustomField(
                        custom_field_id="<value>",
                        custom_field=polar_sdk.CustomFieldNumber(
                            created_at=parse_datetime("2024-01-27T12:44:05.844Z"),
                            modified_at=parse_datetime("2023-11-12T13:10:44.040Z"),
                            id="<value>",
                            metadata={
                                "key": 833527,
                                "key1": False,
                            },
                            slug="<value>",
                            name="<value>",
                            organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737",
                            properties=polar_sdk.CustomFieldNumberProperties(),
                        ),
                        order=786803,
                        required=False,
                    ),
                    polar_sdk.AttachedCustomField(
                        custom_field_id="<value>",
                        custom_field=polar_sdk.CustomFieldNumber(
                            created_at=parse_datetime("2024-01-27T12:44:05.844Z"),
                            modified_at=parse_datetime("2023-11-12T13:10:44.040Z"),
                            id="<value>",
                            metadata={
                                "key": 833527,
                                "key1": False,
                            },
                            slug="<value>",
                            name="<value>",
                            organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737",
                            properties=polar_sdk.CustomFieldNumberProperties(),
                        ),
                        order=786803,
                        required=False,
                    ),
                ],
                customer_metadata={

                },
            ),
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

* [list](docs/sdks/checkouts/README.md#list) - List Checkout Sessions
* [create](docs/sdks/checkouts/README.md#create) - Create Checkout Session
* [get](docs/sdks/checkouts/README.md#get) - Get Checkout Session
* [update](docs/sdks/checkouts/README.md#update) - Update Checkout Session
* [client_get](docs/sdks/checkouts/README.md#client_get) - Get Checkout Session from Client
* [client_update](docs/sdks/checkouts/README.md#client_update) - Update Checkout Session from Client
* [client_confirm](docs/sdks/checkouts/README.md#client_confirm) - Confirm Checkout Session from Client

### [custom_fields](docs/sdks/customfields/README.md)

* [list](docs/sdks/customfields/README.md#list) - List Custom Fields
* [create](docs/sdks/customfields/README.md#create) - Create Custom Field
* [get](docs/sdks/customfields/README.md#get) - Get Custom Field
* [update](docs/sdks/customfields/README.md#update) - Update Custom Field
* [delete](docs/sdks/customfields/README.md#delete) - Delete Custom Field

### [customer_meters](docs/sdks/customermeters/README.md)

* [list](docs/sdks/customermeters/README.md#list) - List Customer Meters
* [get](docs/sdks/customermeters/README.md#get) - Get Customer Meter

### [customer_portal](docs/sdks/customerportal/README.md)


#### [customer_portal.benefit_grants](docs/sdks/benefitgrants/README.md)

* [list](docs/sdks/benefitgrants/README.md#list) - List Benefit Grants
* [get](docs/sdks/benefitgrants/README.md#get) - Get Benefit Grant
* [update](docs/sdks/benefitgrants/README.md#update) - Update Benefit Grant

#### [customer_portal.customer_meters](docs/sdks/polarcustomermeters/README.md)

* [list](docs/sdks/polarcustomermeters/README.md#list) - List Meters
* [get](docs/sdks/polarcustomermeters/README.md#get) - Get Customer Meter

#### [customer_portal.customers](docs/sdks/polarcustomers/README.md)

* [get](docs/sdks/polarcustomers/README.md#get) - Get Customer
* [update](docs/sdks/polarcustomers/README.md#update) - Update Customer
* [get_payment_methods](docs/sdks/polarcustomers/README.md#get_payment_methods) - Get Customer Payment Methods
* [add_payment_method](docs/sdks/polarcustomers/README.md#add_payment_method) - Add Customer Payment Method
* [delete_payment_method](docs/sdks/polarcustomers/README.md#delete_payment_method) - Delete Customer Payment Method

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
* [update](docs/sdks/polarorders/README.md#update) - Update Order
* [generate_invoice](docs/sdks/polarorders/README.md#generate_invoice) - Generate Order Invoice
* [invoice](docs/sdks/polarorders/README.md#invoice) - Get Order Invoice

#### [customer_portal.organizations](docs/sdks/polarorganizations/README.md)

* [get](docs/sdks/polarorganizations/README.md#get) - Get Organization

#### [customer_portal.subscriptions](docs/sdks/polarsubscriptions/README.md)

* [list](docs/sdks/polarsubscriptions/README.md#list) - List Subscriptions
* [get](docs/sdks/polarsubscriptions/README.md#get) - Get Subscription
* [update](docs/sdks/polarsubscriptions/README.md#update) - Update Subscription
* [cancel](docs/sdks/polarsubscriptions/README.md#cancel) - Cancel Subscription

### [customer_sessions](docs/sdks/customersessions/README.md)

* [create](docs/sdks/customersessions/README.md#create) - Create Customer Session

### [customers](docs/sdks/customers/README.md)

* [list](docs/sdks/customers/README.md#list) - List Customers
* [create](docs/sdks/customers/README.md#create) - Create Customer
* [get](docs/sdks/customers/README.md#get) - Get Customer
* [update](docs/sdks/customers/README.md#update) - Update Customer
* [delete](docs/sdks/customers/README.md#delete) - Delete Customer
* [get_external](docs/sdks/customers/README.md#get_external) - Get Customer by External ID
* [update_external](docs/sdks/customers/README.md#update_external) - Update Customer by External ID
* [delete_external](docs/sdks/customers/README.md#delete_external) - Delete Customer by External ID
* [get_state](docs/sdks/customers/README.md#get_state) - Get Customer State
* [get_state_external](docs/sdks/customers/README.md#get_state_external) - Get Customer State by External ID

### [discounts](docs/sdks/discounts/README.md)

* [list](docs/sdks/discounts/README.md#list) - List Discounts
* [create](docs/sdks/discounts/README.md#create) - Create Discount
* [get](docs/sdks/discounts/README.md#get) - Get Discount
* [update](docs/sdks/discounts/README.md#update) - Update Discount
* [delete](docs/sdks/discounts/README.md#delete) - Delete Discount

### [events](docs/sdks/events/README.md)

* [list](docs/sdks/events/README.md#list) - List Events
* [list_names](docs/sdks/events/README.md#list_names) - List Event Names
* [get](docs/sdks/events/README.md#get) - Get Event
* [ingest](docs/sdks/events/README.md#ingest) - Ingest Events

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

### [meters](docs/sdks/meters/README.md)

* [list](docs/sdks/meters/README.md#list) - List Meters
* [create](docs/sdks/meters/README.md#create) - Create Meter
* [get](docs/sdks/meters/README.md#get) - Get Meter
* [update](docs/sdks/meters/README.md#update) - Update Meter
* [quantities](docs/sdks/meters/README.md#quantities) - Get Meter Quantities

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
* [update](docs/sdks/orders/README.md#update) - Update Order
* [generate_invoice](docs/sdks/orders/README.md#generate_invoice) - Generate Order Invoice
* [invoice](docs/sdks/orders/README.md#invoice) - Get Order Invoice

### [organizations](docs/sdks/organizations/README.md)

* [list](docs/sdks/organizations/README.md#list) - List Organizations
* [create](docs/sdks/organizations/README.md#create) - Create Organization
* [get](docs/sdks/organizations/README.md#get) - Get Organization
* [update](docs/sdks/organizations/README.md#update) - Update Organization

### [payments](docs/sdks/payments/README.md)

* [list](docs/sdks/payments/README.md#list) - List Payments
* [get](docs/sdks/payments/README.md#get) - Get Payment


### [products](docs/sdks/products/README.md)

* [list](docs/sdks/products/README.md#list) - List Products
* [create](docs/sdks/products/README.md#create) - Create Product
* [get](docs/sdks/products/README.md#get) - Get Product
* [update](docs/sdks/products/README.md#update) - Update Product
* [update_benefits](docs/sdks/products/README.md#update_benefits) - Update Product Benefits

### [refunds](docs/sdks/refunds/README.md)

* [list](docs/sdks/refunds/README.md#list) - List Refunds
* [create](docs/sdks/refunds/README.md#create) - Create Refund

### [subscriptions](docs/sdks/subscriptions/README.md)

* [list](docs/sdks/subscriptions/README.md#list) - List Subscriptions
* [export](docs/sdks/subscriptions/README.md#export) - Export Subscriptions
* [get](docs/sdks/subscriptions/README.md#get) - Get Subscription
* [update](docs/sdks/subscriptions/README.md#update) - Update Subscription
* [revoke](docs/sdks/subscriptions/README.md#revoke) - Revoke Subscription

### [webhooks](docs/sdks/webhooks/README.md)

* [list_webhook_endpoints](docs/sdks/webhooks/README.md#list_webhook_endpoints) - List Webhook Endpoints
* [create_webhook_endpoint](docs/sdks/webhooks/README.md#create_webhook_endpoint) - Create Webhook Endpoint
* [get_webhook_endpoint](docs/sdks/webhooks/README.md#get_webhook_endpoint) - Get Webhook Endpoint
* [update_webhook_endpoint](docs/sdks/webhooks/README.md#update_webhook_endpoint) - Update Webhook Endpoint
* [delete_webhook_endpoint](docs/sdks/webhooks/README.md#delete_webhook_endpoint) - Delete Webhook Endpoint
* [list_webhook_deliveries](docs/sdks/webhooks/README.md#list_webhook_deliveries) - List Webhook Deliveries
* [redeliver_webhook_event](docs/sdks/webhooks/README.md#redeliver_webhook_event) - Redeliver Webhook Event

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

    res = polar.organizations.list(page=1, limit=10,
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

    res = polar.organizations.list(page=1, limit=10)

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

        res = polar.organizations.list(page=1, limit=10)

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

| Name         | Server                         | Description            |
| ------------ | ------------------------------ | ---------------------- |
| `production` | `https://api.polar.sh`         | Production environment |
| `sandbox`    | `https://sandbox-api.polar.sh` | Sandbox environment    |

#### Example

```python
from polar_sdk import Polar


with Polar(
    server="sandbox",
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.organizations.list(page=1, limit=10)

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

    res = polar.organizations.list(page=1, limit=10)

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

    res = polar.organizations.list(page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.benefit_grants.list(security=polar_sdk.CustomerPortalBenefitGrantsListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id=None, page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Polar` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from polar_sdk import Polar
def main():

    with Polar(
        access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as polar:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Polar(
        access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as polar:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

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

    res = polar.organizations.list(page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Summary [summary] -->
## Summary

Polar API: Polar HTTP and Webhooks API

Read the docs at https://docs.polar.sh/api-reference
<!-- End Summary [summary] -->

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
