"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .externalorganization import ExternalOrganization, ExternalOrganizationTypedDict
from .organization import Organization, OrganizationTypedDict
from .platforms import Platforms
from .repositoryprofilesettings import (
    RepositoryProfileSettings,
    RepositoryProfileSettingsTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from polar_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated, TypedDict


class RepositoryTypedDict(TypedDict):
    id: str
    is_private: bool
    name: str
    description: Nullable[str]
    stars: Nullable[int]
    license: Nullable[str]
    homepage: Nullable[str]
    profile_settings: Nullable[RepositoryProfileSettingsTypedDict]
    r"""Settings for the repository profile"""
    organization: ExternalOrganizationTypedDict
    internal_organization: Nullable[OrganizationTypedDict]
    platform: Platforms


class Repository(BaseModel):
    id: str

    is_private: bool

    name: str

    description: Nullable[str]

    stars: Nullable[int]

    license: Nullable[str]

    homepage: Nullable[str]

    profile_settings: Nullable[RepositoryProfileSettings]
    r"""Settings for the repository profile"""

    organization: ExternalOrganization

    internal_organization: Nullable[Organization]

    PLATFORM: Annotated[
        Annotated[Platforms, AfterValidator(validate_const(Platforms.GITHUB))],
        pydantic.Field(alias="platform"),
    ] = Platforms.GITHUB

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "description",
            "stars",
            "license",
            "homepage",
            "profile_settings",
            "internal_organization",
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
