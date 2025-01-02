"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriptionrecurringinterval import SubscriptionRecurringInterval
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ProductPriceRecurringFreeTypedDict(TypedDict):
    r"""A free recurring price for a product, i.e. a subscription."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the price."""
    is_archived: bool
    r"""Whether the price is archived and no longer available."""
    product_id: str
    r"""The ID of the product owning the price."""
    recurring_interval: SubscriptionRecurringInterval
    amount_type: Literal["free"]
    type: Literal["recurring"]
    r"""The type of the price."""


class ProductPriceRecurringFree(BaseModel):
    r"""A free recurring price for a product, i.e. a subscription."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the price."""

    is_archived: bool
    r"""Whether the price is archived and no longer available."""

    product_id: str
    r"""The ID of the product owning the price."""

    recurring_interval: SubscriptionRecurringInterval

    AMOUNT_TYPE: Annotated[
        Annotated[Literal["free"], AfterValidator(validate_const("free"))],
        pydantic.Field(alias="amount_type"),
    ] = "free"

    TYPE: Annotated[
        Annotated[Literal["recurring"], AfterValidator(validate_const("recurring"))],
        pydantic.Field(alias="type"),
    ] = "recurring"
    r"""The type of the price."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
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
