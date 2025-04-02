"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitgrantwebhook import BenefitGrantWebhook, BenefitGrantWebhookTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookBenefitGrantRevokedPayloadTypedDict(TypedDict):
    r"""Sent when a benefit grant is revoked.

    **Discord & Slack support:** Basic
    """

    data: BenefitGrantWebhookTypedDict
    type: Literal["benefit_grant.revoked"]


class WebhookBenefitGrantRevokedPayload(BaseModel):
    r"""Sent when a benefit grant is revoked.

    **Discord & Slack support:** Basic
    """

    data: BenefitGrantWebhook

    TYPE: Annotated[
        Annotated[
            Literal["benefit_grant.revoked"],
            AfterValidator(validate_const("benefit_grant.revoked")),
        ],
        pydantic.Field(alias="type"),
    ] = "benefit_grant.revoked"
