"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .donation import Donation, DonationTypedDict
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class WebhookDonationCreatedPayloadType(str, Enum):
    DONATION_CREATED = "donation.created"


class WebhookDonationCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new donation is created.

    **Discord & Slack support:** Full
    """

    data: DonationTypedDict
    type: WebhookDonationCreatedPayloadType


class WebhookDonationCreatedPayload(BaseModel):
    r"""Sent when a new donation is created.

    **Discord & Slack support:** Full
    """

    data: Donation

    TYPE: Annotated[
        Annotated[
            WebhookDonationCreatedPayloadType,
            AfterValidator(
                validate_const(WebhookDonationCreatedPayloadType.DONATION_CREATED)
            ),
        ],
        pydantic.Field(alias="type"),
    ] = WebhookDonationCreatedPayloadType.DONATION_CREATED
