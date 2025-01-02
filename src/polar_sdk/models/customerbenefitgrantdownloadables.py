"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitdownloadablessubscriber import (
    BenefitDownloadablesSubscriber,
    BenefitDownloadablesSubscriberTypedDict,
)
from .benefitgrantdownloadablesproperties import (
    BenefitGrantDownloadablesProperties,
    BenefitGrantDownloadablesPropertiesTypedDict,
)
from .customerportalcustomer import (
    CustomerPortalCustomer,
    CustomerPortalCustomerTypedDict,
)
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class CustomerBenefitGrantDownloadablesTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    granted_at: Nullable[datetime]
    revoked_at: Nullable[datetime]
    customer_id: str
    benefit_id: str
    subscription_id: Nullable[str]
    order_id: Nullable[str]
    is_granted: bool
    is_revoked: bool
    customer: CustomerPortalCustomerTypedDict
    benefit: BenefitDownloadablesSubscriberTypedDict
    properties: BenefitGrantDownloadablesPropertiesTypedDict


class CustomerBenefitGrantDownloadables(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    granted_at: Nullable[datetime]

    revoked_at: Nullable[datetime]

    customer_id: str

    benefit_id: str

    subscription_id: Nullable[str]

    order_id: Nullable[str]

    is_granted: bool

    is_revoked: bool

    customer: CustomerPortalCustomer

    benefit: BenefitDownloadablesSubscriber

    properties: BenefitGrantDownloadablesProperties

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "modified_at",
            "granted_at",
            "revoked_at",
            "subscription_id",
            "order_id",
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
