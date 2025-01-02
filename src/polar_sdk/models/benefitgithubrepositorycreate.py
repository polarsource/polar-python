"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitgithubrepositorycreateproperties import (
    BenefitGitHubRepositoryCreateProperties,
    BenefitGitHubRepositoryCreatePropertiesTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class BenefitGitHubRepositoryCreateTypedDict(TypedDict):
    description: str
    r"""The description of the benefit. Will be displayed on products having this benefit."""
    properties: BenefitGitHubRepositoryCreatePropertiesTypedDict
    r"""Properties to create a benefit of type `github_repository`."""
    type: Literal["github_repository"]
    organization_id: NotRequired[Nullable[str]]
    r"""The ID of the organization owning the benefit. **Required unless you use an organization token.**"""


class BenefitGitHubRepositoryCreate(BaseModel):
    description: str
    r"""The description of the benefit. Will be displayed on products having this benefit."""

    properties: BenefitGitHubRepositoryCreateProperties
    r"""Properties to create a benefit of type `github_repository`."""

    TYPE: Annotated[
        Annotated[
            Literal["github_repository"],
            AfterValidator(validate_const("github_repository")),
        ],
        pydantic.Field(alias="type"),
    ] = "github_repository"

    organization_id: OptionalNullable[str] = UNSET
    r"""The ID of the organization owning the benefit. **Required unless you use an organization token.**"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id"]
        nullable_fields = ["organization_id"]
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
