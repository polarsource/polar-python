"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription import Subscription, SubscriptionTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionCanceledPayloadTypedDict(TypedDict):
    r"""Sent when a subscription is canceled by the user.
    They might still have access until the end of the current period.

    **Discord & Slack support:** Full
    """

    data: SubscriptionTypedDict
    type: Literal["subscription.canceled"]


class WebhookSubscriptionCanceledPayload(BaseModel):
    r"""Sent when a subscription is canceled by the user.
    They might still have access until the end of the current period.

    **Discord & Slack support:** Full
    """

    data: Subscription

    TYPE: Annotated[
        Annotated[
            Literal["subscription.canceled"],
            AfterValidator(validate_const("subscription.canceled")),
        ],
        pydantic.Field(alias="type"),
    ] = "subscription.canceled"
