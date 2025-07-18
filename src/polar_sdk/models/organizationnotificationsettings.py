"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class OrganizationNotificationSettingsTypedDict(TypedDict):
    new_order: bool
    new_subscription: bool


class OrganizationNotificationSettings(BaseModel):
    new_order: bool

    new_subscription: bool
