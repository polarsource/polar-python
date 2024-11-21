"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitarticles import BenefitArticles, BenefitArticlesTypedDict
from .benefitbase import BenefitBase, BenefitBaseTypedDict
from .productmediafileread import ProductMediaFileRead, ProductMediaFileReadTypedDict
from .productprice import ProductPrice, ProductPriceTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Union
from typing_extensions import TypedDict


CheckoutLinkProductBenefitsTypedDict = Union[
    BenefitBaseTypedDict, BenefitArticlesTypedDict
]


CheckoutLinkProductBenefits = Union[BenefitBase, BenefitArticles]


class CheckoutLinkProductTypedDict(TypedDict):
    r"""Product data for a checkout link."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the product."""
    name: str
    r"""The name of the product."""
    description: Nullable[str]
    r"""The description of the product."""
    is_recurring: bool
    r"""Whether the product is a subscription tier."""
    is_archived: bool
    r"""Whether the product is archived and no longer available."""
    organization_id: str
    r"""The ID of the organization owning the product."""
    prices: List[ProductPriceTypedDict]
    r"""List of prices for this product."""
    benefits: List[CheckoutLinkProductBenefitsTypedDict]
    r"""List of benefits granted by the product."""
    medias: List[ProductMediaFileReadTypedDict]
    r"""List of medias associated to the product."""


class CheckoutLinkProduct(BaseModel):
    r"""Product data for a checkout link."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the product."""

    name: str
    r"""The name of the product."""

    description: Nullable[str]
    r"""The description of the product."""

    is_recurring: bool
    r"""Whether the product is a subscription tier."""

    is_archived: bool
    r"""Whether the product is archived and no longer available."""

    organization_id: str
    r"""The ID of the organization owning the product."""

    prices: List[ProductPrice]
    r"""List of prices for this product."""

    benefits: List[CheckoutLinkProductBenefits]
    r"""List of benefits granted by the product."""

    medias: List[ProductMediaFileRead]
    r"""List of medias associated to the product."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at", "description"]
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
