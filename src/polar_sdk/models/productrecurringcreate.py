"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attachedcustomfieldcreate import (
    AttachedCustomFieldCreate,
    AttachedCustomFieldCreateTypedDict,
)
from .productpricerecurringfixedcreate import (
    ProductPriceRecurringFixedCreate,
    ProductPriceRecurringFixedCreateTypedDict,
)
from .productpricerecurringfreecreate import (
    ProductPriceRecurringFreeCreate,
    ProductPriceRecurringFreeCreateTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypedDict


ProductRecurringCreateMetadataTypedDict = Union[str, int, bool]


ProductRecurringCreateMetadata = Union[str, int, bool]


ProductRecurringCreatePricesTypedDict = Union[
    List[ProductPriceRecurringFixedCreateTypedDict],
    List[ProductPriceRecurringFreeCreateTypedDict],
]
r"""List of available prices for this product."""


ProductRecurringCreatePrices = Union[
    List[ProductPriceRecurringFixedCreate], List[ProductPriceRecurringFreeCreate]
]
r"""List of available prices for this product."""


class ProductRecurringCreateTypedDict(TypedDict):
    r"""Schema to create a recurring product, i.e. a subscription."""

    name: str
    r"""The name of the product."""
    prices: ProductRecurringCreatePricesTypedDict
    r"""List of available prices for this product."""
    metadata: NotRequired[Dict[str, ProductRecurringCreateMetadataTypedDict]]
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """
    description: NotRequired[Nullable[str]]
    r"""The description of the product."""
    medias: NotRequired[Nullable[List[str]]]
    r"""List of file IDs. Each one must be on the same organization as the product, of type `product_media` and correctly uploaded."""
    attached_custom_fields: NotRequired[List[AttachedCustomFieldCreateTypedDict]]
    r"""List of custom fields to attach."""
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the product. **Required unless you use an organization token.**"""


class ProductRecurringCreate(BaseModel):
    r"""Schema to create a recurring product, i.e. a subscription."""

    name: str
    r"""The name of the product."""

    prices: ProductRecurringCreatePrices
    r"""List of available prices for this product."""

    metadata: Optional[Dict[str, ProductRecurringCreateMetadata]] = None
    r"""Key-value object allowing you to store additional information.

    The key must be a string with a maximum length of **40 characters**.
    The value must be either:

    * A string with a maximum length of **500 characters**
    * An integer
    * A boolean

    You can store up to **50 key-value pairs**.
    """

    description: OptionalNullable[str] = UNSET
    r"""The description of the product."""

    medias: OptionalNullable[List[str]] = UNSET
    r"""List of file IDs. Each one must be on the same organization as the product, of type `product_media` and correctly uploaded."""

    attached_custom_fields: Optional[List[AttachedCustomFieldCreate]] = None
    r"""List of custom fields to attach."""

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the product. **Required unless you use an organization token.**"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "metadata",
            "description",
            "medias",
            "attached_custom_fields",
            "organization_id",
        ]
        nullable_fields = ["description", "medias", "organization_id"]
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
