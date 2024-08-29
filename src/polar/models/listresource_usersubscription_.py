"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .usersubscription import UserSubscription, UserSubscriptionTypedDict
from polar.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class ListResourceUserSubscriptionTypedDict(TypedDict):
    pagination: PaginationTypedDict
    items: NotRequired[List[UserSubscriptionTypedDict]]
    

class ListResourceUserSubscription(BaseModel):
    pagination: Pagination
    items: Optional[List[UserSubscription]] = None
    