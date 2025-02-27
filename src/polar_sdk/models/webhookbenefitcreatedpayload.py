"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefit import Benefit, BenefitTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookBenefitCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new benefit is created.

    **Discord & Slack support:** Basic
    """

    data: BenefitTypedDict
    type: Literal["benefit.created"]


class WebhookBenefitCreatedPayload(BaseModel):
    r"""Sent when a new benefit is created.

    **Discord & Slack support:** Basic
    """

    data: Benefit

    TYPE: Annotated[
        Annotated[
            Literal["benefit.created"],
            AfterValidator(validate_const("benefit.created")),
        ],
        pydantic.Field(alias="type"),
    ] = "benefit.created"
