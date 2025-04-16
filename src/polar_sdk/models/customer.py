"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .taxidformat import TaxIDFormat
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Union
from typing_extensions import TypeAliasType, TypedDict


CustomerMetadata1TypedDict = TypeAliasType(
    "CustomerMetadata1TypedDict", Union[str, int, float, bool]
)


CustomerMetadata1 = TypeAliasType("CustomerMetadata1", Union[str, int, float, bool])


CustomerTaxIDTypedDict = TypeAliasType(
    "CustomerTaxIDTypedDict", Union[str, TaxIDFormat]
)


CustomerTaxID = TypeAliasType("CustomerTaxID", Union[str, TaxIDFormat])


class CustomerTypedDict(TypedDict):
    r"""A customer in an organization."""

    id: str
    r"""The ID of the customer."""
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    metadata: Dict[str, CustomerMetadata1TypedDict]
    external_id: Nullable[str]
    r"""The ID of the customer in your system. This must be unique within the organization. Once set, it can't be updated."""
    email: str
    r"""The email address of the customer. This must be unique within the organization."""
    email_verified: bool
    r"""Whether the customer email address is verified. The address is automatically verified when the customer accesses the customer portal using their email address."""
    name: Nullable[str]
    r"""The name of the customer."""
    billing_address: Nullable[AddressTypedDict]
    tax_id: Nullable[List[Nullable[CustomerTaxIDTypedDict]]]
    organization_id: str
    r"""The ID of the organization owning the customer."""
    deleted_at: Nullable[datetime]
    r"""Timestamp for when the customer was soft deleted."""
    avatar_url: str


class Customer(BaseModel):
    r"""A customer in an organization."""

    id: str
    r"""The ID of the customer."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    metadata: Dict[str, CustomerMetadata1]

    external_id: Nullable[str]
    r"""The ID of the customer in your system. This must be unique within the organization. Once set, it can't be updated."""

    email: str
    r"""The email address of the customer. This must be unique within the organization."""

    email_verified: bool
    r"""Whether the customer email address is verified. The address is automatically verified when the customer accesses the customer portal using their email address."""

    name: Nullable[str]
    r"""The name of the customer."""

    billing_address: Nullable[Address]

    tax_id: Nullable[List[Nullable[CustomerTaxID]]]

    organization_id: str
    r"""The ID of the organization owning the customer."""

    deleted_at: Nullable[datetime]
    r"""Timestamp for when the customer was soft deleted."""

    avatar_url: str

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "external_id",
            "name",
            "billing_address",
            "tax_id",
            "deleted_at",
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
