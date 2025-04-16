"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfieldselectproperties import (
    CustomFieldSelectProperties,
    CustomFieldSelectPropertiesTypedDict,
)
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Literal, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


CustomFieldSelectMetadataTypedDict = TypeAliasType(
    "CustomFieldSelectMetadataTypedDict", Union[str, int, bool]
)


CustomFieldSelectMetadata = TypeAliasType(
    "CustomFieldSelectMetadata", Union[str, int, bool]
)


class CustomFieldSelectTypedDict(TypedDict):
    r"""Schema for a custom field of type select."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    metadata: Dict[str, CustomFieldSelectMetadataTypedDict]
    slug: str
    r"""Identifier of the custom field. It'll be used as key when storing the value."""
    name: str
    r"""Name of the custom field."""
    organization_id: str
    r"""The ID of the organization owning the custom field."""
    properties: CustomFieldSelectPropertiesTypedDict
    type: Literal["select"]


class CustomFieldSelect(BaseModel):
    r"""Schema for a custom field of type select."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    metadata: Dict[str, CustomFieldSelectMetadata]

    slug: str
    r"""Identifier of the custom field. It'll be used as key when storing the value."""

    name: str
    r"""Name of the custom field."""

    organization_id: str
    r"""The ID of the organization owning the custom field."""

    properties: CustomFieldSelectProperties

    TYPE: Annotated[
        Annotated[Literal["select"], AfterValidator(validate_const("select"))],
        pydantic.Field(alias="type"),
    ] = "select"

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
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
