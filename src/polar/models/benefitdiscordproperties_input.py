"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar.types import BaseModel
from typing import TypedDict


class BenefitDiscordPropertiesInputTypedDict(TypedDict):
    r"""Properties for a benefit of type `discord`."""
    
    guild_id: str
    r"""The ID of the Discord server."""
    role_id: str
    r"""The ID of the Discord role to grant."""
    

class BenefitDiscordPropertiesInput(BaseModel):
    r"""Properties for a benefit of type `discord`."""
    
    guild_id: str
    r"""The ID of the Discord server."""
    role_id: str
    r"""The ID of the Discord role to grant."""
    