"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customersubscriptionsortproperty import CustomerSubscriptionSortProperty
from .listresource_customersubscription_ import (
    ListResourceCustomerSubscription,
    ListResourceCustomerSubscriptionTypedDict,
)
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata, SecurityMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class CustomerPortalSubscriptionsListSecurityTypedDict(TypedDict):
    customer_session: str


class CustomerPortalSubscriptionsListSecurity(BaseModel):
    customer_session: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ]


CustomerPortalSubscriptionsListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "CustomerPortalSubscriptionsListQueryParamOrganizationIDFilterTypedDict",
    Union[str, List[str]],
)
r"""Filter by organization ID."""


CustomerPortalSubscriptionsListQueryParamOrganizationIDFilter = TypeAliasType(
    "CustomerPortalSubscriptionsListQueryParamOrganizationIDFilter",
    Union[str, List[str]],
)
r"""Filter by organization ID."""


CustomerPortalSubscriptionsListQueryParamProductIDFilterTypedDict = TypeAliasType(
    "CustomerPortalSubscriptionsListQueryParamProductIDFilterTypedDict",
    Union[str, List[str]],
)
r"""Filter by product ID."""


CustomerPortalSubscriptionsListQueryParamProductIDFilter = TypeAliasType(
    "CustomerPortalSubscriptionsListQueryParamProductIDFilter", Union[str, List[str]]
)
r"""Filter by product ID."""


class CustomerPortalSubscriptionsListRequestTypedDict(TypedDict):
    organization_id: NotRequired[
        Nullable[CustomerPortalSubscriptionsListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    product_id: NotRequired[
        Nullable[CustomerPortalSubscriptionsListQueryParamProductIDFilterTypedDict]
    ]
    r"""Filter by product ID."""
    active: NotRequired[Nullable[bool]]
    r"""Filter by active or cancelled subscription."""
    query: NotRequired[Nullable[str]]
    r"""Search by product or organization name."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[CustomerSubscriptionSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class CustomerPortalSubscriptionsListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[CustomerPortalSubscriptionsListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    product_id: Annotated[
        OptionalNullable[CustomerPortalSubscriptionsListQueryParamProductIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product ID."""

    active: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by active or cancelled subscription."""

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
        OptionalNullable[List[CustomerSubscriptionSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "organization_id",
            "product_id",
            "active",
            "query",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "organization_id",
            "product_id",
            "active",
            "query",
            "sorting",
        ]
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


class CustomerPortalSubscriptionsListResponseTypedDict(TypedDict):
    result: ListResourceCustomerSubscriptionTypedDict


class CustomerPortalSubscriptionsListResponse(BaseModel):
    next: Callable[[], Optional[CustomerPortalSubscriptionsListResponse]]

    result: ListResourceCustomerSubscription
