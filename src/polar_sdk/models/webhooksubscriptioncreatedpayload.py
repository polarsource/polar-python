"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription import Subscription, SubscriptionTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new subscription is created.

    When this event occurs, the subscription `status` might not be `active` yet, as we can still have to wait for the first payment to be processed.

    **Discord & Slack support:** Full
    """

    data: SubscriptionTypedDict
    type: Literal["subscription.created"]


class WebhookSubscriptionCreatedPayload(BaseModel):
    r"""Sent when a new subscription is created.

    When this event occurs, the subscription `status` might not be `active` yet, as we can still have to wait for the first payment to be processed.

    **Discord & Slack support:** Full
    """

    data: Subscription

    TYPE: Annotated[
        Annotated[
            Literal["subscription.created"],
            AfterValidator(validate_const("subscription.created")),
        ],
        pydantic.Field(alias="type"),
    ] = "subscription.created"
