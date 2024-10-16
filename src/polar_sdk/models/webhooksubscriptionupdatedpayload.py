"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscription_input import SubscriptionInput, SubscriptionInputTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookSubscriptionUpdatedPayloadType(str, Enum):
    SUBSCRIPTION_UPDATED = "subscription.updated"


class WebhookSubscriptionUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a subscription is updated. This event fires for all changes to the subscription, including renewals.

    If you want more specific events, you can listen to `subscription.active`, `subscription.canceled`, and `subscription.revoked`.

    To listen specifically for renewals, you can listen to `order.created` events and check the `billing_reason` field.

    **Discord & Slack support:** On cancellation and revocation. Renewals are skipped.
    """

    data: SubscriptionInputTypedDict
    type: WebhookSubscriptionUpdatedPayloadType


class WebhookSubscriptionUpdatedPayload(BaseModel):
    r"""Sent when a subscription is updated. This event fires for all changes to the subscription, including renewals.

    If you want more specific events, you can listen to `subscription.active`, `subscription.canceled`, and `subscription.revoked`.

    To listen specifically for renewals, you can listen to `order.created` events and check the `billing_reason` field.

    **Discord & Slack support:** On cancellation and revocation. Renewals are skipped.
    """

    data: SubscriptionInput

    TYPE: Annotated[
        Annotated[
            WebhookSubscriptionUpdatedPayloadType,
            AfterValidator(
                validate_const(
                    WebhookSubscriptionUpdatedPayloadType.SUBSCRIPTION_UPDATED
                )
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookSubscriptionUpdatedPayloadType.SUBSCRIPTION_UPDATED
