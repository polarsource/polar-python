"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productpricemeter import ProductPriceMeter, ProductPriceMeterTypedDict
from .productpricetype import ProductPriceType
from .subscriptionrecurringinterval import SubscriptionRecurringInterval
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ProductPriceMeteredUnitTypedDict(TypedDict):
    r"""A metered, usage-based, price for a product, with a fixed unit price."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the price."""
    is_archived: bool
    r"""Whether the price is archived and no longer available."""
    product_id: str
    r"""The ID of the product owning the price."""
    type: ProductPriceType
    recurring_interval: Nullable[SubscriptionRecurringInterval]
    price_currency: str
    r"""The currency."""
    unit_amount: int
    r"""The price per unit in cents."""
    cap_amount: Nullable[int]
    r"""The maximum amount in cents that can be charged, regardless of the number of units consumed."""
    meter_id: str
    r"""The ID of the meter associated to the price."""
    meter: ProductPriceMeterTypedDict
    r"""A meter associated to a metered price."""
    amount_type: Literal["metered_unit"]


class ProductPriceMeteredUnit(BaseModel):
    r"""A metered, usage-based, price for a product, with a fixed unit price."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the price."""

    is_archived: bool
    r"""Whether the price is archived and no longer available."""

    product_id: str
    r"""The ID of the product owning the price."""

    type: ProductPriceType

    recurring_interval: Annotated[
        Nullable[SubscriptionRecurringInterval],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    price_currency: str
    r"""The currency."""

    unit_amount: int
    r"""The price per unit in cents."""

    cap_amount: Nullable[int]
    r"""The maximum amount in cents that can be charged, regardless of the number of units consumed."""

    meter_id: str
    r"""The ID of the meter associated to the price."""

    meter: ProductPriceMeter
    r"""A meter associated to a metered price."""

    AMOUNT_TYPE: Annotated[
        Annotated[
            Literal["metered_unit"], AfterValidator(validate_const("metered_unit"))
        ],
        pydantic.Field(alias="amount_type"),
    ] = "metered_unit"

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "recurring_interval", "cap_amount"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
