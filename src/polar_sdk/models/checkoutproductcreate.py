"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CheckoutProductCreateMetadataTypedDict = TypeAliasType(
    "CheckoutProductCreateMetadataTypedDict", Union[str, int, bool]
)


CheckoutProductCreateMetadata = TypeAliasType(
    "CheckoutProductCreateMetadata", Union[str, int, bool]
)


class CheckoutProductCreateCustomFieldDataTypedDict(TypedDict):
    r"""Key-value object storing custom field values."""


class CheckoutProductCreateCustomFieldData(BaseModel):
    r"""Key-value object storing custom field values."""


class CheckoutProductCreatePaymentProcessor(str, Enum):
    r"""Payment processor to use. Currently only Stripe is supported."""

    STRIPE = "stripe"


CheckoutProductCreateCustomerMetadataTypedDict = TypeAliasType(
    "CheckoutProductCreateCustomerMetadataTypedDict", Union[str, int, bool]
)


CheckoutProductCreateCustomerMetadata = TypeAliasType(
    "CheckoutProductCreateCustomerMetadata", Union[str, int, bool]
)


class CheckoutProductCreateTypedDict(TypedDict):
    r"""Create a new checkout session from a product.

    Metadata set on the checkout will be copied
    to the resulting order and/or subscription.
    """

    product_id: str
    r"""ID of the product to checkout. First available price will be selected."""
    metadata: NotRequired[Dict[str, CheckoutProductCreateMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    custom_field_data: NotRequired[CheckoutProductCreateCustomFieldDataTypedDict]
    r"""Key-value object storing custom field values."""
    payment_processor: CheckoutProductCreatePaymentProcessor
    r"""Payment processor to use. Currently only Stripe is supported."""
    discount_id: NotRequired[Nullable[str]]
    r"""ID of the discount to apply to the checkout."""
    allow_discount_codes: NotRequired[bool]
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""
    amount: NotRequired[Nullable[int]]
    customer_id: NotRequired[Nullable[str]]
    r"""ID of an existing customer in the organization. The customer data will be pre-filled in the checkout form. The resulting order will be linked to this customer."""
    customer_name: NotRequired[Nullable[str]]
    customer_email: NotRequired[Nullable[str]]
    customer_ip_address: NotRequired[Nullable[str]]
    customer_billing_address: NotRequired[Nullable[AddressTypedDict]]
    customer_tax_id: NotRequired[Nullable[str]]
    customer_metadata: NotRequired[
        Dict[str, CheckoutProductCreateCustomerMetadataTypedDict]
    ]
    r"""Key-value object allowing you to store additional information that'll be copied to the created customer.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    subscription_id: NotRequired[Nullable[str]]
    r"""ID of a subscription to upgrade. It must be on a free pricing. If checkout is successful, metadata set on this checkout will be copied to the subscription, and existing keys will be overwritten."""
    success_url: NotRequired[Nullable[str]]
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""
    embed_origin: NotRequired[Nullable[str]]
    r"""If you plan to embed the checkout session, set this to the Origin of the embedding page. It'll allow the Polar iframe to communicate with the parent page."""


class CheckoutProductCreate(BaseModel):
    r"""Create a new checkout session from a product.

    Metadata set on the checkout will be copied
    to the resulting order and/or subscription.
    """

    product_id: str
    r"""ID of the product to checkout. First available price will be selected."""

    metadata: Optional[Dict[str, CheckoutProductCreateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    custom_field_data: Optional[CheckoutProductCreateCustomFieldData] = None
    r"""Key-value object storing custom field values."""

    PAYMENT_PROCESSOR: Annotated[
        Annotated[
            CheckoutProductCreatePaymentProcessor,
            AfterValidator(
                validate_const(CheckoutProductCreatePaymentProcessor.STRIPE)
            ),
        ],
        pydantic.Field(alias="payment_processor"),
    ] = CheckoutProductCreatePaymentProcessor.STRIPE
    r"""Payment processor to use. Currently only Stripe is supported."""

    discount_id: OptionalNullable[str] = UNSET
    r"""ID of the discount to apply to the checkout."""

    allow_discount_codes: Optional[bool] = True
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""

    amount: OptionalNullable[int] = UNSET

    customer_id: OptionalNullable[str] = UNSET
    r"""ID of an existing customer in the organization. The customer data will be pre-filled in the checkout form. The resulting order will be linked to this customer."""

    customer_name: OptionalNullable[str] = UNSET

    customer_email: OptionalNullable[str] = UNSET

    customer_ip_address: OptionalNullable[str] = UNSET

    customer_billing_address: OptionalNullable[Address] = UNSET

    customer_tax_id: OptionalNullable[str] = UNSET

    customer_metadata: Optional[Dict[str, CheckoutProductCreateCustomerMetadata]] = None
    r"""Key-value object allowing you to store additional information that'll be copied to the created customer.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    subscription_id: OptionalNullable[str] = UNSET
    r"""ID of a subscription to upgrade. It must be on a free pricing. If checkout is successful, metadata set on this checkout will be copied to the subscription, and existing keys will be overwritten."""

    success_url: OptionalNullable[str] = UNSET
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""

    embed_origin: OptionalNullable[str] = UNSET
    r"""If you plan to embed the checkout session, set this to the Origin of the embedding page. It'll allow the Polar iframe to communicate with the parent page."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "custom_field_data",
            "discount_id",
            "allow_discount_codes",
            "amount",
            "customer_id",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
            "customer_metadata",
            "subscription_id",
            "success_url",
            "embed_origin",
        ]
        nullable_fields = [
            "discount_id",
            "amount",
            "customer_id",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
            "subscription_id",
            "success_url",
            "embed_origin",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
