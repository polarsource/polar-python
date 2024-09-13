"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import TypedDict


class BenefitGitHubRepositorySubscriberPropertiesTypedDict(TypedDict):
    r"""Properties available to subscribers for a benefit of type `github_repository`."""

    repository_owner: str
    r"""The owner of the repository."""
    repository_name: str
    r"""The name of the repository."""


class BenefitGitHubRepositorySubscriberProperties(BaseModel):
    r"""Properties available to subscribers for a benefit of type `github_repository`."""

    repository_owner: str
    r"""The owner of the repository."""

    repository_name: str
    r"""The name of the repository."""
