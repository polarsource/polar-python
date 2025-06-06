"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .missinginvoicebillingdetails import MissingInvoiceBillingDetailsData
from .notpaidorder import NotPaidOrderData
from polar_sdk import utils
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class OrdersGenerateInvoiceRequestTypedDict(TypedDict):
    id: str
    r"""The order ID."""


class OrdersGenerateInvoiceRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The order ID."""


OrdersGenerateInvoiceResponse422OrdersGenerateInvoiceUnion = TypeAliasType(
    "OrdersGenerateInvoiceResponse422OrdersGenerateInvoiceUnion",
    Union[MissingInvoiceBillingDetailsData, NotPaidOrderData],
)
r"""Order is not paid or is missing billing name or address."""


class OrdersGenerateInvoiceResponse422OrdersGenerateInvoice(Exception):
    r"""Order is not paid or is missing billing name or address."""

    data: OrdersGenerateInvoiceResponse422OrdersGenerateInvoiceUnion

    def __init__(
        self, data: OrdersGenerateInvoiceResponse422OrdersGenerateInvoiceUnion
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, OrdersGenerateInvoiceResponse422OrdersGenerateInvoiceUnion
        )
