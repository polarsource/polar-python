"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefit import Benefit, BenefitTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookBenefitUpdatedPayloadType(str, Enum):
    BENEFIT_UPDATED = "benefit.updated"


class WebhookBenefitUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a benefit is updated.

    **Discord & Slack support:** Basic
    """

    data: BenefitTypedDict
    type: WebhookBenefitUpdatedPayloadType


class WebhookBenefitUpdatedPayload(BaseModel):
    r"""Sent when a benefit is updated.

    **Discord & Slack support:** Basic
    """

    data: Benefit

    TYPE: Annotated[
        Annotated[
            WebhookBenefitUpdatedPayloadType,
            AfterValidator(
                validate_const(WebhookBenefitUpdatedPayloadType.BENEFIT_UPDATED)
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookBenefitUpdatedPayloadType.BENEFIT_UPDATED
