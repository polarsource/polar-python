"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .discountsortproperty import DiscountSortProperty
from .listresource_discount_ import ListResourceDiscount, ListResourceDiscountTypedDict
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


DiscountsListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "DiscountsListQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


DiscountsListQueryParamOrganizationIDFilter = TypeAliasType(
    "DiscountsListQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


class DiscountsListRequestTypedDict(TypedDict):
    organization_id: NotRequired[
        Nullable[DiscountsListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    query: NotRequired[Nullable[str]]
    r"""Filter by name."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[DiscountSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class DiscountsListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[DiscountsListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    query: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by name."""

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
        OptionalNullable[List[DiscountSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "query", "page", "limit", "sorting"]
        nullable_fields = ["organization_id", "query", "sorting"]
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


class DiscountsListResponseTypedDict(TypedDict):
    result: ListResourceDiscountTypedDict


class DiscountsListResponse(BaseModel):
    next: Callable[[], Optional[DiscountsListResponse]]

    result: ListResourceDiscount