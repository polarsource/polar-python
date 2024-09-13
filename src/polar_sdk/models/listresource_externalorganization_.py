"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .externalorganization import ExternalOrganization, ExternalOrganizationTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List, TypedDict


class ListResourceExternalOrganizationTypedDict(TypedDict):
    items: List[ExternalOrganizationTypedDict]
    pagination: PaginationTypedDict


class ListResourceExternalOrganization(BaseModel):
    items: List[ExternalOrganization]

    pagination: Pagination
