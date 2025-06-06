"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .product import Product, ProductTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookProductUpdatedPayloadTypedDict(TypedDict):
    r"""Sent when a product is updated.

    **Discord & Slack support:** Basic
    """

    data: ProductTypedDict
    r"""A product."""
    type: Literal["product.updated"]


class WebhookProductUpdatedPayload(BaseModel):
    r"""Sent when a product is updated.

    **Discord & Slack support:** Basic
    """

    data: Product
    r"""A product."""

    TYPE: Annotated[
        Annotated[
            Literal["product.updated"],
            AfterValidator(validate_const("product.updated")),
        ],
        pydantic.Field(alias="type"),
    ] = "product.updated"
