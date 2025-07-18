"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alreadyactivesubscriptionerror import AlreadyActiveSubscriptionErrorData
from .notopencheckout import NotOpenCheckoutData
import httpx
from polar_sdk.models import PolarError
from typing import Optional, Union
from typing_extensions import TypeAliasType


CheckoutForbiddenErrorUnion = TypeAliasType(
    "CheckoutForbiddenErrorUnion",
    Union[AlreadyActiveSubscriptionErrorData, NotOpenCheckoutData],
)


class CheckoutForbiddenError(PolarError):
    data: CheckoutForbiddenErrorUnion

    def __init__(
        self,
        data: CheckoutForbiddenErrorUnion,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data
