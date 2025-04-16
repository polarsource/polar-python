"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .discountduration import DiscountDuration
from .discountproduct import DiscountProduct, DiscountProductTypedDict
from .discounttype import DiscountType
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Union
from typing_extensions import TypeAliasType, TypedDict


DiscountPercentageRepeatDurationMetadataTypedDict = TypeAliasType(
    "DiscountPercentageRepeatDurationMetadataTypedDict", Union[str, int, bool]
)


DiscountPercentageRepeatDurationMetadata = TypeAliasType(
    "DiscountPercentageRepeatDurationMetadata", Union[str, int, bool]
)


class DiscountPercentageRepeatDurationTypedDict(TypedDict):
    r"""Schema for a percentage discount that is applied on every invoice
    for a certain number of months.
    """

    duration: DiscountDuration
    duration_in_months: int
    type: DiscountType
    basis_points: int
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    metadata: Dict[str, DiscountPercentageRepeatDurationMetadataTypedDict]
    name: str
    r"""Name of the discount. Will be displayed to the customer when the discount is applied."""
    code: Nullable[str]
    r"""Code customers can use to apply the discount during checkout."""
    starts_at: Nullable[datetime]
    r"""Timestamp after which the discount is redeemable."""
    ends_at: Nullable[datetime]
    r"""Timestamp after which the discount is no longer redeemable."""
    max_redemptions: Nullable[int]
    r"""Maximum number of times the discount can be redeemed."""
    redemptions_count: int
    r"""Number of times the discount has been redeemed."""
    organization_id: str
    r"""The organization ID."""
    products: List[DiscountProductTypedDict]


class DiscountPercentageRepeatDuration(BaseModel):
    r"""Schema for a percentage discount that is applied on every invoice
    for a certain number of months.
    """

    duration: DiscountDuration

    duration_in_months: int

    type: DiscountType

    basis_points: int

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    metadata: Dict[str, DiscountPercentageRepeatDurationMetadata]

    name: str
    r"""Name of the discount. Will be displayed to the customer when the discount is applied."""

    code: Nullable[str]
    r"""Code customers can use to apply the discount during checkout."""

    starts_at: Nullable[datetime]
    r"""Timestamp after which the discount is redeemable."""

    ends_at: Nullable[datetime]
    r"""Timestamp after which the discount is no longer redeemable."""

    max_redemptions: Nullable[int]
    r"""Maximum number of times the discount can be redeemed."""

    redemptions_count: int
    r"""Number of times the discount has been redeemed."""

    organization_id: str
    r"""The organization ID."""

    products: List[DiscountProduct]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "code",
            "starts_at",
            "ends_at",
            "max_redemptions",
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
