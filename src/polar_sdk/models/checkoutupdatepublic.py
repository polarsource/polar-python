"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


CheckoutUpdatePublicCustomFieldDataTypedDict = TypeAliasType(
    "CheckoutUpdatePublicCustomFieldDataTypedDict", Union[str, int, bool, datetime]
)


CheckoutUpdatePublicCustomFieldData = TypeAliasType(
    "CheckoutUpdatePublicCustomFieldData", Union[str, int, bool, datetime]
)


class CheckoutUpdatePublicTypedDict(TypedDict):
    r"""Update an existing checkout session using the client secret."""

    custom_field_data: NotRequired[
        Nullable[Dict[str, CheckoutUpdatePublicCustomFieldDataTypedDict]]
    ]
    r"""Key-value object storing custom field values."""
    product_price_id: NotRequired[Nullable[str]]
    r"""ID of the product price to checkout. Must correspond to a price linked to the same product."""
    amount: NotRequired[Nullable[int]]
    customer_name: NotRequired[Nullable[str]]
    customer_email: NotRequired[Nullable[str]]
    customer_billing_address: NotRequired[Nullable[AddressTypedDict]]
    customer_tax_id: NotRequired[Nullable[str]]
    discount_code: NotRequired[Nullable[str]]
    r"""Discount code to apply to the checkout."""


class CheckoutUpdatePublic(BaseModel):
    r"""Update an existing checkout session using the client secret."""

    custom_field_data: OptionalNullable[
        Dict[str, CheckoutUpdatePublicCustomFieldData]
    ] = UNSET
    r"""Key-value object storing custom field values."""

    product_price_id: OptionalNullable[str] = UNSET
    r"""ID of the product price to checkout. Must correspond to a price linked to the same product."""

    amount: OptionalNullable[int] = UNSET

    customer_name: OptionalNullable[str] = UNSET

    customer_email: OptionalNullable[str] = UNSET

    customer_billing_address: OptionalNullable[Address] = UNSET

    customer_tax_id: OptionalNullable[str] = UNSET

    discount_code: OptionalNullable[str] = UNSET
    r"""Discount code to apply to the checkout."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "custom_field_data",
            "product_price_id",
            "amount",
            "customer_name",
            "customer_email",
            "customer_billing_address",
            "customer_tax_id",
            "discount_code",
        ]
        nullable_fields = [
            "custom_field_data",
            "product_price_id",
            "amount",
            "customer_name",
            "customer_email",
            "customer_billing_address",
            "customer_tax_id",
            "discount_code",
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
