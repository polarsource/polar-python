"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercancellationreason import CustomerCancellationReason
from .subscriptionrecurringinterval import SubscriptionRecurringInterval
from .subscriptionstatus import SubscriptionStatus
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class CustomerOrderSubscriptionTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    amount: Nullable[int]
    currency: Nullable[str]
    recurring_interval: SubscriptionRecurringInterval
    status: SubscriptionStatus
    current_period_start: datetime
    current_period_end: Nullable[datetime]
    cancel_at_period_end: bool
    canceled_at: Nullable[datetime]
    started_at: Nullable[datetime]
    ends_at: Nullable[datetime]
    ended_at: Nullable[datetime]
    customer_id: str
    product_id: str
    price_id: str
    discount_id: Nullable[str]
    checkout_id: Nullable[str]
    customer_cancellation_reason: Nullable[CustomerCancellationReason]
    customer_cancellation_comment: Nullable[str]


class CustomerOrderSubscription(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    amount: Nullable[int]

    currency: Nullable[str]

    recurring_interval: SubscriptionRecurringInterval

    status: SubscriptionStatus

    current_period_start: datetime

    current_period_end: Nullable[datetime]

    cancel_at_period_end: bool

    canceled_at: Nullable[datetime]

    started_at: Nullable[datetime]

    ends_at: Nullable[datetime]

    ended_at: Nullable[datetime]

    customer_id: str

    product_id: str

    price_id: str

    discount_id: Nullable[str]

    checkout_id: Nullable[str]

    customer_cancellation_reason: Nullable[CustomerCancellationReason]

    customer_cancellation_comment: Nullable[str]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "amount",
            "currency",
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
