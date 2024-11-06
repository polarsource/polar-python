"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .attachedcustomfield import AttachedCustomField, AttachedCustomFieldTypedDict
from .checkoutproduct import CheckoutProduct, CheckoutProductTypedDict
from .checkoutstatus import CheckoutStatus
from .organization import Organization, OrganizationTypedDict
from .polar_enums_paymentprocessor import PolarEnumsPaymentProcessor
from .productprice import ProductPrice, ProductPriceTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CheckoutPublicCustomFieldDataTypedDict(TypedDict):
    r"""Key-value object storing custom field values."""


class CheckoutPublicCustomFieldData(BaseModel):
    r"""Key-value object storing custom field values."""


class CheckoutPublicPaymentProcessorMetadataTypedDict(TypedDict):
    pass


class CheckoutPublicPaymentProcessorMetadata(BaseModel):
    pass


class CheckoutPublicTypedDict(TypedDict):
    r"""Checkout session data retrieved using the client secret."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    status: CheckoutStatus
    client_secret: str
    r"""Client secret used to update and complete the checkout session from the client."""
    url: str
    r"""URL where the customer can access the checkout session."""
    expires_at: datetime
    r"""Expiration date and time of the checkout session."""
    success_url: str
    r"""URL where the customer will be redirected after a successful payment."""
    embed_origin: Nullable[str]
    r"""When checkout is embedded, represents the Origin of the page embedding the checkout. Used as a security measure to send messages only to the embedding page."""
    amount: Nullable[int]
    tax_amount: Nullable[int]
    r"""Computed tax amount to pay in cents."""
    currency: Nullable[str]
    r"""Currency code of the checkout session."""
    total_amount: Nullable[int]
    r"""Total amount to pay in cents."""
    product_id: str
    r"""ID of the product to checkout."""
    product_price_id: str
    r"""ID of the product price to checkout."""
    is_payment_required: bool
    r"""Whether the checkout requires payment. Useful to detect free products."""
    customer_id: Nullable[str]
    customer_name: Nullable[str]
    customer_email: Nullable[str]
    customer_ip_address: Nullable[str]
    customer_billing_address: Nullable[AddressTypedDict]
    customer_tax_id: Nullable[str]
    payment_processor_metadata: CheckoutPublicPaymentProcessorMetadataTypedDict
    product: CheckoutProductTypedDict
    r"""Product data for a checkout session."""
    product_price: ProductPriceTypedDict
    organization: OrganizationTypedDict
    attached_custom_fields: List[AttachedCustomFieldTypedDict]
    custom_field_data: NotRequired[CheckoutPublicCustomFieldDataTypedDict]
    r"""Key-value object storing custom field values."""
    payment_processor: PolarEnumsPaymentProcessor


class CheckoutPublic(BaseModel):
    r"""Checkout session data retrieved using the client secret."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    status: CheckoutStatus

    client_secret: str
    r"""Client secret used to update and complete the checkout session from the client."""

    url: str
    r"""URL where the customer can access the checkout session."""

    expires_at: datetime
    r"""Expiration date and time of the checkout session."""

    success_url: str
    r"""URL where the customer will be redirected after a successful payment."""

    embed_origin: Nullable[str]
    r"""When checkout is embedded, represents the Origin of the page embedding the checkout. Used as a security measure to send messages only to the embedding page."""

    amount: Nullable[int]

    tax_amount: Nullable[int]
    r"""Computed tax amount to pay in cents."""

    currency: Nullable[str]
    r"""Currency code of the checkout session."""

    total_amount: Nullable[int]
    r"""Total amount to pay in cents."""

    product_id: str
    r"""ID of the product to checkout."""

    product_price_id: str
    r"""ID of the product price to checkout."""

    is_payment_required: bool
    r"""Whether the checkout requires payment. Useful to detect free products."""

    customer_id: Nullable[str]

    customer_name: Nullable[str]

    customer_email: Nullable[str]

    customer_ip_address: Nullable[str]

    customer_billing_address: Nullable[Address]

    customer_tax_id: Nullable[str]

    payment_processor_metadata: CheckoutPublicPaymentProcessorMetadata

    product: CheckoutProduct
    r"""Product data for a checkout session."""

    product_price: ProductPrice

    organization: Organization

    attached_custom_fields: List[AttachedCustomField]

    custom_field_data: Optional[CheckoutPublicCustomFieldData] = None
    r"""Key-value object storing custom field values."""

    PAYMENT_PROCESSOR: Annotated[
        Annotated[
            PolarEnumsPaymentProcessor,
            AfterValidator(validate_const(PolarEnumsPaymentProcessor.STRIPE)),
        ],
        pydantic.Field(alias="payment_processor"),
    ] = PolarEnumsPaymentProcessor.STRIPE

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["custom_field_data"]
        nullable_fields = [
            "modified_at",
            "embed_origin",
            "amount",
            "tax_amount",
            "currency",
            "total_amount",
            "customer_id",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
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
