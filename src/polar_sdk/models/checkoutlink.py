"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .checkoutlinkproduct import CheckoutLinkProduct, CheckoutLinkProductTypedDict
from .discountfixedonceforeverdurationbase import (
    DiscountFixedOnceForeverDurationBase,
    DiscountFixedOnceForeverDurationBaseTypedDict,
)
from .discountfixedrepeatdurationbase import (
    DiscountFixedRepeatDurationBase,
    DiscountFixedRepeatDurationBaseTypedDict,
)
from .discountpercentageonceforeverdurationbase import (
    DiscountPercentageOnceForeverDurationBase,
    DiscountPercentageOnceForeverDurationBaseTypedDict,
)
from .discountpercentagerepeatdurationbase import (
    DiscountPercentageRepeatDurationBase,
    DiscountPercentageRepeatDurationBaseTypedDict,
)
from .paymentprocessor import PaymentProcessor
from .productprice import ProductPrice, ProductPriceTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, Union
from typing_extensions import TypeAliasType, TypedDict


CheckoutLinkMetadataTypedDict = TypeAliasType(
    "CheckoutLinkMetadataTypedDict", Union[str, int, bool]
)


CheckoutLinkMetadata = TypeAliasType("CheckoutLinkMetadata", Union[str, int, bool])


CheckoutLinkDiscountTypedDict = TypeAliasType(
    "CheckoutLinkDiscountTypedDict",
    Union[
        DiscountPercentageOnceForeverDurationBaseTypedDict,
        DiscountFixedOnceForeverDurationBaseTypedDict,
        DiscountPercentageRepeatDurationBaseTypedDict,
        DiscountFixedRepeatDurationBaseTypedDict,
    ],
)


CheckoutLinkDiscount = TypeAliasType(
    "CheckoutLinkDiscount",
    Union[
        DiscountPercentageOnceForeverDurationBase,
        DiscountFixedOnceForeverDurationBase,
        DiscountPercentageRepeatDurationBase,
        DiscountFixedRepeatDurationBase,
    ],
)


class CheckoutLinkTypedDict(TypedDict):
    r"""Checkout link data."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    metadata: Dict[str, CheckoutLinkMetadataTypedDict]
    payment_processor: PaymentProcessor
    client_secret: str
    r"""Client secret used to access the checkout link."""
    success_url: Nullable[str]
    r"""URL where the customer will be redirected after a successful payment."""
    label: Nullable[str]
    r"""Optional label to distinguish links internally"""
    allow_discount_codes: bool
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""
    product_id: str
    r"""ID of the product to checkout."""
    product_price_id: Nullable[str]
    r"""ID of the product price to checkout. First available price will be selected unless an explicit price ID is set."""
    discount_id: Nullable[str]
    r"""ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored."""
    product: CheckoutLinkProductTypedDict
    r"""Product data for a checkout link."""
    product_price: Nullable[ProductPriceTypedDict]
    discount: Nullable[CheckoutLinkDiscountTypedDict]
    url: str


class CheckoutLink(BaseModel):
    r"""Checkout link data."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    metadata: Dict[str, CheckoutLinkMetadata]

    payment_processor: PaymentProcessor

    client_secret: str
    r"""Client secret used to access the checkout link."""

    success_url: Nullable[str]
    r"""URL where the customer will be redirected after a successful payment."""

    label: Nullable[str]
    r"""Optional label to distinguish links internally"""

    allow_discount_codes: bool
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""

    product_id: str
    r"""ID of the product to checkout."""

    product_price_id: Nullable[str]
    r"""ID of the product price to checkout. First available price will be selected unless an explicit price ID is set."""

    discount_id: Nullable[str]
    r"""ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored."""

    product: CheckoutLinkProduct
    r"""Product data for a checkout link."""

    product_price: Nullable[ProductPrice]

    discount: Nullable[CheckoutLinkDiscount]

    url: str

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "success_url",
            "label",
            "product_price_id",
            "discount_id",
            "product_price",
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
