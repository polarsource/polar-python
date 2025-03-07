"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription import Subscription, SubscriptionTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionActivePayloadTypedDict(TypedDict):
    r"""Sent when a subscription becomes active,
    whether because it's a new paid subscription or because payment was recovered.

    **Discord & Slack support:** Full
    """

    data: SubscriptionTypedDict
    type: Literal["subscription.active"]


class WebhookSubscriptionActivePayload(BaseModel):
    r"""Sent when a subscription becomes active,
    whether because it's a new paid subscription or because payment was recovered.

    **Discord & Slack support:** Full
    """

    data: Subscription

    TYPE: Annotated[
        Annotated[
            Literal["subscription.active"],
            AfterValidator(validate_const("subscription.active")),
        ],
        pydantic.Field(alias="type"),
    ] = "subscription.active"
