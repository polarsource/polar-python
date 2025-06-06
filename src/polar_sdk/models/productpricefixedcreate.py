"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ProductPriceFixedCreateTypedDict(TypedDict):
    r"""Schema to create a fixed price."""

    price_amount: int
    r"""The price in cents."""
    amount_type: Literal["fixed"]
    price_currency: NotRequired[str]
    r"""The currency. Currently, only `usd` is supported."""


class ProductPriceFixedCreate(BaseModel):
    r"""Schema to create a fixed price."""

    price_amount: int
    r"""The price in cents."""

    AMOUNT_TYPE: Annotated[
        Annotated[Literal["fixed"], AfterValidator(validate_const("fixed"))],
        pydantic.Field(alias="amount_type"),
    ] = "fixed"

    price_currency: Optional[str] = "usd"
    r"""The currency. Currently, only `usd` is supported."""
