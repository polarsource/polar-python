"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitgithubrepositoryproperties import (
    BenefitGitHubRepositoryProperties,
    BenefitGitHubRepositoryPropertiesTypedDict,
)
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, Literal, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


BenefitGitHubRepositoryMetadataTypedDict = TypeAliasType(
    "BenefitGitHubRepositoryMetadataTypedDict", Union[str, int, float, bool]
)


BenefitGitHubRepositoryMetadata = TypeAliasType(
    "BenefitGitHubRepositoryMetadata", Union[str, int, float, bool]
)


class BenefitGitHubRepositoryTypedDict(TypedDict):
    r"""A benefit of type `github_repository`.

    Use it to automatically invite your backers to a private GitHub repository.
    """

    id: str
    r"""The ID of the benefit."""
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    metadata: Dict[str, BenefitGitHubRepositoryMetadataTypedDict]
    description: str
    r"""The description of the benefit."""
    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""
    deletable: bool
    r"""Whether the benefit is deletable."""
    organization_id: str
    r"""The ID of the organization owning the benefit."""
    properties: BenefitGitHubRepositoryPropertiesTypedDict
    r"""Properties for a benefit of type `github_repository`."""
    type: Literal["github_repository"]


class BenefitGitHubRepository(BaseModel):
    r"""A benefit of type `github_repository`.

    Use it to automatically invite your backers to a private GitHub repository.
    """

    id: str
    r"""The ID of the benefit."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    metadata: Dict[str, BenefitGitHubRepositoryMetadata]

    description: str
    r"""The description of the benefit."""

    selectable: bool
    r"""Whether the benefit is selectable when creating a product."""

    deletable: bool
    r"""Whether the benefit is deletable."""

    organization_id: str
    r"""The ID of the organization owning the benefit."""

    properties: BenefitGitHubRepositoryProperties
    r"""Properties for a benefit of type `github_repository`."""

    TYPE: Annotated[
        Annotated[
            Literal["github_repository"],
            AfterValidator(validate_const("github_repository")),
        ],
        pydantic.Field(alias="type"),
    ] = "github_repository"

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["modified_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
