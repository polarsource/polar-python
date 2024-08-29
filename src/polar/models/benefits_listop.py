"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefittype import BenefitType
from .listresource_union_benefitarticles_benefitads_benefitcustom_benefitdiscord_benefitgithubrepository_benefitdownloadables_ import ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadables, ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadablesTypedDict
from polar.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


BenefitsListQueryParamOrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


BenefitsListQueryParamOrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


QueryParamBenefitTypeFilterTypedDict = Union[BenefitType, List[BenefitType]]
r"""Filter by benefit type."""


QueryParamBenefitTypeFilter = Union[BenefitType, List[BenefitType]]
r"""Filter by benefit type."""


class BenefitsListRequestTypedDict(TypedDict):
    organization_id: NotRequired[Nullable[BenefitsListQueryParamOrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    type_filter: NotRequired[Nullable[QueryParamBenefitTypeFilterTypedDict]]
    r"""Filter by benefit type."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    

class BenefitsListRequest(BaseModel):
    organization_id: Annotated[OptionalNullable[BenefitsListQueryParamOrganizationIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by organization ID."""
    type_filter: Annotated[OptionalNullable[QueryParamBenefitTypeFilter], pydantic.Field(alias="type"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by benefit type."""
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""Page number, defaults to 1."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "type_filter", "page", "limit"]
        nullable_fields = ["organization_id", "type_filter"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class BenefitsListResponseTypedDict(TypedDict):
    result: ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadablesTypedDict
    

class BenefitsListResponse(BaseModel):
    next: Callable[[], Optional[BenefitsListResponse]]
    
    result: ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadables
    
