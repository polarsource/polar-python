"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


CheckoutLinkUpdateMetadataTypedDict = TypeAliasType(
    "CheckoutLinkUpdateMetadataTypedDict", Union[str, int, float, bool]
)


CheckoutLinkUpdateMetadata = TypeAliasType(
    "CheckoutLinkUpdateMetadata", Union[str, int, float, bool]
)


class CheckoutLinkUpdateTypedDict(TypedDict):
    r"""Schema to update an existing checkout link."""

    metadata: NotRequired[Dict[str, CheckoutLinkUpdateMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    products: NotRequired[Nullable[List[str]]]
    r"""List of products that will be available to select at checkout."""
    label: NotRequired[Nullable[str]]
    allow_discount_codes: NotRequired[Nullable[bool]]
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""
    discount_id: NotRequired[Nullable[str]]
    r"""ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored."""
    success_url: NotRequired[Nullable[str]]
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""


class CheckoutLinkUpdate(BaseModel):
    r"""Schema to update an existing checkout link."""

    metadata: Optional[Dict[str, CheckoutLinkUpdateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A floating-point number
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    products: OptionalNullable[List[str]] = UNSET
    r"""List of products that will be available to select at checkout."""

    label: OptionalNullable[str] = UNSET

    allow_discount_codes: OptionalNullable[bool] = UNSET
    r"""Whether to allow the customer to apply discount codes. If you apply a discount through `discount_id`, it'll still be applied, but the customer won't be able to change it."""

    discount_id: OptionalNullable[str] = UNSET
    r"""ID of the discount to apply to the checkout. If the discount is not applicable anymore when opening the checkout link, it'll be ignored."""

    success_url: OptionalNullable[str] = UNSET
    r"""URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "products",
            "label",
            "allow_discount_codes",
            "discount_id",
            "success_url",
        ]
        nullable_fields = [
            "products",
            "label",
            "allow_discount_codes",
            "discount_id",
            "success_url",
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
