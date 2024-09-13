"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ArticleCreateArticleByline(str, Enum):
    r"""If the user or organization should be credited in the byline."""

    USER = "user"
    ORGANIZATION = "organization"


class ArticleCreateArticleVisibility(str, Enum):
    PUBLIC = "public"
    HIDDEN = "hidden"
    PRIVATE = "private"


class ArticleCreateTypedDict(TypedDict):
    title: str
    r"""Title of the article."""
    slug: NotRequired[Nullable[str]]
    r"""Slug of the article to be used in URLs. If no slug is provided one will be generated from the title."""
    body: NotRequired[Nullable[str]]
    r"""Body in string format. Either one of body or body_base64 is required."""
    body_base64: NotRequired[Nullable[str]]
    r"""Body in base64-encoded format. Can be helpful to bypass Web Application Firewalls (WAF). Either one of body or body_base64 is required."""
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the article. **Required unless you use an organization token.**"""
    byline: NotRequired[ArticleCreateArticleByline]
    r"""If the user or organization should be credited in the byline."""
    visibility: NotRequired[ArticleCreateArticleVisibility]
    paid_subscribers_only: NotRequired[bool]
    r"""Set to true to only make this article available for subscribers to a paid subscription tier in the organization."""
    paid_subscribers_only_ends_at: NotRequired[Nullable[datetime]]
    r"""If specified, time at which the article should no longer be restricted to paid subscribers. Only relevant if `paid_subscribers_only` is true."""
    published_at: NotRequired[Nullable[datetime]]
    r"""Time of publishing. If this date is in the future, the post will be scheduled to publish at this time. If visibility is 'public', published_at will default to the current time."""
    notify_subscribers: NotRequired[Nullable[bool]]
    r"""Set to true to deliver this article via email and/or notifications to subscribers."""
    is_pinned: NotRequired[Nullable[bool]]
    r"""If the article should be pinned"""
    og_image_url: NotRequired[Nullable[str]]
    r"""Custom og:image URL value"""
    og_description: NotRequired[Nullable[str]]
    r"""Custom og:description value"""


class ArticleCreate(BaseModel):
    title: str
    r"""Title of the article."""

    slug: OptionalNullable[str] = UNSET
    r"""Slug of the article to be used in URLs. If no slug is provided one will be generated from the title."""

    body: OptionalNullable[str] = UNSET
    r"""Body in string format. Either one of body or body_base64 is required."""

    body_base64: OptionalNullable[str] = UNSET
    r"""Body in base64-encoded format. Can be helpful to bypass Web Application Firewalls (WAF). Either one of body or body_base64 is required."""

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the article. **Required unless you use an organization token.**"""

    byline: Optional[ArticleCreateArticleByline] = (
        ArticleCreateArticleByline.ORGANIZATION
    )
    r"""If the user or organization should be credited in the byline."""

    visibility: Optional[ArticleCreateArticleVisibility] = (
        ArticleCreateArticleVisibility.PRIVATE
    )

    paid_subscribers_only: Optional[bool] = False
    r"""Set to true to only make this article available for subscribers to a paid subscription tier in the organization."""

    paid_subscribers_only_ends_at: OptionalNullable[datetime] = UNSET
    r"""If specified, time at which the article should no longer be restricted to paid subscribers. Only relevant if `paid_subscribers_only` is true."""

    published_at: OptionalNullable[datetime] = UNSET
    r"""Time of publishing. If this date is in the future, the post will be scheduled to publish at this time. If visibility is 'public', published_at will default to the current time."""

    notify_subscribers: OptionalNullable[bool] = UNSET
    r"""Set to true to deliver this article via email and/or notifications to subscribers."""

    is_pinned: OptionalNullable[bool] = UNSET
    r"""If the article should be pinned"""

    og_image_url: OptionalNullable[str] = UNSET
    r"""Custom og:image URL value"""

    og_description: OptionalNullable[str] = UNSET
    r"""Custom og:description value"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "slug",
            "body",
            "body_base64",
            "organization_id",
            "byline",
            "visibility",
            "paid_subscribers_only",
            "paid_subscribers_only_ends_at",
            "published_at",
            "notify_subscribers",
            "is_pinned",
            "og_image_url",
            "og_description",
        ]
        nullable_fields = [
            "slug",
            "body",
            "body_base64",
            "organization_id",
            "paid_subscribers_only_ends_at",
            "published_at",
            "notify_subscribers",
            "is_pinned",
            "og_image_url",
            "og_description",
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
