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
from .paymentprocessor import PaymentProcessor
from .productprice import ProductPrice, ProductPriceTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CheckoutCustomFieldDataTypedDict = TypeAliasType(
    "CheckoutCustomFieldDataTypedDict", Union[str, int, bool, datetime]
)


CheckoutCustomFieldData = TypeAliasType(
    "CheckoutCustomFieldData", Union[str, int, bool, datetime]
)


CheckoutMetadataTypedDict = TypeAliasType(
    "CheckoutMetadataTypedDict", Union[str, int, bool]
)


CheckoutMetadata = TypeAliasType("CheckoutMetadata", Union[str, int, bool])


CheckoutProductPriceTypedDict = TypeAliasType(
    "CheckoutProductPriceTypedDict",
    Union[LegacyRecurringProductPriceTypedDict, ProductPriceTypedDict],
)
r"""Price of the selected product."""


CheckoutProductPrice = TypeAliasType(
    "CheckoutProductPrice", Union[LegacyRecurringProductPrice, ProductPrice]
)
r"""Price of the selected product."""


CheckoutDiscountTypedDict = TypeAliasType(
    "CheckoutDiscountTypedDict",
    Union[
        CheckoutDiscountPercentageOnceForeverDurationTypedDict,
        CheckoutDiscountFixedOnceForeverDurationTypedDict,
        CheckoutDiscountPercentageRepeatDurationTypedDict,
        CheckoutDiscountFixedRepeatDurationTypedDict,
    ],
)


CheckoutDiscount = TypeAliasType(
    "CheckoutDiscount",
    Union[
        CheckoutDiscountPercentageOnceForeverDuration,
        CheckoutDiscountFixedOnceForeverDuration,
        CheckoutDiscountPercentageRepeatDuration,
        CheckoutDiscountFixedRepeatDuration,
    ],
)


CustomerMetadataTypedDict = TypeAliasType(
    "CustomerMetadataTypedDict", Union[str, int, bool]
)


CustomerMetadata = TypeAliasType("CustomerMetadata", Union[str, int, bool])


class CheckoutTypedDict(TypedDict):
    r"""Checkout session data retrieved using an access token."""

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
    amount: int
    r"""Amount in cents, before discounts and taxes."""
    discount_amount: int
    r"""Discount amount in cents."""
    net_amount: int
    r"""Amount in cents, after discounts but before taxes."""
    tax_amount: Nullable[int]
    r"""Sales tax amount in cents. If `null`, it means there is no enough information yet to calculate it."""
    total_amount: int
    r"""Amount in cents, after discounts and taxes."""
    currency: str
    r"""Currency code of the checkout session."""
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
    subtotal_amount: Nullable[int]
    metadata: Dict[str, CheckoutMetadataTypedDict]
    customer_external_id: Nullable[str]
    r"""ID of the customer in your system. If a matching customer exists on Polar, the resulting order will be linked to this customer. Otherwise, a new customer will be created with this external ID set."""
    products: List[CheckoutProductTypedDict]
    r"""List of products available to select."""
    product: CheckoutProductTypedDict
    r"""Product data for a checkout session."""
    product_price: CheckoutProductPriceTypedDict
    r"""Price of the selected product."""
    discount: Nullable[CheckoutDiscountTypedDict]
    subscription_id: Nullable[str]
    attached_custom_fields: List[AttachedCustomFieldTypedDict]
    customer_metadata: Dict[str, CustomerMetadataTypedDict]
    custom_field_data: NotRequired[
        Dict[str, Nullable[CheckoutCustomFieldDataTypedDict]]
    ]
    r"""Key-value object storing custom field values."""


class Checkout(BaseModel):
    r"""Checkout session data retrieved using an access token."""

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

    amount: int
    r"""Amount in cents, before discounts and taxes."""

    discount_amount: int
    r"""Discount amount in cents."""

    net_amount: int
    r"""Amount in cents, after discounts but before taxes."""

    tax_amount: Nullable[int]
    r"""Sales tax amount in cents. If `null`, it means there is no enough information yet to calculate it."""

    total_amount: int
    r"""Amount in cents, after discounts and taxes."""

    currency: str
    r"""Currency code of the checkout session."""

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

    subtotal_amount: Annotated[
        Nullable[int],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    metadata: Dict[str, CheckoutMetadata]

    customer_external_id: Nullable[str]
    r"""ID of the customer in your system. If a matching customer exists on Polar, the resulting order will be linked to this customer. Otherwise, a new customer will be created with this external ID set."""

    products: List[CheckoutProduct]
    r"""List of products available to select."""

    product: CheckoutProduct
    r"""Product data for a checkout session."""

    product_price: CheckoutProductPrice
    r"""Price of the selected product."""

    discount: Nullable[CheckoutDiscount]

    subscription_id: Nullable[str]

    attached_custom_fields: List[AttachedCustomField]

    customer_metadata: Dict[str, CustomerMetadata]

    custom_field_data: Optional[Dict[str, Nullable[CheckoutCustomFieldData]]] = None
    r"""Key-value object storing custom field values."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["custom_field_data"]
        nullable_fields = [
            "modified_at",
            "embed_origin",
            "tax_amount",
            "discount_id",
            "customer_id",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
            "subtotal_amount",
            "customer_external_id",
            "discount",
            "subscription_id",
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
