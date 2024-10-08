"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class RepositoryProfileSettingsTypedDict(TypedDict):
    description: NotRequired[Nullable[str]]
    r"""A description of the repository"""
    cover_image_url: NotRequired[Nullable[str]]
    r"""A URL to a cover image"""
    featured_organizations: NotRequired[Nullable[List[str]]]
    r"""A list of featured organizations"""
    highlighted_subscription_tiers: NotRequired[Nullable[List[str]]]
    r"""A list of highlighted subscription tiers"""
    links: NotRequired[Nullable[List[str]]]
    r"""A list of links related to the repository"""


class RepositoryProfileSettings(BaseModel):
    description: OptionalNullable[str] = UNSET
    r"""A description of the repository"""

    cover_image_url: OptionalNullable[str] = UNSET
    r"""A URL to a cover image"""

    featured_organizations: OptionalNullable[List[str]] = UNSET
    r"""A list of featured organizations"""

    highlighted_subscription_tiers: OptionalNullable[List[str]] = UNSET
    r"""A list of highlighted subscription tiers"""

    links: OptionalNullable[List[str]] = UNSET
    r"""A list of links related to the repository"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "cover_image_url",
            "featured_organizations",
            "highlighted_subscription_tiers",
            "links",
        ]
        nullable_fields = [
            "description",
            "cover_image_url",
            "featured_organizations",
            "highlighted_subscription_tiers",
            "links",
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
