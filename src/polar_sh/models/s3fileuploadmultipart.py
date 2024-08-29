"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .s3fileuploadpart import S3FileUploadPart, S3FileUploadPartTypedDict
from polar_sh.types import BaseModel
from typing import List, TypedDict


class S3FileUploadMultipartTypedDict(TypedDict):
    id: str
    path: str
    parts: List[S3FileUploadPartTypedDict]
    

class S3FileUploadMultipart(BaseModel):
    id: str
    path: str
    parts: List[S3FileUploadPart]
    