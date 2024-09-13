"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .licensekeyread import LicenseKeyRead, LicenseKeyReadTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class LicenseKeyActivationReadMetaTypedDict(TypedDict):
    pass


class LicenseKeyActivationReadMeta(BaseModel):
    pass


class LicenseKeyActivationReadTypedDict(TypedDict):
    id: str
    license_key_id: str
    label: str
    meta: LicenseKeyActivationReadMetaTypedDict
    created_at: datetime
    modified_at: Nullable[datetime]
    license_key: LicenseKeyReadTypedDict


class LicenseKeyActivationRead(BaseModel):
    id: str

    license_key_id: str

    label: str

    meta: LicenseKeyActivationReadMeta

    created_at: datetime

    modified_at: Nullable[datetime]

    license_key: LicenseKeyRead

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
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
