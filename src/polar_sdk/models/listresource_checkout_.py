"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .checkout import Checkout, CheckoutTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListResourceCheckoutTypedDict(TypedDict):
    items: List[CheckoutTypedDict]
    pagination: PaginationTypedDict


class ListResourceCheckout(BaseModel):
    items: List[Checkout]

    pagination: Pagination
