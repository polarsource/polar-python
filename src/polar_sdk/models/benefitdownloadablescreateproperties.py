"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class BenefitDownloadablesCreatePropertiesTypedDict(TypedDict):
    files: List[str]
    archived: NotRequired[Dict[str, bool]]


class BenefitDownloadablesCreateProperties(BaseModel):
    files: List[str]

    archived: Optional[Dict[str, bool]] = None
