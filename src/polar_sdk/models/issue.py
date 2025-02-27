"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assignee import Assignee, AssigneeTypedDict
from .author import Author, AuthorTypedDict
from .funding import Funding, FundingTypedDict
from .label import Label, LabelTypedDict
from .platforms import Platforms
from .reactions import Reactions, ReactionsTypedDict
from .repository import Repository, RepositoryTypedDict
from .state import State
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class IssueTypedDict(TypedDict):
    id: str
    platform: Platforms
    number: int
    r"""GitHub #number"""
    title: str
    r"""GitHub issue title"""
    state: State
    issue_created_at: datetime
    needs_confirmation_solved: bool
    r"""If a maintainer needs to mark this issue as solved"""
    funding: FundingTypedDict
    repository: RepositoryTypedDict
    pledge_badge_currently_embedded: bool
    r"""If this issue currently has the Polar badge SVG embedded"""
    body: NotRequired[Nullable[str]]
    r"""GitHub issue body"""
    comments: NotRequired[Nullable[int]]
    r"""Number of GitHub comments made on the issue"""
    labels: NotRequired[List[LabelTypedDict]]
    author: NotRequired[Nullable[AuthorTypedDict]]
    r"""GitHub author"""
    assignees: NotRequired[Nullable[List[AssigneeTypedDict]]]
    r"""GitHub assignees"""
    reactions: NotRequired[Nullable[ReactionsTypedDict]]
    r"""GitHub reactions"""
    issue_closed_at: NotRequired[Nullable[datetime]]
    issue_modified_at: NotRequired[Nullable[datetime]]
    confirmed_solved_at: NotRequired[Nullable[datetime]]
    r"""If this issue has been marked as confirmed solved through Polar"""
    upfront_split_to_contributors: NotRequired[Nullable[int]]
    r"""Share of rewrads that will be rewarded to contributors of this issue. A number between 0 and 100 (inclusive)."""
    badge_custom_content: NotRequired[Nullable[str]]
    r"""Optional custom badge SVG promotional content"""


class Issue(BaseModel):
    id: str

    platform: Platforms

    number: int
    r"""GitHub #number"""

    title: str
    r"""GitHub issue title"""

    state: State

    issue_created_at: datetime

    needs_confirmation_solved: bool
    r"""If a maintainer needs to mark this issue as solved"""

    funding: Funding

    repository: Repository

    pledge_badge_currently_embedded: bool
    r"""If this issue currently has the Polar badge SVG embedded"""

    body: OptionalNullable[str] = UNSET
    r"""GitHub issue body"""

    comments: OptionalNullable[int] = UNSET
    r"""Number of GitHub comments made on the issue"""

    labels: Optional[List[Label]] = None

    author: OptionalNullable[Author] = UNSET
    r"""GitHub author"""

    assignees: OptionalNullable[List[Assignee]] = UNSET
    r"""GitHub assignees"""

    reactions: OptionalNullable[Reactions] = UNSET
    r"""GitHub reactions"""

    issue_closed_at: OptionalNullable[datetime] = UNSET

    issue_modified_at: OptionalNullable[datetime] = UNSET

    confirmed_solved_at: OptionalNullable[datetime] = UNSET
    r"""If this issue has been marked as confirmed solved through Polar"""

    upfront_split_to_contributors: OptionalNullable[int] = UNSET
    r"""Share of rewrads that will be rewarded to contributors of this issue. A number between 0 and 100 (inclusive)."""

    badge_custom_content: OptionalNullable[str] = UNSET
    r"""Optional custom badge SVG promotional content"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "body",
            "comments",
            "labels",
            "author",
            "assignees",
            "reactions",
            "issue_closed_at",
            "issue_modified_at",
            "confirmed_solved_at",
            "upfront_split_to_contributors",
            "badge_custom_content",
        ]
        nullable_fields = [
            "body",
            "comments",
            "author",
            "assignees",
            "reactions",
            "issue_closed_at",
            "issue_modified_at",
            "confirmed_solved_at",
            "upfront_split_to_contributors",
            "badge_custom_content",
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
