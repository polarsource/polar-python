"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .checkoutpricecreate import CheckoutPriceCreate, CheckoutPriceCreateTypedDict
from .checkoutproductcreate import CheckoutProductCreate, CheckoutProductCreateTypedDict
from .checkoutproductscreate import (
    CheckoutProductsCreate,
    CheckoutProductsCreateTypedDict,
)
from typing import Union
from typing_extensions import TypeAliasType


CheckoutCreateTypedDict = TypeAliasType(
    "CheckoutCreateTypedDict",
    Union[
        CheckoutProductsCreateTypedDict,
        CheckoutProductCreateTypedDict,
        CheckoutPriceCreateTypedDict,
    ],
)


CheckoutCreate = TypeAliasType(
    "CheckoutCreate",
    Union[CheckoutProductsCreate, CheckoutProductCreate, CheckoutPriceCreate],
)
