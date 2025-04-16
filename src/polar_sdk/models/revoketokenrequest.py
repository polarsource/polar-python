"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class TokenTypeHint(str, Enum):
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"


class RevokeTokenRequestTypedDict(TypedDict):
    token: str
    client_id: str
    client_secret: str
    token_type_hint: NotRequired[Nullable[TokenTypeHint]]


class RevokeTokenRequest(BaseModel):
    token: Annotated[str, FieldMetadata(form=True)]

    client_id: Annotated[str, FieldMetadata(form=True)]

    client_secret: Annotated[str, FieldMetadata(form=True)]

    token_type_hint: Annotated[
        OptionalNullable[TokenTypeHint], FieldMetadata(form=True)
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["token_type_hint"]
        nullable_fields = ["token_type_hint"]
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
