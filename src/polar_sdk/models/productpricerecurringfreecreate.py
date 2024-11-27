"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriptionrecurringinterval import SubscriptionRecurringInterval
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class ProductPriceRecurringFreeCreateType(str, Enum):
    RECURRING = "recurring"


class ProductPriceRecurringFreeCreateAmountType(str, Enum):
    FREE = "free"


class ProductPriceRecurringFreeCreateTypedDict(TypedDict):
    r"""Schema to create a free recurring product price, i.e. a subscription."""

    recurring_interval: SubscriptionRecurringInterval
    type: ProductPriceRecurringFreeCreateType
    amount_type: ProductPriceRecurringFreeCreateAmountType


class ProductPriceRecurringFreeCreate(BaseModel):
    r"""Schema to create a free recurring product price, i.e. a subscription."""

    recurring_interval: SubscriptionRecurringInterval

    TYPE: Annotated[
        Annotated[
            ProductPriceRecurringFreeCreateType,
            AfterValidator(
                validate_const(ProductPriceRecurringFreeCreateType.RECURRING)
            ),
        ],
        pydantic.Field(alias="type"),
    ] = ProductPriceRecurringFreeCreateType.RECURRING

    AMOUNT_TYPE: Annotated[
        Annotated[
            ProductPriceRecurringFreeCreateAmountType,
            AfterValidator(
                validate_const(ProductPriceRecurringFreeCreateAmountType.FREE)
            ),
        ],
        pydantic.Field(alias="amount_type"),
    ] = ProductPriceRecurringFreeCreateAmountType.FREE