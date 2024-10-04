"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class BenefitDiscordSubscriberPropertiesTypedDict(TypedDict):
    r"""Properties available to subscribers for a benefit of type `discord`."""

    guild_id: str
    r"""The ID of the Discord server."""


class BenefitDiscordSubscriberProperties(BaseModel):
    r"""Properties available to subscribers for a benefit of type `discord`."""

    guild_id: str
    r"""The ID of the Discord server."""
