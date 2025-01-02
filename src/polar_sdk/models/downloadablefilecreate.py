"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .s3filecreatemultipart import S3FileCreateMultipart, S3FileCreateMultipartTypedDict
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class DownloadableFileCreateTypedDict(TypedDict):
    r"""Schema to create a file to be associated with the downloadables benefit."""

    name: str
    mime_type: str
    size: int
    upload: S3FileCreateMultipartTypedDict
    organization_id: NotRequired[Nullable[str]]
    checksum_sha256_base64: NotRequired[Nullable[str]]
    service: Literal["downloadable"]
    version: NotRequired[Nullable[str]]


class DownloadableFileCreate(BaseModel):
    r"""Schema to create a file to be associated with the downloadables benefit."""

    name: str

    mime_type: str

    size: int

    upload: S3FileCreateMultipart

    organization_id: OptionalNullable[str] = UNSET

    checksum_sha256_base64: OptionalNullable[str] = UNSET

    SERVICE: Annotated[
        Annotated[
            Literal["downloadable"], AfterValidator(validate_const("downloadable"))
        ],
        pydantic.Field(alias="service"),
    ] = "downloadable"

    version: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "checksum_sha256_base64", "version"]
        nullable_fields = ["organization_id", "checksum_sha256_base64", "version"]
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
