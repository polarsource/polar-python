"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .advertisementcampaign import AdvertisementCampaign, AdvertisementCampaignTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AdvertisementCampaignListResourceTypedDict(TypedDict):
    items: List[AdvertisementCampaignTypedDict]
    pagination: PaginationTypedDict
    dimensions: List[int]
    r"""The dimensions (width, height) in pixels of the advertisement images."""


class AdvertisementCampaignListResource(BaseModel):
    items: List[AdvertisementCampaign]

    pagination: Pagination

    dimensions: List[int]
    r"""The dimensions (width, height) in pixels of the advertisement images."""
