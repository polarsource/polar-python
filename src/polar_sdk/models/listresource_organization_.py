"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organization import Organization, OrganizationTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListResourceOrganizationTypedDict(TypedDict):
    items: List[OrganizationTypedDict]
    pagination: PaginationTypedDict


class ListResourceOrganization(BaseModel):
    items: List[Organization]

    pagination: Pagination
