"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class OrderItemSchemaTypedDict(TypedDict):
    r"""An order line item."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    label: str
    r"""Description of the line item charge."""
    amount: int
    r"""Amount in cents, before discounts and taxes."""
    tax_amount: int
    r"""Sales tax amount in cents."""
    proration: bool
    r"""Whether this charge is due to a proration."""
    product_price_id: Nullable[str]
    r"""Associated price ID, if any."""


class OrderItemSchema(BaseModel):
    r"""An order line item."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    label: str
    r"""Description of the line item charge."""

    amount: int
    r"""Amount in cents, before discounts and taxes."""

    tax_amount: int
    r"""Sales tax amount in cents."""

    proration: bool
    r"""Whether this charge is due to a proration."""

    product_price_id: Nullable[str]
    r"""Associated price ID, if any."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "product_price_id"]
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
