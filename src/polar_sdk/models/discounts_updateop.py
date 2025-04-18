"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .discountupdate import DiscountUpdate, DiscountUpdateTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class DiscountsUpdateRequestTypedDict(TypedDict):
    id: str
    r"""The discount ID."""
    discount_update: DiscountUpdateTypedDict


class DiscountsUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The discount ID."""

    discount_update: Annotated[
        DiscountUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
