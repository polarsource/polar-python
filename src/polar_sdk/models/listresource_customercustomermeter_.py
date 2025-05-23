"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercustomermeter import CustomerCustomerMeter, CustomerCustomerMeterTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListResourceCustomerCustomerMeterTypedDict(TypedDict):
    items: List[CustomerCustomerMeterTypedDict]
    pagination: PaginationTypedDict


class ListResourceCustomerCustomerMeter(BaseModel):
    items: List[CustomerCustomerMeter]

    pagination: Pagination
