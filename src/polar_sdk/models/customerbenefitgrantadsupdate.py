"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class CustomerBenefitGrantAdsUpdateBenefitType(str, Enum):
    ADS = "ads"


class CustomerBenefitGrantAdsUpdateTypedDict(TypedDict):
    benefit_type: CustomerBenefitGrantAdsUpdateBenefitType


class CustomerBenefitGrantAdsUpdate(BaseModel):
    BENEFIT_TYPE: Annotated[
        Annotated[
            CustomerBenefitGrantAdsUpdateBenefitType,
            AfterValidator(
                validate_const(CustomerBenefitGrantAdsUpdateBenefitType.ADS)
            ),
        ],
        pydantic.Field(alias="benefit_type"),
    ] = CustomerBenefitGrantAdsUpdateBenefitType.ADS
