"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .meterquantity import MeterQuantity, MeterQuantityTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class MeterQuantitiesTypedDict(TypedDict):
    quantities: List[MeterQuantityTypedDict]


class MeterQuantities(BaseModel):
    quantities: List[MeterQuantity]
