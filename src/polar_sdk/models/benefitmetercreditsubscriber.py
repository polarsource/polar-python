"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitmetercreditsubscriberproperties import (
    BenefitMeterCreditSubscriberProperties,
    BenefitMeterCreditSubscriberPropertiesTypedDict,
)
from .organization import Organization, OrganizationTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Literal, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


BenefitMeterCreditSubscriberMetadataTypedDict = TypeAliasType(
    "BenefitMeterCreditSubscriberMetadataTypedDict", Union[str, int, float, bool]
)


BenefitMeterCreditSubscriberMetadata = TypeAliasType(
    "BenefitMeterCreditSubscriberMetadata", Union[str, int, float, bool]
)


class BenefitMeterCreditSubscriberTypedDict(TypedDict):
    id: str
    r"""The ID of the benefit."""
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    description: str
    r"""The description of the benefit."""
    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""
    deletable: bool
    r"""Whether the benefit is deletable."""
    organization_id: str
    r"""The ID of the organization owning the benefit."""
    metadata: Dict[str, BenefitMeterCreditSubscriberMetadataTypedDict]
    organization: OrganizationTypedDict
    properties: BenefitMeterCreditSubscriberPropertiesTypedDict
    r"""Properties available to subscribers for a benefit of type `meter_unit`."""
    type: Literal["meter_credit"]


class BenefitMeterCreditSubscriber(BaseModel):
    id: str
    r"""The ID of the benefit."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    description: str
    r"""The description of the benefit."""

    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""

    deletable: bool
    r"""Whether the benefit is deletable."""

    organization_id: str
    r"""The ID of the organization owning the benefit."""

    metadata: Dict[str, BenefitMeterCreditSubscriberMetadata]

    organization: Organization

    properties: BenefitMeterCreditSubscriberProperties
    r"""Properties available to subscribers for a benefit of type `meter_unit`."""

    TYPE: Annotated[
        Annotated[
            Literal["meter_credit"], AfterValidator(validate_const("meter_credit"))
        ],
        pydantic.Field(alias="type"),
    ] = "meter_credit"

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
