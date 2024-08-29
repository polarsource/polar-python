"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_subscription_ import ListResourceSubscription, ListResourceSubscriptionTypedDict
from .subscriptionsortproperty import SubscriptionSortProperty
from .subscriptiontiertype import SubscriptionTierType
from polar_sh.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sh.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


SubscriptionsListQueryParamOrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


SubscriptionsListQueryParamOrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


SubscriptionsListQueryParamProductIDFilterTypedDict = Union[str, List[str]]
r"""Filter by product ID."""


SubscriptionsListQueryParamProductIDFilter = Union[str, List[str]]
r"""Filter by product ID."""


SubscriptionTierTypeFilterTypedDict = Union[SubscriptionTierType, List[SubscriptionTierType]]
r"""Filter by subscription tier type."""


SubscriptionTierTypeFilter = Union[SubscriptionTierType, List[SubscriptionTierType]]
r"""Filter by subscription tier type."""


class SubscriptionsListRequestTypedDict(TypedDict):
    organization_id: NotRequired[Nullable[SubscriptionsListQueryParamOrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    product_id: NotRequired[Nullable[SubscriptionsListQueryParamProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    type: NotRequired[Nullable[SubscriptionTierTypeFilterTypedDict]]
    r"""Filter by subscription tier type."""
    active: NotRequired[Nullable[bool]]
    r"""Filter by active or inactive subscription."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[SubscriptionSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    

class SubscriptionsListRequest(BaseModel):
    organization_id: Annotated[OptionalNullable[SubscriptionsListQueryParamOrganizationIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by organization ID."""
    product_id: Annotated[OptionalNullable[SubscriptionsListQueryParamProductIDFilter], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by product ID."""
    type: Annotated[OptionalNullable[SubscriptionTierTypeFilter], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by subscription tier type."""
    active: Annotated[OptionalNullable[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by active or inactive subscription."""
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""Page number, defaults to 1."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: Annotated[OptionalNullable[List[SubscriptionSortProperty]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "product_id", "type", "active", "page", "limit", "sorting"]
        nullable_fields = ["organization_id", "product_id", "type", "active", "sorting"]
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
        

class SubscriptionsListResponseTypedDict(TypedDict):
    result: ListResourceSubscriptionTypedDict
    

class SubscriptionsListResponse(BaseModel):
    next: Callable[[], Optional[SubscriptionsListResponse]]
    
    result: ListResourceSubscription
    
