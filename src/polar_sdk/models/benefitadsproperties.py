"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BenefitAdsPropertiesTypedDict(TypedDict):
    r"""Properties for a benefit of type `ads`."""

    image_height: NotRequired[int]
    r"""The height of the displayed ad."""
    image_width: NotRequired[int]
    r"""The width of the displayed ad."""


class BenefitAdsProperties(BaseModel):
    r"""Properties for a benefit of type `ads`."""

    image_height: Optional[int] = 400
    r"""The height of the displayed ad."""

    image_width: Optional[int] = 400
    r"""The width of the displayed ad."""
