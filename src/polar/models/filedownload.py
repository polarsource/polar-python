"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fileservicetypes import FileServiceTypes
from .s3downloadurl import S3DownloadURL, S3DownloadURLTypedDict
from datetime import datetime
from polar.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class FileDownloadTypedDict(TypedDict):
    id: str
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
    download: S3DownloadURLTypedDict
    version: Nullable[str]
    is_uploaded: bool
    service: FileServiceTypes
    size_readable: str
    

class FileDownload(BaseModel):
    id: str
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
    download: S3DownloadURL
    version: Nullable[str]
    is_uploaded: bool
    service: FileServiceTypes
    size_readable: str
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["storage_version", "checksum_etag", "checksum_sha256_base64", "checksum_sha256_hex", "last_modified_at", "version"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        