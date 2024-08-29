"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class Oauth2ClientsOauth2GetClientRequestTypedDict(TypedDict):
    client_id: str
    

class Oauth2ClientsOauth2GetClientRequest(BaseModel):
    client_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    