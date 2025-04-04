"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class CustomerBenefitGrantDownloadablesUpdateTypedDict(TypedDict):
    benefit_type: Literal["downloadables"]


class CustomerBenefitGrantDownloadablesUpdate(BaseModel):
    BENEFIT_TYPE: Annotated[
        Annotated[
            Literal["downloadables"], AfterValidator(validate_const("downloadables"))
        ],
        pydantic.Field(alias="benefit_type"),
    ] = "downloadables"
