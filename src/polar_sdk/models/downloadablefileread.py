"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class DownloadableFileReadTypedDict(TypedDict):
    r"""File to be associated with the downloadables benefit."""

    id: str
    r"""The ID of the object."""
    organization_id: str
    name: str
    path: str
    mime_type: str
    size: int
    storage_version: Nullable[str]
    checksum_etag: Nullable[str]
    checksum_sha256_base64: Nullable[str]
    checksum_sha256_hex: Nullable[str]
    last_modified_at: Nullable[datetime]
    version: Nullable[str]
    is_uploaded: bool
    created_at: datetime
    size_readable: str
    service: Literal["downloadable"]


class DownloadableFileRead(BaseModel):
    r"""File to be associated with the downloadables benefit."""

    id: str
    r"""The ID of the object."""

    organization_id: str

    name: str

    path: str

    mime_type: str

    size: int

    storage_version: Nullable[str]

    checksum_etag: Nullable[str]

    checksum_sha256_base64: Nullable[str]

    checksum_sha256_hex: Nullable[str]

    last_modified_at: Nullable[datetime]

    version: Nullable[str]

    is_uploaded: bool

    created_at: datetime

    size_readable: str

    SERVICE: Annotated[
        Annotated[
            Literal["downloadable"], AfterValidator(validate_const("downloadable"))
        ],
        pydantic.Field(alias="service"),
    ] = "downloadable"

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "storage_version",
            "checksum_etag",
            "checksum_sha256_base64",
            "checksum_sha256_hex",
            "last_modified_at",
            "version",
        ]
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
