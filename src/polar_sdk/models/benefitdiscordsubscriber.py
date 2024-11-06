"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitdiscordsubscriberproperties import (
    BenefitDiscordSubscriberProperties,
    BenefitDiscordSubscriberPropertiesTypedDict,
)
from .benefitgrantsubscriber import (
    BenefitGrantSubscriber,
    BenefitGrantSubscriberTypedDict,
)
from .organization import Organization, OrganizationTypedDict
from datetime import datetime
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List
from typing_extensions import Annotated, TypedDict


class BenefitDiscordSubscriberType(str, Enum):
    DISCORD = "discord"


class BenefitDiscordSubscriberTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the benefit."""
    description: str
    r"""The description of the benefit."""
    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""
    deletable: bool
    r"""Whether the benefit is deletable."""
    organization_id: str
    r"""The ID of the organization owning the benefit."""
    grants: List[BenefitGrantSubscriberTypedDict]
    organization: OrganizationTypedDict
    properties: BenefitDiscordSubscriberPropertiesTypedDict
    r"""Properties available to subscribers for a benefit of type `discord`."""
    type: BenefitDiscordSubscriberType


class BenefitDiscordSubscriber(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the benefit."""

    description: str
    r"""The description of the benefit."""

    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""

    deletable: bool
    r"""Whether the benefit is deletable."""

    organization_id: str
    r"""The ID of the organization owning the benefit."""

    grants: List[BenefitGrantSubscriber]

    organization: Organization

    properties: BenefitDiscordSubscriberProperties
    r"""Properties available to subscribers for a benefit of type `discord`."""

    TYPE: Annotated[
        Annotated[
            BenefitDiscordSubscriberType,
            AfterValidator(validate_const(BenefitDiscordSubscriberType.DISCORD)),
        ],
        pydantic.Field(alias="type"),
    ] = BenefitDiscordSubscriberType.DISCORD

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
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
