"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class LicenseKeyActivateConditionsTypedDict(TypedDict):
    pass


class LicenseKeyActivateConditions(BaseModel):
    pass


class LicenseKeyActivateMetaTypedDict(TypedDict):
    pass


class LicenseKeyActivateMeta(BaseModel):
    pass


class LicenseKeyActivateTypedDict(TypedDict):
    key: str
    organization_id: str
    label: str
    conditions: NotRequired[LicenseKeyActivateConditionsTypedDict]
    meta: NotRequired[LicenseKeyActivateMetaTypedDict]


class LicenseKeyActivate(BaseModel):
    key: str

    organization_id: str

    label: str

    conditions: Optional[LicenseKeyActivateConditions] = None

    meta: Optional[LicenseKeyActivateMeta] = None
