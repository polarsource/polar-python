"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfieldselectproperties import (
    CustomFieldSelectProperties,
    CustomFieldSelectPropertiesTypedDict,
)
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


CustomFieldCreateSelectMetadataTypedDict = Union[str, int, bool]


CustomFieldCreateSelectMetadata = Union[str, int, bool]


class CustomFieldCreateSelectType(str, Enum):
    SELECT = "select"


class CustomFieldCreateSelectTypedDict(TypedDict):
    r"""Schema to create a custom field of type select."""

    slug: str
    r"""Identifier of the custom field. It'll be used as key when storing the value. Must be unique across the organization.It can only contain ASCII letters, numbers and hyphens."""
    name: str
    r"""Name of the custom field."""
    properties: CustomFieldSelectPropertiesTypedDict
    metadata: NotRequired[Dict[str, CustomFieldCreateSelectMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:
    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    type: CustomFieldCreateSelectType
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the custom field. **Required unless you use an organization token.**"""


class CustomFieldCreateSelect(BaseModel):
    r"""Schema to create a custom field of type select."""

    slug: str
    r"""Identifier of the custom field. It'll be used as key when storing the value. Must be unique across the organization.It can only contain ASCII letters, numbers and hyphens."""

    name: str
    r"""Name of the custom field."""

    properties: CustomFieldSelectProperties

    metadata: Optional[Dict[str, CustomFieldCreateSelectMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:
    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    TYPE: Annotated[
        Annotated[
            CustomFieldCreateSelectType,
            AfterValidator(validate_const(CustomFieldCreateSelectType.SELECT)),
        ],
        pydantic.Field(alias="type"),
    ] = CustomFieldCreateSelectType.SELECT

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the custom field. **Required unless you use an organization token.**"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "organization_id"]
        nullable_fields = ["organization_id"]
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
