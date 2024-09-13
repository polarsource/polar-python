"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import Dict, List, TypedDict


class BenefitDownloadablesPropertiesTypedDict(TypedDict):
    archived: Dict[str, bool]
    files: List[str]


class BenefitDownloadablesProperties(BaseModel):
    archived: Dict[str, bool]

    files: List[str]
