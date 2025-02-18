"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .attachedcustomfield import AttachedCustomField, AttachedCustomFieldTypedDict
from .checkoutdiscountfixedonceforeverduration import (
    CheckoutDiscountFixedOnceForeverDuration,
    CheckoutDiscountFixedOnceForeverDurationTypedDict,
)
from .checkoutdiscountfixedrepeatduration import (
    CheckoutDiscountFixedRepeatDuration,
    CheckoutDiscountFixedRepeatDurationTypedDict,
)
from .checkoutdiscountpercentageonceforeverduration import (
    CheckoutDiscountPercentageOnceForeverDuration,
    CheckoutDiscountPercentageOnceForeverDurationTypedDict,
)
from .checkoutdiscountpercentagerepeatduration import (
    CheckoutDiscountPercentageRepeatDuration,
    CheckoutDiscountPercentageRepeatDurationTypedDict,
)
from .checkoutproduct import CheckoutProduct, CheckoutProductTypedDict
from .checkoutstatus import CheckoutStatus
from .legacyrecurringproductprice import (
    LegacyRecurringProductPrice,
    LegacyRecurringProductPriceTypedDict,
)
from .organization import Organization, OrganizationTypedDict
from .paymentprocessor import PaymentProcessor
from .productprice import ProductPrice, ProductPriceTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


CheckoutPublicCustomFieldDataTypedDict = TypeAliasType(
    "CheckoutPublicCustomFieldDataTypedDict", Union[str, int, bool, datetime]
)


CheckoutPublicCustomFieldData = TypeAliasType(
    "CheckoutPublicCustomFieldData", Union[str, int, bool, datetime]
)


CheckoutPublicProductPriceTypedDict = TypeAliasType(
    "CheckoutPublicProductPriceTypedDict",
    Union[LegacyRecurringProductPriceTypedDict, ProductPriceTypedDict],
)
r"""Price of the selected product."""


CheckoutPublicProductPrice = TypeAliasType(
    "CheckoutPublicProductPrice", Union[LegacyRecurringProductPrice, ProductPrice]
)
r"""Price of the selected product."""


CheckoutPublicDiscountTypedDict = TypeAliasType(
    "CheckoutPublicDiscountTypedDict",
    Union[
        CheckoutDiscountPercentageOnceForeverDurationTypedDict,
        CheckoutDiscountFixedOnceForeverDurationTypedDict,
        CheckoutDiscountPercentageRepeatDurationTypedDict,
        CheckoutDiscountFixedRepeatDurationTypedDict,
    ],
)


CheckoutPublicDiscount = TypeAliasType(
    "CheckoutPublicDiscount",
    Union[
        CheckoutDiscountPercentageOnceForeverDuration,
        CheckoutDiscountFixedOnceForeverDuration,
        CheckoutDiscountPercentageRepeatDuration,
        CheckoutDiscountFixedRepeatDuration,
    ],
)


class CheckoutPublicTypedDict(TypedDict):
    r"""Checkout session data retrieved using the client secret."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    payment_processor: PaymentProcessor
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
    subtotal_amount: Nullable[int]
    r"""Subtotal amount in cents, including discounts and before tax."""
    total_amount: Nullable[int]
    r"""Total amount to pay in cents, including discounts and after tax."""
    product_id: str
    r"""ID of the product to checkout."""
    product_price_id: str
    r"""ID of the product price to checkout."""
    discount_id: Nullable[str]
    r"""ID of the discount applied to the checkout."""
    allow_discount_codes: bool
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""
    is_discount_applicable: bool
    r"""Whether the discount is applicable to the checkout. Typically, free and custom prices are not discountable."""
    is_free_product_price: bool
    r"""Whether the product price is free, regardless of discounts."""
    is_payment_required: bool
    r"""Whether the checkout requires payment, e.g. in case of free products or discounts that cover the total amount."""
    is_payment_setup_required: bool
    r"""Whether the checkout requires setting up a payment method, regardless of the amount, e.g. subscriptions that have first free cycles."""
    is_payment_form_required: bool
    r"""Whether the checkout requires a payment form, whether because of a payment or payment method setup."""
    customer_id: Nullable[str]
    customer_name: Nullable[str]
    r"""Name of the customer."""
    customer_email: Nullable[str]
    r"""Email address of the customer."""
    customer_ip_address: Nullable[str]
    customer_billing_address: Nullable[AddressTypedDict]
    customer_tax_id: Nullable[str]
    payment_processor_metadata: Dict[str, str]
    products: List[CheckoutProductTypedDict]
    r"""List of products available to select."""
    product: CheckoutProductTypedDict
    r"""Product data for a checkout session."""
    product_price: CheckoutPublicProductPriceTypedDict
    r"""Price of the selected product."""
    discount: Nullable[CheckoutPublicDiscountTypedDict]
    organization: OrganizationTypedDict
    attached_custom_fields: List[AttachedCustomFieldTypedDict]
    custom_field_data: NotRequired[Dict[str, CheckoutPublicCustomFieldDataTypedDict]]
    r"""Key-value object storing custom field values."""


class CheckoutPublic(BaseModel):
    r"""Checkout session data retrieved using the client secret."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    payment_processor: PaymentProcessor

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

    subtotal_amount: Nullable[int]
    r"""Subtotal amount in cents, including discounts and before tax."""

    total_amount: Nullable[int]
    r"""Total amount to pay in cents, including discounts and after tax."""

    product_id: str
    r"""ID of the product to checkout."""

    product_price_id: str
    r"""ID of the product price to checkout."""

    discount_id: Nullable[str]
    r"""ID of the discount applied to the checkout."""

    allow_discount_codes: bool
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""

    is_discount_applicable: bool
    r"""Whether the discount is applicable to the checkout. Typically, free and custom prices are not discountable."""

    is_free_product_price: bool
    r"""Whether the product price is free, regardless of discounts."""

    is_payment_required: bool
    r"""Whether the checkout requires payment, e.g. in case of free products or discounts that cover the total amount."""

    is_payment_setup_required: bool
    r"""Whether the checkout requires setting up a payment method, regardless of the amount, e.g. subscriptions that have first free cycles."""

    is_payment_form_required: bool
    r"""Whether the checkout requires a payment form, whether because of a payment or payment method setup."""

    customer_id: Nullable[str]

    customer_name: Nullable[str]
    r"""Name of the customer."""

    customer_email: Nullable[str]
    r"""Email address of the customer."""

    customer_ip_address: Nullable[str]

    customer_billing_address: Nullable[Address]

    customer_tax_id: Nullable[str]

    payment_processor_metadata: Dict[str, str]

    products: List[CheckoutProduct]
    r"""List of products available to select."""

    product: CheckoutProduct
    r"""Product data for a checkout session."""

    product_price: CheckoutPublicProductPrice
    r"""Price of the selected product."""

    discount: Nullable[CheckoutPublicDiscount]

    organization: Organization

    attached_custom_fields: List[AttachedCustomField]

    custom_field_data: Optional[Dict[str, CheckoutPublicCustomFieldData]] = None
    r"""Key-value object storing custom field values."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["custom_field_data"]
        nullable_fields = [
            "modified_at",
            "embed_origin",
            "amount",
            "tax_amount",
            "currency",
            "subtotal_amount",
            "total_amount",
            "discount_id",
            "customer_id",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
            "discount",
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
