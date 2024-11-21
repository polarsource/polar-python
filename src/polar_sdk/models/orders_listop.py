"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_order_ import ListResourceOrder, ListResourceOrderTypedDict
from .ordersortproperty import OrderSortProperty
from .productpricetype import ProductPriceType
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


OrdersListQueryParamOrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


OrdersListQueryParamOrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


OrdersListQueryParamProductIDFilterTypedDict = Union[str, List[str]]
r"""Filter by product ID."""


OrdersListQueryParamProductIDFilter = Union[str, List[str]]
r"""Filter by product ID."""


QueryParamProductPriceTypeFilterTypedDict = Union[
    ProductPriceType, List[ProductPriceType]
]
r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""


QueryParamProductPriceTypeFilter = Union[ProductPriceType, List[ProductPriceType]]
r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""


QueryParamDiscountIDFilterTypedDict = Union[str, List[str]]
r"""Filter by discount ID."""


QueryParamDiscountIDFilter = Union[str, List[str]]
r"""Filter by discount ID."""


UserIDFilterTypedDict = Union[str, List[str]]
r"""Filter by customer's user ID."""


UserIDFilter = Union[str, List[str]]
r"""Filter by customer's user ID."""


class OrdersListRequestTypedDict(TypedDict):
    organization_id: NotRequired[
        Nullable[OrdersListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    product_id: NotRequired[Nullable[OrdersListQueryParamProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    product_price_type: NotRequired[Nullable[QueryParamProductPriceTypeFilterTypedDict]]
    r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""
    discount_id: NotRequired[Nullable[QueryParamDiscountIDFilterTypedDict]]
    r"""Filter by discount ID."""
    user_id: NotRequired[Nullable[UserIDFilterTypedDict]]
    r"""Filter by customer's user ID."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[OrderSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class OrdersListRequest(BaseModel):
    organization_id: Annotated[
        OptionalNullable[OrdersListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    product_id: Annotated[
        OptionalNullable[OrdersListQueryParamProductIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product ID."""

    product_price_type: Annotated[
        OptionalNullable[QueryParamProductPriceTypeFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases."""

    discount_id: Annotated[
        OptionalNullable[QueryParamDiscountIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by discount ID."""

    user_id: Annotated[
        OptionalNullable[UserIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by customer's user ID."""

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
        OptionalNullable[List[OrderSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "organization_id",
            "product_id",
            "product_price_type",
            "discount_id",
            "user_id",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "organization_id",
            "product_id",
            "product_price_type",
            "discount_id",
            "user_id",
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


class OrdersListResponseTypedDict(TypedDict):
    result: ListResourceOrderTypedDict


class OrdersListResponse(BaseModel):
    next: Callable[[], Optional[OrdersListResponse]]

    result: ListResourceOrder
