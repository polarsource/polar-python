"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .authorizeorganization import AuthorizeOrganization, AuthorizeOrganizationTypedDict
from .oauth2clientpublic import OAuth2ClientPublic, OAuth2ClientPublicTypedDict
from .scope import Scope
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal
from typing_extensions import Annotated, TypedDict


class AuthorizeResponseOrganizationTypedDict(TypedDict):
    client: OAuth2ClientPublicTypedDict
    sub: Nullable[AuthorizeOrganizationTypedDict]
    scopes: List[Scope]
    organizations: List[AuthorizeOrganizationTypedDict]
    sub_type: Literal["organization"]


class AuthorizeResponseOrganization(BaseModel):
    client: OAuth2ClientPublic

    sub: Nullable[AuthorizeOrganization]

    scopes: List[Scope]

    organizations: List[AuthorizeOrganization]

    SUB_TYPE: Annotated[
        Annotated[
            Literal["organization"], AfterValidator(validate_const("organization"))
        ],
        pydantic.Field(alias="sub_type"),
    ] = "organization"

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["sub"]
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
