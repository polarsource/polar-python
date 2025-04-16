"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercancellationreason import CustomerCancellationReason
from .subscriptionrecurringinterval import SubscriptionRecurringInterval
from .subscriptionstatus import SubscriptionStatus
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Dict, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


OrderSubscriptionMetadataTypedDict = TypeAliasType(
    "OrderSubscriptionMetadataTypedDict", Union[str, int, float, bool]
)


OrderSubscriptionMetadata = TypeAliasType(
    "OrderSubscriptionMetadata", Union[str, int, float, bool]
)


class OrderSubscriptionTypedDict(TypedDict):
    metadata: Dict[str, OrderSubscriptionMetadataTypedDict]
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
    price_id: str
    user_id: str


class OrderSubscription(BaseModel):
    metadata: Dict[str, OrderSubscriptionMetadata]

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

    price_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    user_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
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
