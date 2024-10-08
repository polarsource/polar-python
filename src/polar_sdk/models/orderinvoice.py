"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class OrderInvoiceTypedDict(TypedDict):
    r"""Order's invoice data."""

    url: str
    r"""The URL to the invoice."""


class OrderInvoice(BaseModel):
    r"""Order's invoice data."""

    url: str
    r"""The URL to the invoice."""
