"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk import utils
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated


class MissingInvoiceBillingDetailsData(BaseModel):
    detail: str

    ERROR: Annotated[
        Annotated[
            Literal["MissingInvoiceBillingDetails"],
            AfterValidator(validate_const("MissingInvoiceBillingDetails")),
        ],
        pydantic.Field(alias="error"),
    ] = "MissingInvoiceBillingDetails"


class MissingInvoiceBillingDetails(Exception):
    data: MissingInvoiceBillingDetailsData

    def __init__(self, data: MissingInvoiceBillingDetailsData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, MissingInvoiceBillingDetailsData)
