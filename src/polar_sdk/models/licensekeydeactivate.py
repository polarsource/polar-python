"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class LicenseKeyDeactivateTypedDict(TypedDict):
    key: str
    organization_id: str
    activation_id: str


class LicenseKeyDeactivate(BaseModel):
    key: str

    organization_id: str

    activation_id: str
