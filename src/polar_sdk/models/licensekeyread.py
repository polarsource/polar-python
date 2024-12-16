"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .licensekeycustomer import LicenseKeyCustomer, LicenseKeyCustomerTypedDict
from .licensekeystatus import LicenseKeyStatus
from .licensekeyuser import LicenseKeyUser, LicenseKeyUserTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, TypedDict


class LicenseKeyReadTypedDict(TypedDict):
    id: str
    organization_id: str
    user_id: str
    customer_id: str
    user: LicenseKeyUserTypedDict
    customer: LicenseKeyCustomerTypedDict
    benefit_id: str
    r"""The benefit ID."""
    key: str
    display_key: str
    status: LicenseKeyStatus
    limit_activations: Nullable[int]
    usage: int
    limit_usage: Nullable[int]
    validations: int
    last_validated_at: Nullable[datetime]
    expires_at: Nullable[datetime]


class LicenseKeyRead(BaseModel):
    id: str

    organization_id: str

    user_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    customer_id: str

    user: LicenseKeyUser

    customer: LicenseKeyCustomer

    benefit_id: str
    r"""The benefit ID."""

    key: str

    display_key: str

    status: LicenseKeyStatus

    limit_activations: Nullable[int]

    usage: int

    limit_usage: Nullable[int]

    validations: int

    last_validated_at: Nullable[datetime]

    expires_at: Nullable[datetime]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "limit_activations",
            "limit_usage",
            "last_validated_at",
            "expires_at",
        ]
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
