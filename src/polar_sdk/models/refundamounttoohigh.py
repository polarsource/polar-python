"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from polar_sdk.models import PolarError
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated


class RefundAmountTooHighData(BaseModel):
    detail: str

    ERROR: Annotated[
        Annotated[
            Literal["RefundAmountTooHigh"],
            AfterValidator(validate_const("RefundAmountTooHigh")),
        ],
        pydantic.Field(alias="error"),
    ] = "RefundAmountTooHigh"


class RefundAmountTooHigh(PolarError):
    data: RefundAmountTooHighData

    def __init__(
        self,
        data: RefundAmountTooHighData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data
