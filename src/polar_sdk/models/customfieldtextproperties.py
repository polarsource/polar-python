"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomFieldTextPropertiesTypedDict(TypedDict):
    form_label: NotRequired[str]
    form_help_text: NotRequired[str]
    form_placeholder: NotRequired[str]
    textarea: NotRequired[bool]
    min_length: NotRequired[int]
    max_length: NotRequired[int]


class CustomFieldTextProperties(BaseModel):
    form_label: Optional[str] = None

    form_help_text: Optional[str] = None

    form_placeholder: Optional[str] = None

    textarea: Optional[bool] = None

    min_length: Optional[int] = None

    max_length: Optional[int] = None
