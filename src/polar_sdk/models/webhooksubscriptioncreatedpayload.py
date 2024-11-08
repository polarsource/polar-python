"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription import SubscriptionInput, SubscriptionInputTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionCreatedPayloadType(str, Enum):
    SUBSCRIPTION_CREATED = "subscription.created"


class WebhookSubscriptionCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new subscription is created.

    **Discord & Slack support:** Full
    """

    data: SubscriptionInputTypedDict
    type: WebhookSubscriptionCreatedPayloadType


class WebhookSubscriptionCreatedPayload(BaseModel):
    r"""Sent when a new subscription is created.

    **Discord & Slack support:** Full
    """

    data: SubscriptionInput

    TYPE: Annotated[
        Annotated[
            WebhookSubscriptionCreatedPayloadType,
            AfterValidator(
                validate_const(
                    WebhookSubscriptionCreatedPayloadType.SUBSCRIPTION_CREATED
                )
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookSubscriptionCreatedPayloadType.SUBSCRIPTION_CREATED
