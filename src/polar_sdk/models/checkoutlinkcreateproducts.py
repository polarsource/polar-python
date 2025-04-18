"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CheckoutLinkCreateProductsMetadataTypedDict = TypeAliasType(
    "CheckoutLinkCreateProductsMetadataTypedDict", Union[str, int, float, bool]
)


CheckoutLinkCreateProductsMetadata = TypeAliasType(
    "CheckoutLinkCreateProductsMetadata", Union[str, int, float, bool]
)


class CheckoutLinkCreateProductsTypedDict(TypedDict):
    r"""Schema to create a new checkout link."""

    products: List[str]
    r"""List of products that will be available to select at checkout."""
    metadata: NotRequired[Dict[str, CheckoutLinkCreateProductsMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    payment_processor: Literal["stripe"]
    r"""Payment processor to use. Currently only Stripe is supported."""
    label: NotRequired[Nullable[str]]
    r"""Optional label to distinguish links internally"""
    allow_discount_codes: NotRequired[bool]
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""
    require_billing_address: NotRequired[bool]
    r"""Whether to require the customer to fill their full billing address, instead of just the country. Customers in the US will always be required to fill their full address, regardless of this setting."""
    discount_id: NotRequired[Nullable[str]]
    r"""ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored."""
    success_url: NotRequired[Nullable[str]]
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""


class CheckoutLinkCreateProducts(BaseModel):
    r"""Schema to create a new checkout link."""

    products: List[str]
    r"""List of products that will be available to select at checkout."""

    metadata: Optional[Dict[str, CheckoutLinkCreateProductsMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    PAYMENT_PROCESSOR: Annotated[
        Annotated[Literal["stripe"], AfterValidator(validate_const("stripe"))],
        pydantic.Field(alias="payment_processor"),
    ] = "stripe"
    r"""Payment processor to use. Currently only Stripe is supported."""

    label: OptionalNullable[str] = UNSET
    r"""Optional label to distinguish links internally"""

    allow_discount_codes: Optional[bool] = True
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""

    require_billing_address: Optional[bool] = False
    r"""Whether to require the customer to fill their full billing address, instead of just the country. Customers in the US will always be required to fill their full address, regardless of this setting."""

    discount_id: OptionalNullable[str] = UNSET
    r"""ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored."""

    success_url: OptionalNullable[str] = UNSET
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "label",
            "allow_discount_codes",
            "require_billing_address",
            "discount_id",
            "success_url",
        ]
        nullable_fields = ["label", "discount_id", "success_url"]
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
