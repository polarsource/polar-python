"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitgrantwebhook import BenefitGrantWebhook, BenefitGrantWebhookTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
import pydantic
from typing import Final, TypedDict
from typing_extensions import Annotated


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

    # fmt: off
    TYPE: Annotated[Final[WebhookBenefitGrantUpdatedPayloadType], pydantic.Field(alias="type")] = WebhookBenefitGrantUpdatedPayloadType.BENEFIT_GRANT_UPDATED # type: ignore
    # fmt: on
