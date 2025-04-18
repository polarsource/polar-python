"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercancellationreason import CustomerCancellationReason
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscriptionRevokeTypedDict(TypedDict):
    customer_cancellation_reason: NotRequired[Nullable[CustomerCancellationReason]]
    r"""Customer reason for cancellation.

    Helpful to monitor reasons behind churn for future improvements.

    Only set this in case your own service is requesting the reason from the
    customer. Or you know based on direct conversations, i.e support, with
    the customer.

    * `too_expensive`: Too expensive for the customer.
    * `missing_features`: Customer is missing certain features.
    * `switched_service`: Customer switched to another service.
    * `unused`: Customer is not using it enough.
    * `customer_service`: Customer is not satisfied with the customer service.
    * `low_quality`: Customer is unhappy with the quality.
    * `too_complex`: Customer considers the service too complicated.
    * `other`: Other reason(s).
    """
    customer_cancellation_comment: NotRequired[Nullable[str]]
    r"""Customer feedback and why they decided to cancel.

    **IMPORTANT:**
    Do not use this to store internal notes! It's intended to be input
    from the customer and is therefore also available in their Polar
    purchases library.

    Only set this in case your own service is requesting the reason from the
    customer. Or you copy a message directly from a customer
    conversation, i.e support.
    """
    revoke: Literal[True]
    r"""Cancel and revoke an active subscription immediately"""


class SubscriptionRevoke(BaseModel):
    customer_cancellation_reason: OptionalNullable[CustomerCancellationReason] = UNSET
    r"""Customer reason for cancellation.

    Helpful to monitor reasons behind churn for future improvements.

    Only set this in case your own service is requesting the reason from the
    customer. Or you know based on direct conversations, i.e support, with
    the customer.

    * `too_expensive`: Too expensive for the customer.
    * `missing_features`: Customer is missing certain features.
    * `switched_service`: Customer switched to another service.
    * `unused`: Customer is not using it enough.
    * `customer_service`: Customer is not satisfied with the customer service.
    * `low_quality`: Customer is unhappy with the quality.
    * `too_complex`: Customer considers the service too complicated.
    * `other`: Other reason(s).
    """

    customer_cancellation_comment: OptionalNullable[str] = UNSET
    r"""Customer feedback and why they decided to cancel.

    **IMPORTANT:**
    Do not use this to store internal notes! It's intended to be input
    from the customer and is therefore also available in their Polar
    purchases library.

    Only set this in case your own service is requesting the reason from the
    customer. Or you copy a message directly from a customer
    conversation, i.e support.
    """

    REVOKE: Annotated[
        Annotated[Literal[True], AfterValidator(validate_const(True))],
        pydantic.Field(alias="revoke"),
    ] = True
    r"""Cancel and revoke an active subscription immediately"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "customer_cancellation_reason",
            "customer_cancellation_comment",
        ]
        nullable_fields = [
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
