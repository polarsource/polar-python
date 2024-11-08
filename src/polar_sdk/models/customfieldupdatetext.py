"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfieldtextproperties import (
    CustomFieldTextProperties,
    CustomFieldTextPropertiesTypedDict,
)
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomFieldUpdateTextType(str, Enum):
    TEXT = "text"


class CustomFieldUpdateTextTypedDict(TypedDict):
    r"""Schema to update a custom field of type text."""

    metadata: NotRequired[Nullable[Dict[str, str]]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be a string with a maximum length of **500 characters**.
    You can store up to **50 key-value pairs**.
    """
    name: NotRequired[Nullable[str]]
    slug: NotRequired[Nullable[str]]
    type: CustomFieldUpdateTextType
    properties: NotRequired[Nullable[CustomFieldTextPropertiesTypedDict]]


class CustomFieldUpdateText(BaseModel):
    r"""Schema to update a custom field of type text."""

    metadata: OptionalNullable[Dict[str, str]] = UNSET
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be a string with a maximum length of **500 characters**.
    You can store up to **50 key-value pairs**.
    """

    name: OptionalNullable[str] = UNSET

    slug: OptionalNullable[str] = UNSET

    TYPE: Annotated[
        Annotated[
            CustomFieldUpdateTextType,
            AfterValidator(validate_const(CustomFieldUpdateTextType.TEXT)),
        ],
        pydantic.Field(alias="type"),
    ] = CustomFieldUpdateTextType.TEXT

    properties: OptionalNullable[CustomFieldTextProperties] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "name", "slug", "properties"]
        nullable_fields = ["metadata", "name", "slug", "properties"]
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
