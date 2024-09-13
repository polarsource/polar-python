"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriptiontiertype import SubscriptionTierType
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import Annotated


class OrderProductTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the product."""
    name: str
    r"""The name of the product."""
    description: Nullable[str]
    r"""The description of the product."""
    is_recurring: bool
    r"""Whether the product is a subscription tier."""
    is_archived: bool
    r"""Whether the product is archived and no longer available."""
    organization_id: str
    r"""The ID of the organization owning the product."""
    type: Nullable[SubscriptionTierType]
    is_highlighted: Nullable[bool]


class OrderProduct(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the product."""

    name: str
    r"""The name of the product."""

    description: Nullable[str]
    r"""The description of the product."""

    is_recurring: bool
    r"""Whether the product is a subscription tier."""

    is_archived: bool
    r"""Whether the product is archived and no longer available."""

    organization_id: str
    r"""The ID of the organization owning the product."""

    type: Annotated[
        Nullable[SubscriptionTierType],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    is_highlighted: Annotated[
        Nullable[bool],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "description", "type", "is_highlighted"]
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
