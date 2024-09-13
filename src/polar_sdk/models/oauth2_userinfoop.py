"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userinfoorganization import UserInfoOrganization, UserInfoOrganizationTypedDict
from .userinfouser import UserInfoUser, UserInfoUserTypedDict
from typing import Union


Oauth2UserinfoResponseOauth2UserinfoTypedDict = Union[
    UserInfoOrganizationTypedDict, UserInfoUserTypedDict
]
r"""Successful Response"""


Oauth2UserinfoResponseOauth2Userinfo = Union[UserInfoOrganization, UserInfoUser]
r"""Successful Response"""
