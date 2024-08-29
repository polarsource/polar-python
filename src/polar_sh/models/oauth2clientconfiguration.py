"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sh.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class OAuth2ClientConfigurationTokenEndpointAuthMethod(str, Enum):
    CLIENT_SECRET_BASIC = "client_secret_basic"
    CLIENT_SECRET_POST = "client_secret_post"
    NONE = "none"

class OAuth2ClientConfigurationGrantTypes(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"

class OAuth2ClientConfigurationResponseTypes(str, Enum):
    CODE = "code"

class OAuth2ClientConfigurationTypedDict(TypedDict):
    redirect_uris: List[str]
    client_name: str
    token_endpoint_auth_method: NotRequired[OAuth2ClientConfigurationTokenEndpointAuthMethod]
    grant_types: NotRequired[List[OAuth2ClientConfigurationGrantTypes]]
    response_types: NotRequired[List[OAuth2ClientConfigurationResponseTypes]]
    scope: NotRequired[str]
    client_uri: NotRequired[Nullable[str]]
    logo_uri: NotRequired[Nullable[str]]
    tos_uri: NotRequired[Nullable[str]]
    policy_uri: NotRequired[Nullable[str]]
    

class OAuth2ClientConfiguration(BaseModel):
    redirect_uris: List[str]
    client_name: str
    token_endpoint_auth_method: Optional[OAuth2ClientConfigurationTokenEndpointAuthMethod] = OAuth2ClientConfigurationTokenEndpointAuthMethod.CLIENT_SECRET_POST
    grant_types: Optional[List[OAuth2ClientConfigurationGrantTypes]] = None
    response_types: Optional[List[OAuth2ClientConfigurationResponseTypes]] = None
    scope: Optional[str] = "openid profile email user:read organizations:read organizations:write products:read products:write benefits:read benefits:write files:read files:write subscriptions:read subscriptions:write orders:read metrics:read articles:read articles:write webhooks:read webhooks:write external_organizations:read repositories:read repositories:write issues:read issues:write user:benefits:read user:orders:read user:subscriptions:read user:subscriptions:write user:downloadables:read user:advertisement_campaigns:read user:advertisement_campaigns:write"
    client_uri: OptionalNullable[str] = UNSET
    logo_uri: OptionalNullable[str] = UNSET
    tos_uri: OptionalNullable[str] = UNSET
    policy_uri: OptionalNullable[str] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["token_endpoint_auth_method", "grant_types", "response_types", "scope", "client_uri", "logo_uri", "tos_uri", "policy_uri"]
        nullable_fields = ["client_uri", "logo_uri", "tos_uri", "policy_uri"]
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
        