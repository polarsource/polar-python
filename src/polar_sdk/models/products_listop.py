"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_product_ import ListResourceProduct, ListResourceProductTypedDict
from .productsortproperty import ProductSortProperty
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


QueryParamProductIDFilterTypedDict = TypeAliasType(
    "QueryParamProductIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by product ID."""


QueryParamProductIDFilter = TypeAliasType(
    "QueryParamProductIDFilter", Union[str, List[str]]
)
r"""Filter by product ID."""


ProductsListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "ProductsListQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


ProductsListQueryParamOrganizationIDFilter = TypeAliasType(
    "ProductsListQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


BenefitIDFilterTypedDict = TypeAliasType(
    "BenefitIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter products granting specific benefit."""


BenefitIDFilter = TypeAliasType("BenefitIDFilter", Union[str, List[str]])
r"""Filter products granting specific benefit."""


class ProductsListRequestTypedDict(TypedDict):
    id: NotRequired[Nullable[QueryParamProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    organization_id: NotRequired[
        Nullable[ProductsListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    query: NotRequired[Nullable[str]]
    r"""Filter by product name."""
    is_archived: NotRequired[Nullable[bool]]
    r"""Filter on archived products."""
    is_recurring: NotRequired[Nullable[bool]]
    r"""Filter on recurring products. If `true`, only subscriptions tiers are returned. If `false`, only one-time purchase products are returned."""
    benefit_id: NotRequired[Nullable[BenefitIDFilterTypedDict]]
    r"""Filter products granting specific benefit."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[ProductSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class ProductsListRequest(BaseModel):
    id: Annotated[
        OptionalNullable[QueryParamProductIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product ID."""

    organization_id: Annotated[
        OptionalNullable[ProductsListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    query: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product name."""

    is_archived: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter on archived products."""

    is_recurring: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter on recurring products. If `true`, only subscriptions tiers are returned. If `false`, only one-time purchase products are returned."""

    benefit_id: Annotated[
        OptionalNullable[BenefitIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter products granting specific benefit."""

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
        OptionalNullable[List[ProductSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "organization_id",
            "query",
            "is_archived",
            "is_recurring",
            "benefit_id",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "id",
            "organization_id",
            "query",
            "is_archived",
            "is_recurring",
            "benefit_id",
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


class ProductsListResponseTypedDict(TypedDict):
    result: ListResourceProductTypedDict


class ProductsListResponse(BaseModel):
    next: Callable[[], Optional[ProductsListResponse]]

    result: ListResourceProduct
