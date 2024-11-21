"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .discountduration import DiscountDuration
from .discounttype import DiscountType
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypedDict


DiscountPercentageRepeatDurationCreateMetadataTypedDict = Union[str, int, bool]


DiscountPercentageRepeatDurationCreateMetadata = Union[str, int, bool]


class DiscountPercentageRepeatDurationCreateTypedDict(TypedDict):
    r"""Schema to create a percentage discount that is applied on every invoice
    for a certain number of months.
    """

    duration: DiscountDuration
    duration_in_months: int
    r"""Number of months the discount should be applied.

    For this to work on yearly pricing, you should multiply this by 12.
    For example, to apply the discount for 2 years, set this to 24.
    """
    type: DiscountType
    basis_points: int
    r"""Discount percentage in basis points.

    A basis point is 1/100th of a percent.
    For example, to create a 25.5% discount, set this to 2550.
    """
    name: str
    r"""Name of the discount. Will be displayed to the customer when the discount is applied."""
    metadata: NotRequired[
        Dict[str, DiscountPercentageRepeatDurationCreateMetadataTypedDict]
    ]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:
    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    code: NotRequired[Nullable[str]]
    r"""Code customers can use to apply the discount during checkout. Must be between 3 and 256 characters long and contain only alphanumeric characters.If not provided, the discount can only be applied via the API."""
    starts_at: NotRequired[Nullable[datetime]]
    r"""Optional timestamp after which the discount is redeemable."""
    ends_at: NotRequired[Nullable[datetime]]
    r"""Optional timestamp after which the discount is no longer redeemable."""
    max_redemptions: NotRequired[Nullable[int]]
    r"""Optional maximum number of times the discount can be redeemed."""
    products: NotRequired[Nullable[List[str]]]
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the discount. **Required unless you use an organization token.**"""


class DiscountPercentageRepeatDurationCreate(BaseModel):
    r"""Schema to create a percentage discount that is applied on every invoice
    for a certain number of months.
    """

    duration: DiscountDuration

    duration_in_months: int
    r"""Number of months the discount should be applied.

    For this to work on yearly pricing, you should multiply this by 12.
    For example, to apply the discount for 2 years, set this to 24.
    """

    type: DiscountType

    basis_points: int
    r"""Discount percentage in basis points.

    A basis point is 1/100th of a percent.
    For example, to create a 25.5% discount, set this to 2550.
    """

    name: str
    r"""Name of the discount. Will be displayed to the customer when the discount is applied."""

    metadata: Optional[Dict[str, DiscountPercentageRepeatDurationCreateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:
    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    code: OptionalNullable[str] = UNSET
    r"""Code customers can use to apply the discount during checkout. Must be between 3 and 256 characters long and contain only alphanumeric characters.If not provided, the discount can only be applied via the API."""

    starts_at: OptionalNullable[datetime] = UNSET
    r"""Optional timestamp after which the discount is redeemable."""

    ends_at: OptionalNullable[datetime] = UNSET
    r"""Optional timestamp after which the discount is no longer redeemable."""

    max_redemptions: OptionalNullable[int] = UNSET
    r"""Optional maximum number of times the discount can be redeemed."""

    products: OptionalNullable[List[str]] = UNSET

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the discount. **Required unless you use an organization token.**"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "code",
            "starts_at",
            "ends_at",
            "max_redemptions",
            "products",
            "organization_id",
        ]
        nullable_fields = [
            "code",
            "starts_at",
            "ends_at",
            "max_redemptions",
            "products",
            "organization_id",
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
