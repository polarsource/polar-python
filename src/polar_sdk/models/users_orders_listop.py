"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_userorder_ import (
    ListResourceUserOrder,
    ListResourceUserOrderTypedDict,
)
from .productpricetype import ProductPriceType
from .userordersortproperty import UserOrderSortProperty
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


QueryParamOrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


QueryParamOrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


ProductIDFilterTypedDict = Union[str, List[str]]
r"""Filter by product ID."""


ProductIDFilter = Union[str, List[str]]
r"""Filter by product ID."""


ProductPriceTypeFilterTypedDict = Union[ProductPriceType, List[ProductPriceType]]
r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""


ProductPriceTypeFilter = Union[ProductPriceType, List[ProductPriceType]]
r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""


QueryParamSubscriptionIDFilterTypedDict = Union[str, List[str]]
r"""Filter by subscription ID."""


QueryParamSubscriptionIDFilter = Union[str, List[str]]
r"""Filter by subscription ID."""


class UsersOrdersListRequestTypedDict(TypedDict):
    organization_id: NotRequired[Nullable[QueryParamOrganizationIDFilterTypedDict]]
    r"""Filter by organization ID."""
    product_id: NotRequired[Nullable[ProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    product_price_type: NotRequired[Nullable[ProductPriceTypeFilterTypedDict]]
    r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""
    subscription_id: NotRequired[Nullable[QueryParamSubscriptionIDFilterTypedDict]]
    r"""Filter by subscription ID."""
    query: NotRequired[Nullable[str]]
    r"""Search by product or organization name."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[UserOrderSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class UsersOrdersListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[QueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    product_id: Annotated[
        OptionalNullable[ProductIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product ID."""

    product_price_type: Annotated[
        OptionalNullable[ProductPriceTypeFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""

    subscription_id: Annotated[
        OptionalNullable[QueryParamSubscriptionIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by subscription ID."""

    query: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Search by product or organization name."""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number, defaults to 1."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""

    sorting: Annotated[
        OptionalNullable[List[UserOrderSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "organization_id",
            "product_id",
            "product_price_type",
            "subscription_id",
            "query",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "organization_id",
            "product_id",
            "product_price_type",
            "subscription_id",
            "query",
            "sorting",
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


class UsersOrdersListResponseTypedDict(TypedDict):
    result: ListResourceUserOrderTypedDict


class UsersOrdersListResponse(BaseModel):
    next: Callable[[], Optional[UsersOrdersListResponse]]

    result: ListResourceUserOrder
