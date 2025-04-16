"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercancellationreason import CustomerCancellationReason
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class CustomerSubscriptionCancelTypedDict(TypedDict):
    cancel_at_period_end: NotRequired[Nullable[bool]]
    r"""Cancel an active subscription once the current period ends.

    Or uncancel a subscription currently set to be revoked at period end.
    """
    cancellation_reason: NotRequired[Nullable[CustomerCancellationReason]]
    r"""Customers reason for cancellation.

    * `too_expensive`: Too expensive for the customer.
    * `missing_features`: Customer is missing certain features.
    * `switched_service`: Customer switched to another service.
    * `unused`: Customer is not using it enough.
    * `customer_service`: Customer is not satisfied with the customer service.
    * `low_quality`: Customer is unhappy with the quality.
    * `too_complex`: Customer considers the service too complicated.
    * `other`: Other reason(s).
    """
    cancellation_comment: NotRequired[Nullable[str]]
    r"""Customer feedback and why they decided to cancel."""


class CustomerSubscriptionCancel(BaseModel):
    cancel_at_period_end: OptionalNullable[bool] = UNSET
    r"""Cancel an active subscription once the current period ends.

    Or uncancel a subscription currently set to be revoked at period end.
    """

    cancellation_reason: OptionalNullable[CustomerCancellationReason] = UNSET
    r"""Customers reason for cancellation.

    * `too_expensive`: Too expensive for the customer.
    * `missing_features`: Customer is missing certain features.
    * `switched_service`: Customer switched to another service.
    * `unused`: Customer is not using it enough.
    * `customer_service`: Customer is not satisfied with the customer service.
    * `low_quality`: Customer is unhappy with the quality.
    * `too_complex`: Customer considers the service too complicated.
    * `other`: Other reason(s).
    """

    cancellation_comment: OptionalNullable[str] = UNSET
    r"""Customer feedback and why they decided to cancel."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "cancel_at_period_end",
            "cancellation_reason",
            "cancellation_comment",
        ]
        nullable_fields = [
            "cancel_at_period_end",
            "cancellation_reason",
            "cancellation_comment",
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
