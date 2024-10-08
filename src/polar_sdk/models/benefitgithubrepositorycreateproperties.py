"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class BenefitGitHubRepositoryCreatePropertiesPermission(str, Enum):
    r"""The permission level to grant. Read more about roles and their permissions on [GitHub documentation](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role)."""

    PULL = "pull"
    TRIAGE = "triage"
    PUSH = "push"
    MAINTAIN = "maintain"
    ADMIN = "admin"


class BenefitGitHubRepositoryCreatePropertiesTypedDict(TypedDict):
    r"""Properties to create a benefit of type `github_repository`."""

    permission: BenefitGitHubRepositoryCreatePropertiesPermission
    r"""The permission level to grant. Read more about roles and their permissions on [GitHub documentation](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role)."""
    repository_id: NotRequired[Nullable[str]]
    repository_owner: NotRequired[Nullable[str]]
    r"""The owner of the repository."""
    repository_name: NotRequired[Nullable[str]]
    r"""The name of the repository."""


class BenefitGitHubRepositoryCreateProperties(BaseModel):
    r"""Properties to create a benefit of type `github_repository`."""

    permission: BenefitGitHubRepositoryCreatePropertiesPermission
    r"""The permission level to grant. Read more about roles and their permissions on [GitHub documentation](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role)."""

    repository_id: OptionalNullable[str] = UNSET

    repository_owner: OptionalNullable[str] = UNSET
    r"""The owner of the repository."""

    repository_name: OptionalNullable[str] = UNSET
    r"""The name of the repository."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["repository_id", "repository_owner", "repository_name"]
        nullable_fields = ["repository_id", "repository_owner", "repository_name"]
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
