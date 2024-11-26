"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfieldcheckboxproperties import (
    CustomFieldCheckboxProperties,
    CustomFieldCheckboxPropertiesTypedDict,
)
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CustomFieldUpdateCheckboxMetadataTypedDict = TypeAliasType(
    "CustomFieldUpdateCheckboxMetadataTypedDict", Union[str, int, bool]
)


CustomFieldUpdateCheckboxMetadata = TypeAliasType(
    "CustomFieldUpdateCheckboxMetadata", Union[str, int, bool]
)


class CustomFieldUpdateCheckboxType(str, Enum):
    CHECKBOX = "checkbox"


class CustomFieldUpdateCheckboxTypedDict(TypedDict):
    r"""Schema to update a custom field of type checkbox."""

    metadata: NotRequired[
        Nullable[Dict[str, CustomFieldUpdateCheckboxMetadataTypedDict]]
    ]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    name: NotRequired[Nullable[str]]
    slug: NotRequired[Nullable[str]]
    type: CustomFieldUpdateCheckboxType
    properties: NotRequired[Nullable[CustomFieldCheckboxPropertiesTypedDict]]


class CustomFieldUpdateCheckbox(BaseModel):
    r"""Schema to update a custom field of type checkbox."""

    metadata: OptionalNullable[Dict[str, CustomFieldUpdateCheckboxMetadata]] = UNSET
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    name: OptionalNullable[str] = UNSET

    slug: OptionalNullable[str] = UNSET

    TYPE: Annotated[
        Annotated[
            CustomFieldUpdateCheckboxType,
            AfterValidator(validate_const(CustomFieldUpdateCheckboxType.CHECKBOX)),
        ],
        pydantic.Field(alias="type"),
    ] = CustomFieldUpdateCheckboxType.CHECKBOX

    properties: OptionalNullable[CustomFieldCheckboxProperties] = UNSET

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
