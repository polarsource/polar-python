"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productpriceonetime import ProductPriceOneTime, ProductPriceOneTimeTypedDict
from .productpricerecurring_output import (
    ProductPriceRecurringOutput,
    ProductPriceRecurringOutputTypedDict,
)
from typing import Union


ProductPriceOutputTypedDict = Union[
    ProductPriceRecurringOutputTypedDict, ProductPriceOneTimeTypedDict
]


ProductPriceOutput = Union[ProductPriceRecurringOutput, ProductPriceOneTime]
