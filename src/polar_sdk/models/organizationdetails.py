"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SwitchingFrom(str, Enum):
    PADDLE = "paddle"
    LEMON_SQUEEZY = "lemon_squeezy"
    GUMROAD = "gumroad"
    STRIPE = "stripe"
    OTHER = "other"


class OrganizationDetailsTypedDict(TypedDict):
    about: str
    r"""Brief information about you and your business."""
    product_description: str
    r"""Description of digital products being sold."""
    intended_use: str
    r"""How the organization will integrate and use Polar."""
    customer_acquisition: List[str]
    r"""Main customer acquisition channels."""
    future_annual_revenue: int
    r"""Estimated revenue in the next 12 months"""
    switching: NotRequired[bool]
    r"""Switching from another platform?"""
    switching_from: NotRequired[Nullable[SwitchingFrom]]
    r"""Which platform the organization is migrating from."""
    previous_annual_revenue: NotRequired[int]
    r"""Revenue from last year if applicable."""


class OrganizationDetails(BaseModel):
    about: str
    r"""Brief information about you and your business."""

    product_description: str
    r"""Description of digital products being sold."""

    intended_use: str
    r"""How the organization will integrate and use Polar."""

    customer_acquisition: List[str]
    r"""Main customer acquisition channels."""

    future_annual_revenue: int
    r"""Estimated revenue in the next 12 months"""

    switching: Optional[bool] = True
    r"""Switching from another platform?"""

    switching_from: OptionalNullable[SwitchingFrom] = UNSET
    r"""Which platform the organization is migrating from."""

    previous_annual_revenue: Optional[int] = 0
    r"""Revenue from last year if applicable."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["switching", "switching_from", "previous_annual_revenue"]
        nullable_fields = ["switching_from"]
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
