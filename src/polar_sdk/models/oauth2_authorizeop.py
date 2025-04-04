"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .authorizeresponseorganization import (
    AuthorizeResponseOrganization,
    AuthorizeResponseOrganizationTypedDict,
)
from .authorizeresponseuser import AuthorizeResponseUser, AuthorizeResponseUserTypedDict
from polar_sdk.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType


Oauth2AuthorizeResponseOauth2AuthorizeTypedDict = TypeAliasType(
    "Oauth2AuthorizeResponseOauth2AuthorizeTypedDict",
    Union[AuthorizeResponseUserTypedDict, AuthorizeResponseOrganizationTypedDict],
)
r"""Successful Response"""


Oauth2AuthorizeResponseOauth2Authorize = Annotated[
    Union[
        Annotated[AuthorizeResponseUser, Tag("user")],
        Annotated[AuthorizeResponseOrganization, Tag("organization")],
    ],
    Discriminator(lambda m: get_discriminator(m, "sub_type", "sub_type")),
]
r"""Successful Response"""
