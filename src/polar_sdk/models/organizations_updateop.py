"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationupdate import OrganizationUpdate, OrganizationUpdateTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class OrganizationsUpdateRequestTypedDict(TypedDict):
    id: str
    organization_update: OrganizationUpdateTypedDict


class OrganizationsUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    organization_update: Annotated[
        OrganizationUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
