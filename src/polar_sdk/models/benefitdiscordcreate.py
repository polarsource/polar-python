"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitdiscordcreateproperties import (
    BenefitDiscordCreateProperties,
    BenefitDiscordCreatePropertiesTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


BenefitDiscordCreateMetadataTypedDict = TypeAliasType(
    "BenefitDiscordCreateMetadataTypedDict", Union[str, int, float, bool]
)


BenefitDiscordCreateMetadata = TypeAliasType(
    "BenefitDiscordCreateMetadata", Union[str, int, float, bool]
)


class BenefitDiscordCreateTypedDict(TypedDict):
    description: str
    r"""The description of the benefit. Will be displayed on products having this benefit."""
    properties: BenefitDiscordCreatePropertiesTypedDict
    r"""Properties to create a benefit of type `discord`."""
    metadata: NotRequired[Dict[str, BenefitDiscordCreateMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    type: Literal["discord"]
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the benefit. **Required unless you use an organization token.**"""


class BenefitDiscordCreate(BaseModel):
    description: str
    r"""The description of the benefit. Will be displayed on products having this benefit."""

    properties: BenefitDiscordCreateProperties
    r"""Properties to create a benefit of type `discord`."""

    metadata: Optional[Dict[str, BenefitDiscordCreateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    TYPE: Annotated[
        Annotated[Literal["discord"], AfterValidator(validate_const("discord"))],
        pydantic.Field(alias="type"),
    ] = "discord"

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the benefit. **Required unless you use an organization token.**"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata", "organization_id"]
        nullable_fields = ["organization_id"]
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
