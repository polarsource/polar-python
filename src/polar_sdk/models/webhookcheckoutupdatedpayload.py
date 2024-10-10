"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .polar_checkout_schemas_checkout import (
    PolarCheckoutSchemasCheckoutInput,
    PolarCheckoutSchemasCheckoutInputTypedDict,
)
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookCheckoutUpdatedPayloadType(str, Enum):
    CHECKOUT_UPDATED = "checkout.updated"


class WebhookCheckoutUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a checkout is updated.

    **Discord & Slack support:** Basic
    """

    data: PolarCheckoutSchemasCheckoutInputTypedDict
    r"""Checkout session data retrieved using an access token."""
    type: WebhookCheckoutUpdatedPayloadType


class WebhookCheckoutUpdatedPayload(BaseModel):
    r"""Sent when a checkout is updated.

    **Discord & Slack support:** Basic
    """

    data: PolarCheckoutSchemasCheckoutInput
    r"""Checkout session data retrieved using an access token."""

    TYPE: Annotated[
        Annotated[
            WebhookCheckoutUpdatedPayloadType,
            AfterValidator(
                validate_const(WebhookCheckoutUpdatedPayloadType.CHECKOUT_UPDATED)
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookCheckoutUpdatedPayloadType.CHECKOUT_UPDATED
