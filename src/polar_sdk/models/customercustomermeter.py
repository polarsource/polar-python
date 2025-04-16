"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customercustomermetermeter import (
    CustomerCustomerMeterMeter,
    CustomerCustomerMeterMeterTypedDict,
)
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class CustomerCustomerMeterTypedDict(TypedDict):
    id: str
    r"""The ID of the object."""
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    customer_id: str
    r"""The ID of the customer."""
    meter_id: str
    r"""The ID of the meter."""
    consumed_units: float
    r"""The number of consumed units."""
    credited_units: int
    r"""The number of credited units."""
    balance: float
    r"""The balance of the meter, i.e. the difference between credited and consumed units. Never goes negative."""
    meter: CustomerCustomerMeterMeterTypedDict


class CustomerCustomerMeter(BaseModel):
    id: str
    r"""The ID of the object."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    customer_id: str
    r"""The ID of the customer."""

    meter_id: str
    r"""The ID of the meter."""

    consumed_units: float
    r"""The number of consumed units."""

    credited_units: int
    r"""The number of credited units."""

    balance: float
    r"""The balance of the meter, i.e. the difference between credited and consumed units. Never goes negative."""

    meter: CustomerCustomerMeterMeter

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
