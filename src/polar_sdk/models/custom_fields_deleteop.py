"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class CustomFieldsDeleteRequestTypedDict(TypedDict):
    id: str
    r"""The custom field ID."""


class CustomFieldsDeleteRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The custom field ID."""