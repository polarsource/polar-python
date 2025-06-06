"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk import utils
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated


class NotPaidOrderData(BaseModel):
    detail: str

    ERROR: Annotated[
        Annotated[
            Literal["NotPaidOrder"], AfterValidator(validate_const("NotPaidOrder"))
        ],
        pydantic.Field(alias="error"),
    ] = "NotPaidOrder"


class NotPaidOrder(Exception):
    data: NotPaidOrderData

    def __init__(self, data: NotPaidOrderData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, NotPaidOrderData)
