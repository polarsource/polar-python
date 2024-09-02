"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import TypedDict


class UserAdvertisementCampaignEnableTypedDict(TypedDict):
    benefit_id: str
    r"""The benefit ID."""
    

class UserAdvertisementCampaignEnable(BaseModel):
    benefit_id: str
    r"""The benefit ID."""
    