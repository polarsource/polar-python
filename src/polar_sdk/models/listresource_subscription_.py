"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .subscription import Subscription, SubscriptionTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListResourceSubscriptionTypedDict(TypedDict):
    items: List[SubscriptionTypedDict]
    pagination: PaginationTypedDict


class ListResourceSubscription(BaseModel):
    items: List[Subscription]

    pagination: Pagination
