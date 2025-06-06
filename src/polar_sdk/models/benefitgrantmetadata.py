"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefittype import BenefitType
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class BenefitGrantMetadataTypedDict(TypedDict):
    benefit_id: str
    benefit_grant_id: str
    benefit_type: BenefitType


class BenefitGrantMetadata(BaseModel):
    benefit_id: str

    benefit_grant_id: str

    benefit_type: BenefitType
