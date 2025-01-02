"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfieldcheckboxproperties import (
    CustomFieldCheckboxProperties,
    CustomFieldCheckboxPropertiesTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Literal, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CustomFieldUpdateCheckboxMetadataTypedDict = TypeAliasType(
    "CustomFieldUpdateCheckboxMetadataTypedDict", Union[str, int, bool]
)


CustomFieldUpdateCheckboxMetadata = TypeAliasType(
    "CustomFieldUpdateCheckboxMetadata", Union[str, int, bool]
)


class CustomFieldUpdateCheckboxTypedDict(TypedDict):
    r"""Schema to update a custom field of type checkbox."""

    metadata: NotRequired[
        Nullable[Dict[str, CustomFieldUpdateCheckboxMetadataTypedDict]]
    ]
    name: NotRequired[Nullable[str]]
    slug: NotRequired[Nullable[str]]
    type: Literal["checkbox"]
    properties: NotRequired[Nullable[CustomFieldCheckboxPropertiesTypedDict]]


class CustomFieldUpdateCheckbox(BaseModel):
    r"""Schema to update a custom field of type checkbox."""

    metadata: OptionalNullable[Dict[str, CustomFieldUpdateCheckboxMetadata]] = UNSET

    name: OptionalNullable[str] = UNSET

    slug: OptionalNullable[str] = UNSET

    TYPE: Annotated[
        Annotated[Literal["checkbox"], AfterValidator(validate_const("checkbox"))],
        pydantic.Field(alias="type"),
    ] = "checkbox"

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
