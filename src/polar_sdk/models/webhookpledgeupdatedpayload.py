"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pledge import Pledge, PledgeTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookPledgeUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a pledge is updated.

    **Discord & Slack support:** Basic
    """

    data: PledgeTypedDict
    type: Literal["pledge.updated"]


class WebhookPledgeUpdatedPayload(BaseModel):
    r"""Sent when a pledge is updated.

    **Discord & Slack support:** Basic
    """

    data: Pledge

    TYPE: Annotated[
        Annotated[
            Literal["pledge.updated"], AfterValidator(validate_const("pledge.updated"))
        ],
        pydantic.Field(alias="type"),
    ] = "pledge.updated"
