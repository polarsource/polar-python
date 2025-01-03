"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productpriceonetime import ProductPriceOneTime, ProductPriceOneTimeTypedDict
from .productpricerecurring import ProductPriceRecurring, ProductPriceRecurringTypedDict
from typing import Union
from typing_extensions import TypeAliasType


ProductPriceTypedDict = TypeAliasType(
    "ProductPriceTypedDict",
    Union[ProductPriceRecurringTypedDict, ProductPriceOneTimeTypedDict],
)


ProductPrice = TypeAliasType(
    "ProductPrice", Union[ProductPriceRecurring, ProductPriceOneTime]
)
