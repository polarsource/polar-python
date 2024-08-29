"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .oauth2client import OAuth2Client, OAuth2ClientTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar_sh.types import BaseModel
from typing import List, TypedDict


class ListResourceOAuth2ClientTypedDict(TypedDict):
    items: List[OAuth2ClientTypedDict]
    pagination: PaginationTypedDict
    

class ListResourceOAuth2Client(BaseModel):
    items: List[OAuth2Client]
    pagination: Pagination
    