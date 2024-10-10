"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PaymentProcessor(str, Enum):
    r"""Payment processor to use. Currently only Stripe is supported."""

    STRIPE = "stripe"


class PolarCheckoutSchemasCheckoutCreateTypedDict(TypedDict):
    r"""Create a new checkout session."""

    product_price_id: str
    r"""ID of the product price to checkout."""
    metadata: NotRequired[Dict[str, str]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be a string with a maximum length of **500 characters**.
    You can store up to **50 key-value pairs**.
    """
    payment_processor: PaymentProcessor
    r"""Payment processor to use. Currently only Stripe is supported."""
    amount: NotRequired[Nullable[int]]
    customer_name: NotRequired[Nullable[str]]
    customer_email: NotRequired[Nullable[str]]
    customer_ip_address: NotRequired[Nullable[str]]
    customer_billing_address: NotRequired[Nullable[AddressTypedDict]]
    customer_tax_id: NotRequired[Nullable[str]]
    success_url: NotRequired[Nullable[str]]
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""


class PolarCheckoutSchemasCheckoutCreate(BaseModel):
    r"""Create a new checkout session."""

    product_price_id: str
    r"""ID of the product price to checkout."""

    metadata: Optional[Dict[str, str]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be a string with a maximum length of **500 characters**.
    You can store up to **50 key-value pairs**.
    """

    PAYMENT_PROCESSOR: Annotated[
        Annotated[
            PaymentProcessor, AfterValidator(validate_const(PaymentProcessor.STRIPE))
        ],
        pydantic.Field(alias="payment_processor"),
    ] = PaymentProcessor.STRIPE
    r"""Payment processor to use. Currently only Stripe is supported."""

    amount: OptionalNullable[int] = UNSET

    customer_name: OptionalNullable[str] = UNSET

    customer_email: OptionalNullable[str] = UNSET

    customer_ip_address: OptionalNullable[str] = UNSET

    customer_billing_address: OptionalNullable[Address] = UNSET

    customer_tax_id: OptionalNullable[str] = UNSET

    success_url: OptionalNullable[str] = UNSET
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "amount",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
            "success_url",
        ]
        nullable_fields = [
            "amount",
            "customer_name",
            "customer_email",
            "customer_ip_address",
            "customer_billing_address",
            "customer_tax_id",
            "success_url",
        ]
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
