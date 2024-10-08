"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .licensekeyupdate import LicenseKeyUpdate, LicenseKeyUpdateTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class LicenseKeysUpdateRequestTypedDict(TypedDict):
    id: str
    license_key_update: LicenseKeyUpdateTypedDict


class LicenseKeysUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    license_key_update: Annotated[
        LicenseKeyUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
