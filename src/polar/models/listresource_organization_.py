"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organization_output import OrganizationOutput, OrganizationOutputTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class ListResourceOrganizationTypedDict(TypedDict):
    pagination: PaginationTypedDict
    items: NotRequired[List[OrganizationOutputTypedDict]]
    

class ListResourceOrganization(BaseModel):
    pagination: Pagination
    items: Optional[List[OrganizationOutput]] = None
    