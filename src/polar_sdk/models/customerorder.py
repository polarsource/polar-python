"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .customerorderproduct import CustomerOrderProduct, CustomerOrderProductTypedDict
from .customerordersubscription import (
    CustomerOrderSubscription,
    CustomerOrderSubscriptionTypedDict,
)
from .orderbillingreason import OrderBillingReason
from .orderitemschema import OrderItemSchema, OrderItemSchemaTypedDict
from .orderstatus import OrderStatus
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List
from typing_extensions import Annotated, TypedDict


class CustomerOrderTypedDict(TypedDict):
    id: str
    r"""The ID of the object."""
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    status: OrderStatus
    paid: bool
    r"""Whether the order has been paid for."""
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
    billing_reason: OrderBillingReason
    billing_name: Nullable[str]
    r"""The name of the customer that should appear on the invoice."""
    billing_address: Nullable[AddressTypedDict]
    is_invoice_generated: bool
    r"""Whether an invoice has been generated for this order."""
    customer_id: str
    product_id: str
    discount_id: Nullable[str]
    subscription_id: Nullable[str]
    checkout_id: Nullable[str]
    user_id: str
    product: CustomerOrderProductTypedDict
    subscription: Nullable[CustomerOrderSubscriptionTypedDict]
    items: List[OrderItemSchemaTypedDict]
    r"""Line items composing the order."""


class CustomerOrder(BaseModel):
    id: str
    r"""The ID of the object."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    status: OrderStatus

    paid: bool
    r"""Whether the order has been paid for."""

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

    billing_reason: OrderBillingReason

    billing_name: Nullable[str]
    r"""The name of the customer that should appear on the invoice."""

    billing_address: Nullable[Address]

    is_invoice_generated: bool
    r"""Whether an invoice has been generated for this order."""

    customer_id: str

    product_id: str

    discount_id: Nullable[str]

    subscription_id: Nullable[str]

    checkout_id: Nullable[str]

    user_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    product: CustomerOrderProduct

    subscription: Nullable[CustomerOrderSubscription]

    items: List[OrderItemSchema]
    r"""Line items composing the order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "billing_name",
            "billing_address",
            "discount_id",
            "subscription_id",
            "checkout_id",
            "subscription",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
