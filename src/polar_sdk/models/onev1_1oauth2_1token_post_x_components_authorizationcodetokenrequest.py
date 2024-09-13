"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata
import pydantic
from typing import Final, TypedDict
from typing_extensions import Annotated


class GrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"


class Onev11oauth21tokenPostXComponentsAuthorizationCodeTokenRequestTypedDict(
    TypedDict
):
    client_id: str
    client_secret: str
    code: str
    redirect_uri: str


class Onev11oauth21tokenPostXComponentsAuthorizationCodeTokenRequest(BaseModel):
    client_id: Annotated[str, FieldMetadata(form=True)]

    client_secret: Annotated[str, FieldMetadata(form=True)]

    code: Annotated[str, FieldMetadata(form=True)]

    redirect_uri: Annotated[str, FieldMetadata(form=True)]

    # fmt: off
    GRANT_TYPE: Annotated[Final[GrantType], pydantic.Field(alias="grant_type"), FieldMetadata(form=True)] = GrantType.AUTHORIZATION_CODE # type: ignore
    # fmt: on
