"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_refund_ import ListResourceRefund, ListResourceRefundTypedDict
from .refundsortproperty import RefundSortProperty
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


RefundIDFilterTypedDict = TypeAliasType(
    "RefundIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by refund ID."""


RefundIDFilter = TypeAliasType("RefundIDFilter", Union[str, List[str]])
r"""Filter by refund ID."""


RefundsListQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "RefundsListQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


RefundsListQueryParamOrganizationIDFilter = TypeAliasType(
    "RefundsListQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


OrderIDFilterTypedDict = TypeAliasType("OrderIDFilterTypedDict", Union[str, List[str]])
r"""Filter by order ID."""


OrderIDFilter = TypeAliasType("OrderIDFilter", Union[str, List[str]])
r"""Filter by order ID."""


SubscriptionIDFilterTypedDict = TypeAliasType(
    "SubscriptionIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by subscription ID."""


SubscriptionIDFilter = TypeAliasType("SubscriptionIDFilter", Union[str, List[str]])
r"""Filter by subscription ID."""


RefundsListQueryParamCustomerIDFilterTypedDict = TypeAliasType(
    "RefundsListQueryParamCustomerIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by customer ID."""


RefundsListQueryParamCustomerIDFilter = TypeAliasType(
    "RefundsListQueryParamCustomerIDFilter", Union[str, List[str]]
)
r"""Filter by customer ID."""


class RefundsListRequestTypedDict(TypedDict):
    id: NotRequired[Nullable[RefundIDFilterTypedDict]]
    r"""Filter by refund ID."""
    organization_id: NotRequired[
        Nullable[RefundsListQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    order_id: NotRequired[Nullable[OrderIDFilterTypedDict]]
    r"""Filter by order ID."""
    subscription_id: NotRequired[Nullable[SubscriptionIDFilterTypedDict]]
    r"""Filter by subscription ID."""
    customer_id: NotRequired[Nullable[RefundsListQueryParamCustomerIDFilterTypedDict]]
    r"""Filter by customer ID."""
    succeeded: NotRequired[Nullable[bool]]
    r"""Filter by `succeeded`."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    sorting: NotRequired[Nullable[List[RefundSortProperty]]]
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""


class RefundsListRequest(BaseModel):
    id: Annotated[
        OptionalNullable[RefundIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by refund ID."""

    organization_id: Annotated[
        OptionalNullable[RefundsListQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    order_id: Annotated[
        OptionalNullable[OrderIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by order ID."""

    subscription_id: Annotated[
        OptionalNullable[SubscriptionIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by subscription ID."""

    customer_id: Annotated[
        OptionalNullable[RefundsListQueryParamCustomerIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by customer ID."""

    succeeded: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by `succeeded`."""

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
        OptionalNullable[List[RefundSortProperty]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "organization_id",
            "order_id",
            "subscription_id",
            "customer_id",
            "succeeded",
            "page",
            "limit",
            "sorting",
        ]
        nullable_fields = [
            "id",
            "organization_id",
            "order_id",
            "subscription_id",
            "customer_id",
            "succeeded",
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


class RefundsListResponseTypedDict(TypedDict):
    result: ListResourceRefundTypedDict


class RefundsListResponse(BaseModel):
    next: Callable[[], Optional[RefundsListResponse]]

    result: ListResourceRefund
