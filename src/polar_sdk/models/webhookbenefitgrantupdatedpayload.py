"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitgrantwebhook import BenefitGrantWebhook, BenefitGrantWebhookTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookBenefitGrantUpdatedPayloadType(str, Enum):
    BENEFIT_GRANT_UPDATED = "benefit_grant.updated"


class WebhookBenefitGrantUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a new benefit grant is updated.

    **Discord & Slack support:** Basic
    """

    data: BenefitGrantWebhookTypedDict
    type: WebhookBenefitGrantUpdatedPayloadType


class WebhookBenefitGrantUpdatedPayload(BaseModel):
    r"""Sent when a new benefit grant is updated.

    **Discord & Slack support:** Basic
    """

    data: BenefitGrantWebhook

    TYPE: Annotated[
        Annotated[
            WebhookBenefitGrantUpdatedPayloadType,
            AfterValidator(
                validate_const(
                    WebhookBenefitGrantUpdatedPayloadType.BENEFIT_GRANT_UPDATED
                )
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookBenefitGrantUpdatedPayloadType.BENEFIT_GRANT_UPDATED