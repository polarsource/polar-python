"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productonetimecreate import ProductOneTimeCreate, ProductOneTimeCreateTypedDict
from .productrecurringcreate import (
    ProductRecurringCreate,
    ProductRecurringCreateTypedDict,
)
from typing import Union


ProductsCreateProductCreateTypedDict = Union[
    ProductRecurringCreateTypedDict, ProductOneTimeCreateTypedDict
]


ProductsCreateProductCreate = Union[ProductRecurringCreate, ProductOneTimeCreate]
