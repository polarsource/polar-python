"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customerorderproduct import CustomerOrderProduct, CustomerOrderProductTypedDict
from .customerordersubscription import (
    CustomerOrderSubscription,
    CustomerOrderSubscriptionTypedDict,
)
from .legacyrecurringproductprice import (
    LegacyRecurringProductPrice,
    LegacyRecurringProductPriceTypedDict,
)
from .orderitemschema import OrderItemSchema, OrderItemSchemaTypedDict
from .productprice import ProductPrice, ProductPriceTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


CustomerOrderProductPriceTypedDict = TypeAliasType(
    "CustomerOrderProductPriceTypedDict",
    Union[LegacyRecurringProductPriceTypedDict, ProductPriceTypedDict],
)


CustomerOrderProductPrice = TypeAliasType(
    "CustomerOrderProductPrice", Union[LegacyRecurringProductPrice, ProductPrice]
)


class CustomerOrderTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    subtotal_amount: int
    r"""Amount in cents, before discounts and taxes."""
    discount_amount: int
    r"""Discount amount in cents."""
    net_amount: int
    r"""Amount in cents, after discounts but before taxes."""
    amount: int
    r"""Amount in cents, after discounts but before taxes."""
    tax_amount: int
    r"""Sales tax amount in cents."""
    total_amount: int
    r"""Amount in cents, after discounts and taxes."""
    refunded_amount: int
    r"""Amount refunded in cents."""
    refunded_tax_amount: int
    r"""Sales tax refunded in cents."""
    currency: str
    customer_id: str
    product_id: str
    product_price_id: str
    subscription_id: Nullable[str]
    user_id: str
    product: CustomerOrderProductTypedDict
    product_price: CustomerOrderProductPriceTypedDict
    subscription: Nullable[CustomerOrderSubscriptionTypedDict]
    items: List[OrderItemSchemaTypedDict]
    r"""Line items composing the order."""


class CustomerOrder(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str

    subtotal_amount: int
    r"""Amount in cents, before discounts and taxes."""

    discount_amount: int
    r"""Discount amount in cents."""

    net_amount: int
    r"""Amount in cents, after discounts but before taxes."""

    amount: Annotated[
        int,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Amount in cents, after discounts but before taxes."""

    tax_amount: int
    r"""Sales tax amount in cents."""

    total_amount: int
    r"""Amount in cents, after discounts and taxes."""

    refunded_amount: int
    r"""Amount refunded in cents."""

    refunded_tax_amount: int
    r"""Sales tax refunded in cents."""

    currency: str

    customer_id: str

    product_id: str

    product_price_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    subscription_id: Nullable[str]

    user_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    product: CustomerOrderProduct

    product_price: Annotated[
        CustomerOrderProductPrice,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    subscription: Nullable[CustomerOrderSubscription]

    items: List[OrderItemSchema]
    r"""Line items composing the order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "subscription_id", "subscription"]
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
