"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .taxidformat import TaxIDFormat
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


CustomerUpdateMetadataTypedDict = TypeAliasType(
    "CustomerUpdateMetadataTypedDict", Union[str, int, bool]
)


CustomerUpdateMetadata = TypeAliasType("CustomerUpdateMetadata", Union[str, int, bool])


CustomerUpdateTaxIDTypedDict = TypeAliasType(
    "CustomerUpdateTaxIDTypedDict", Union[str, TaxIDFormat]
)


CustomerUpdateTaxID = TypeAliasType("CustomerUpdateTaxID", Union[str, TaxIDFormat])


class CustomerUpdateTypedDict(TypedDict):
    metadata: NotRequired[Dict[str, CustomerUpdateMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    external_id: NotRequired[Nullable[str]]
    r"""The ID of the customer in your system. This must be unique within the organization. Once set, it can't be updated."""
    email: NotRequired[Nullable[str]]
    r"""The email address of the customer. This must be unique within the organization."""
    name: NotRequired[Nullable[str]]
    r"""The name of the customer."""
    billing_address: NotRequired[Nullable[AddressTypedDict]]
    tax_id: NotRequired[Nullable[List[Nullable[CustomerUpdateTaxIDTypedDict]]]]


class CustomerUpdate(BaseModel):
    metadata: Optional[Dict[str, CustomerUpdateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    external_id: OptionalNullable[str] = UNSET
    r"""The ID of the customer in your system. This must be unique within the organization. Once set, it can't be updated."""

    email: OptionalNullable[str] = UNSET
    r"""The email address of the customer. This must be unique within the organization."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the customer."""

    billing_address: OptionalNullable[Address] = UNSET

    tax_id: OptionalNullable[List[Nullable[CustomerUpdateTaxID]]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "external_id",
            "email",
            "name",
            "billing_address",
            "tax_id",
        ]
        nullable_fields = ["external_id", "email", "name", "billing_address", "tax_id"]
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
