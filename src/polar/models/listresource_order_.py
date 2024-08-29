"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .order_output import OrderOutput, OrderOutputTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar.types import BaseModel
from typing import List, TypedDict


class ListResourceOrderTypedDict(TypedDict):
    items: List[OrderOutputTypedDict]
    pagination: PaginationTypedDict
    

class ListResourceOrder(BaseModel):
    items: List[OrderOutput]
    pagination: Pagination
    
