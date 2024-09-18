"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productpricerecurringcustom import (
    ProductPriceRecurringCustom,
    ProductPriceRecurringCustomTypedDict,
)
from .productpricerecurringfixed import (
    ProductPriceRecurringFixed,
    ProductPriceRecurringFixedTypedDict,
)
from polar_sdk.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated


ProductPriceRecurringOutputTypedDict = Union[
    ProductPriceRecurringFixedTypedDict, ProductPriceRecurringCustomTypedDict
]


ProductPriceRecurringOutput = Annotated[
    Union[
        Annotated[ProductPriceRecurringCustom, Tag("custom")],
        Annotated[ProductPriceRecurringFixed, Tag("fixed")],
    ],
    Discriminator(lambda m: get_discriminator(m, "amount_type", "amount_type")),
]
