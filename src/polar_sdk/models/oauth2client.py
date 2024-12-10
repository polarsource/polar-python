"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TokenEndpointAuthMethod(str, Enum):
    CLIENT_SECRET_BASIC = "client_secret_basic"
    CLIENT_SECRET_POST = "client_secret_post"
    NONE = "none"


class GrantTypes(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"


class ResponseTypes(str, Enum):
    CODE = "code"


class OAuth2ClientTypedDict(TypedDict):
    redirect_uris: List[str]
    client_name: str
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    client_id: str
    client_secret: str
    client_id_issued_at: int
    client_secret_expires_at: int
    token_endpoint_auth_method: NotRequired[TokenEndpointAuthMethod]
    grant_types: NotRequired[List[GrantTypes]]
    response_types: NotRequired[List[ResponseTypes]]
    scope: NotRequired[str]
    client_uri: NotRequired[Nullable[str]]
    logo_uri: NotRequired[Nullable[str]]
    tos_uri: NotRequired[Nullable[str]]
    policy_uri: NotRequired[Nullable[str]]


class OAuth2Client(BaseModel):
    redirect_uris: List[str]

    client_name: str

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    client_id: str

    client_secret: str

    client_id_issued_at: int

    client_secret_expires_at: int

    token_endpoint_auth_method: Optional[TokenEndpointAuthMethod] = (
        TokenEndpointAuthMethod.CLIENT_SECRET_POST
    )

    grant_types: Optional[List[GrantTypes]] = None

    response_types: Optional[List[ResponseTypes]] = None

    scope: Optional[str] = (
        "openid profile email user:read organizations:read organizations:write custom_fields:read custom_fields:write discounts:read discounts:write checkout_links:read checkout_links:write checkouts:read checkouts:write products:read products:write benefits:read benefits:write files:read files:write subscriptions:read subscriptions:write orders:read metrics:read webhooks:read webhooks:write external_organizations:read license_keys:read license_keys:write repositories:read repositories:write issues:read issues:write user:benefits:read user:orders:read user:subscriptions:read user:subscriptions:write user:downloadables:read user:license_keys:read user:advertisement_campaigns:read user:advertisement_campaigns:write"
    )

    client_uri: OptionalNullable[str] = UNSET

    logo_uri: OptionalNullable[str] = UNSET

    tos_uri: OptionalNullable[str] = UNSET

    policy_uri: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "token_endpoint_auth_method",
            "grant_types",
            "response_types",
            "scope",
            "client_uri",
            "logo_uri",
            "tos_uri",
            "policy_uri",
        ]
        nullable_fields = [
            "modified_at",
            "client_uri",
            "logo_uri",
            "tos_uri",
            "policy_uri",
        ]
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
