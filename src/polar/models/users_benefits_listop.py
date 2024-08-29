"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefittype import BenefitType
from .listresource_annotated_union_benefitarticlessubscriber_benefitadssubscriber_benefitdiscordsubscriber_benefitcustomsubscriber_benefitgithubrepositorysubscriber_benefitdownloadablessubscriber_discriminator_mergejsonschema_ import ListResourceAnnotatedUnionBenefitArticlesSubscriberBenefitAdsSubscriberBenefitDiscordSubscriberBenefitCustomSubscriberBenefitGitHubRepositorySubscriberBenefitDownloadablesSubscriberDiscriminatorMergeJSONSchema, ListResourceAnnotatedUnionBenefitArticlesSubscriberBenefitAdsSubscriberBenefitDiscordSubscriberBenefitCustomSubscriberBenefitGitHubRepositorySubscriberBenefitDownloadablesSubscriberDiscriminatorMergeJSONSchemaTypedDict
from .userbenefitsortproperty import UserBenefitSortProperty
from polar.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


BenefitTypeFilterTypedDict = Union[BenefitType, List[BenefitType]]
r"""Filter by benefit type."""


BenefitTypeFilter = Union[BenefitType, List[BenefitType]]
r"""Filter by benefit type."""


OrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


OrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


OrderIDFilterTypedDict = Union[str, List[str]]
r"""Filter by order ID."""


OrderIDFilter = Union[str, List[str]]
r"""Filter by order ID."""


SubscriptionIDFilterTypedDict = Union[str, List[str]]
r"""Filter by subscription ID."""


SubscriptionIDFilter = Union[str, List[str]]
r"""Filter by subscription ID."""


class UsersBenefitsListRequestTypedDict(TypedDict):
    type_filter: NotRequired[Nullable[BenefitTypeFilterTypedDict]]
    r"""Filter by benefit type."""
    organization_id: NotRequired[Nullable[OrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    order_id: NotRequired[Nullable[OrderIDFilterTypedDict]]
    r"""Filter by order ID."""
    subscription_id: NotRequired[Nullable[SubscriptionIDFilterTypedDict]]
    r"""Filter by subscription ID."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[UserBenefitSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    

class UsersBenefitsListRequest(BaseModel):
    type_filter: Annotated[OptionalNullable[BenefitTypeFilter], pydantic.Field(alias="type"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by benefit type."""
    organization_id: Annotated[OptionalNullable[OrganizationIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by organization ID."""
    order_id: Annotated[OptionalNullable[OrderIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by order ID."""
    subscription_id: Annotated[OptionalNullable[SubscriptionIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by subscription ID."""
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""Page number, defaults to 1."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: Annotated[OptionalNullable[List[UserBenefitSortProperty]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type_filter", "organization_id", "order_id", "subscription_id", "page", "limit", "sorting"]
        nullable_fields = ["type_filter", "organization_id", "order_id", "subscription_id", "sorting"]
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
        

class UsersBenefitsListResponseTypedDict(TypedDict):
    result: ListResourceAnnotatedUnionBenefitArticlesSubscriberBenefitAdsSubscriberBenefitDiscordSubscriberBenefitCustomSubscriberBenefitGitHubRepositorySubscriberBenefitDownloadablesSubscriberDiscriminatorMergeJSONSchemaTypedDict
    

class UsersBenefitsListResponse(BaseModel):
    next: Callable[[], Optional[UsersBenefitsListResponse]]
    
    result: ListResourceAnnotatedUnionBenefitArticlesSubscriberBenefitAdsSubscriberBenefitDiscordSubscriberBenefitCustomSubscriberBenefitGitHubRepositorySubscriberBenefitDownloadablesSubscriberDiscriminatorMergeJSONSchema
    
