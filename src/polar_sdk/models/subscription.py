"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercancellationreason import CustomerCancellationReason
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
from .legacyrecurringproductprice import (
    LegacyRecurringProductPrice,
    LegacyRecurringProductPriceTypedDict,
)
from .product import Product, ProductTypedDict
from .productprice import ProductPrice, ProductPriceTypedDict
from .subscriptioncustomer import SubscriptionCustomer, SubscriptionCustomerTypedDict
from .subscriptionmeter import SubscriptionMeter, SubscriptionMeterTypedDict
from .subscriptionrecurringinterval import SubscriptionRecurringInterval
from .subscriptionstatus import SubscriptionStatus
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


MetadataTypedDict = TypeAliasType("MetadataTypedDict", Union[str, int, float, bool])


Metadata = TypeAliasType("Metadata", Union[str, int, float, bool])


CustomFieldDataTypedDict = TypeAliasType(
    "CustomFieldDataTypedDict", Union[str, int, bool, datetime]
)


CustomFieldData = TypeAliasType("CustomFieldData", Union[str, int, bool, datetime])


SubscriptionDiscountTypedDict = TypeAliasType(
    "SubscriptionDiscountTypedDict",
    Union[
        DiscountPercentageOnceForeverDurationBaseTypedDict,
        DiscountFixedOnceForeverDurationBaseTypedDict,
        DiscountPercentageRepeatDurationBaseTypedDict,
        DiscountFixedRepeatDurationBaseTypedDict,
    ],
)


SubscriptionDiscount = TypeAliasType(
    "SubscriptionDiscount",
    Union[
        DiscountPercentageOnceForeverDurationBase,
        DiscountFixedOnceForeverDurationBase,
        DiscountPercentageRepeatDurationBase,
        DiscountFixedRepeatDurationBase,
    ],
)


SubscriptionPricesTypedDict = TypeAliasType(
    "SubscriptionPricesTypedDict",
    Union[LegacyRecurringProductPriceTypedDict, ProductPriceTypedDict],
)


SubscriptionPrices = TypeAliasType(
    "SubscriptionPrices", Union[LegacyRecurringProductPrice, ProductPrice]
)


class SubscriptionTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    amount: int
    r"""The amount of the subscription."""
    currency: str
    r"""The currency of the subscription."""
    recurring_interval: SubscriptionRecurringInterval
    status: SubscriptionStatus
    current_period_start: datetime
    r"""The start timestamp of the current billing period."""
    current_period_end: Nullable[datetime]
    r"""The end timestamp of the current billing period."""
    cancel_at_period_end: bool
    r"""Whether the subscription will be canceled at the end of the current period."""
    canceled_at: Nullable[datetime]
    r"""The timestamp when the subscription was canceled. The subscription might still be active if `cancel_at_period_end` is `true`."""
    started_at: Nullable[datetime]
    r"""The timestamp when the subscription started."""
    ends_at: Nullable[datetime]
    r"""The timestamp when the subscription will end."""
    ended_at: Nullable[datetime]
    r"""The timestamp when the subscription ended."""
    customer_id: str
    r"""The ID of the subscribed customer."""
    product_id: str
    r"""The ID of the subscribed product."""
    discount_id: Nullable[str]
    r"""The ID of the applied discount, if any."""
    checkout_id: Nullable[str]
    customer_cancellation_reason: Nullable[CustomerCancellationReason]
    customer_cancellation_comment: Nullable[str]
    metadata: Dict[str, MetadataTypedDict]
    customer: SubscriptionCustomerTypedDict
    product: ProductTypedDict
    r"""A product."""
    discount: Nullable[SubscriptionDiscountTypedDict]
    prices: List[SubscriptionPricesTypedDict]
    r"""List of enabled prices for the subscription."""
    meters: List[SubscriptionMeterTypedDict]
    r"""List of meters associated with the subscription."""
    custom_field_data: NotRequired[Dict[str, Nullable[CustomFieldDataTypedDict]]]
    r"""Key-value object storing custom field values."""


class Subscription(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    amount: int
    r"""The amount of the subscription."""

    currency: str
    r"""The currency of the subscription."""

    recurring_interval: SubscriptionRecurringInterval

    status: SubscriptionStatus

    current_period_start: datetime
    r"""The start timestamp of the current billing period."""

    current_period_end: Nullable[datetime]
    r"""The end timestamp of the current billing period."""

    cancel_at_period_end: bool
    r"""Whether the subscription will be canceled at the end of the current period."""

    canceled_at: Nullable[datetime]
    r"""The timestamp when the subscription was canceled. The subscription might still be active if `cancel_at_period_end` is `true`."""

    started_at: Nullable[datetime]
    r"""The timestamp when the subscription started."""

    ends_at: Nullable[datetime]
    r"""The timestamp when the subscription will end."""

    ended_at: Nullable[datetime]
    r"""The timestamp when the subscription ended."""

    customer_id: str
    r"""The ID of the subscribed customer."""

    product_id: str
    r"""The ID of the subscribed product."""

    discount_id: Nullable[str]
    r"""The ID of the applied discount, if any."""

    checkout_id: Nullable[str]

    customer_cancellation_reason: Nullable[CustomerCancellationReason]

    customer_cancellation_comment: Nullable[str]

    metadata: Dict[str, Metadata]

    customer: SubscriptionCustomer

    product: Product
    r"""A product."""

    discount: Nullable[SubscriptionDiscount]

    prices: List[SubscriptionPrices]
    r"""List of enabled prices for the subscription."""

    meters: List[SubscriptionMeter]
    r"""List of meters associated with the subscription."""

    custom_field_data: Optional[Dict[str, Nullable[CustomFieldData]]] = None
    r"""Key-value object storing custom field values."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["custom_field_data"]
        nullable_fields = [
            "modified_at",
            "current_period_end",
            "canceled_at",
            "started_at",
            "ends_at",
            "ended_at",
            "discount_id",
            "checkout_id",
            "customer_cancellation_reason",
            "customer_cancellation_comment",
            "discount",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
