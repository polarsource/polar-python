"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict, Optional, TypedDict
from typing_extensions import NotRequired


class S3FileUploadPartTypedDict(TypedDict):
    number: int
    chunk_start: int
    chunk_end: int
    url: str
    expires_at: datetime
    checksum_sha256_base64: NotRequired[Nullable[str]]
    headers: NotRequired[Dict[str, str]]


class S3FileUploadPart(BaseModel):
    number: int

    chunk_start: int

    chunk_end: int

    url: str

    expires_at: datetime

    checksum_sha256_base64: OptionalNullable[str] = UNSET

    headers: Optional[Dict[str, str]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["checksum_sha256_base64", "headers"]
        nullable_fields = ["checksum_sha256_base64"]
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
