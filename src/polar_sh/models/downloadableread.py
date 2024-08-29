"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filedownload import FileDownload, FileDownloadTypedDict
from polar_sh.types import BaseModel
from typing import TypedDict


class DownloadableReadTypedDict(TypedDict):
    id: str
    benefit_id: str
    file: FileDownloadTypedDict
    

class DownloadableRead(BaseModel):
    id: str
    benefit_id: str
    file: FileDownload
    