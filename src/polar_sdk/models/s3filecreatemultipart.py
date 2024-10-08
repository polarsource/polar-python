"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .s3filecreatepart import S3FileCreatePart, S3FileCreatePartTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class S3FileCreateMultipartTypedDict(TypedDict):
    parts: List[S3FileCreatePartTypedDict]


class S3FileCreateMultipart(BaseModel):
    parts: List[S3FileCreatePart]
