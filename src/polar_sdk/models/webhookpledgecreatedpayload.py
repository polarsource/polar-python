"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pledge_input import PledgeInput, PledgeInputTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
import pydantic
from typing import Final, TypedDict
from typing_extensions import Annotated


class WebhookPledgeCreatedPayloadType(str, Enum):
    PLEDGE_CREATED = "pledge.created"


class WebhookPledgeCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new pledge is created. Note that this does mean that the pledge has been paid yet.

    **Discord & Slack support:** Full
    """

    data: PledgeInputTypedDict
    type: WebhookPledgeCreatedPayloadType


class WebhookPledgeCreatedPayload(BaseModel):
    r"""Sent when a new pledge is created. Note that this does mean that the pledge has been paid yet.

    **Discord & Slack support:** Full
    """

    data: PledgeInput

    # fmt: off
    TYPE: Annotated[Final[WebhookPledgeCreatedPayloadType], pydantic.Field(alias="type")] = WebhookPledgeCreatedPayloadType.PLEDGE_CREATED # type: ignore
    # fmt: on
