"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .platforms import Platforms
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Final, TypedDict
from typing_extensions import Annotated


class ExternalOrganizationTypedDict(TypedDict):
    id: str
    name: str
    avatar_url: str
    is_personal: bool
    bio: Nullable[str]
    pretty_name: Nullable[str]
    company: Nullable[str]
    blog: Nullable[str]
    location: Nullable[str]
    email: Nullable[str]
    twitter_username: Nullable[str]
    organization_id: Nullable[str]
    platform: Platforms


class ExternalOrganization(BaseModel):
    id: str

    name: str

    avatar_url: str

    is_personal: bool

    bio: Nullable[str]

    pretty_name: Nullable[str]

    company: Nullable[str]

    blog: Nullable[str]

    location: Nullable[str]

    email: Nullable[str]

    twitter_username: Nullable[str]

    organization_id: Nullable[str]

    # fmt: off
    PLATFORM: Annotated[Final[Platforms], pydantic.Field(alias="platform")] = Platforms.GITHUB # type: ignore
    # fmt: on

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "bio",
            "pretty_name",
            "company",
            "blog",
            "location",
            "email",
            "twitter_username",
            "organization_id",
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
