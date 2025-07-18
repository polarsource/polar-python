"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productbillingtype import ProductBillingType
from .timeinterval import TimeInterval
from datetime import date
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


MetricsGetQueryParamOrganizationIDFilterTypedDict = TypeAliasType(
    "MetricsGetQueryParamOrganizationIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by organization ID."""


MetricsGetQueryParamOrganizationIDFilter = TypeAliasType(
    "MetricsGetQueryParamOrganizationIDFilter", Union[str, List[str]]
)
r"""Filter by organization ID."""


MetricsGetQueryParamProductIDFilterTypedDict = TypeAliasType(
    "MetricsGetQueryParamProductIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by product ID."""


MetricsGetQueryParamProductIDFilter = TypeAliasType(
    "MetricsGetQueryParamProductIDFilter", Union[str, List[str]]
)
r"""Filter by product ID."""


QueryParamProductBillingTypeFilterTypedDict = TypeAliasType(
    "QueryParamProductBillingTypeFilterTypedDict",
    Union[ProductBillingType, List[ProductBillingType]],
)
r"""Filter by billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""


QueryParamProductBillingTypeFilter = TypeAliasType(
    "QueryParamProductBillingTypeFilter",
    Union[ProductBillingType, List[ProductBillingType]],
)
r"""Filter by billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""


MetricsGetQueryParamCustomerIDFilterTypedDict = TypeAliasType(
    "MetricsGetQueryParamCustomerIDFilterTypedDict", Union[str, List[str]]
)
r"""Filter by customer ID."""


MetricsGetQueryParamCustomerIDFilter = TypeAliasType(
    "MetricsGetQueryParamCustomerIDFilter", Union[str, List[str]]
)
r"""Filter by customer ID."""


class MetricsGetRequestTypedDict(TypedDict):
    start_date: date
    r"""Start date."""
    end_date: date
    r"""End date."""
    interval: TimeInterval
    r"""Interval between two timestamps."""
    timezone: NotRequired[str]
    r"""Timezone to use for the timestamps. Default is UTC."""
    organization_id: NotRequired[
        Nullable[MetricsGetQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    product_id: NotRequired[Nullable[MetricsGetQueryParamProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    billing_type: NotRequired[Nullable[QueryParamProductBillingTypeFilterTypedDict]]
    r"""Filter by billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""
    customer_id: NotRequired[Nullable[MetricsGetQueryParamCustomerIDFilterTypedDict]]
    r"""Filter by customer ID."""


class MetricsGetRequest(BaseModel):
    start_date: Annotated[
        date, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Start date."""

    end_date: Annotated[
        date, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""End date."""

    interval: Annotated[
        TimeInterval,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Interval between two timestamps."""

    timezone: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "UTC"
    r"""Timezone to use for the timestamps. Default is UTC."""

    organization_id: Annotated[
        OptionalNullable[MetricsGetQueryParamOrganizationIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by organization ID."""

    product_id: Annotated[
        OptionalNullable[MetricsGetQueryParamProductIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product ID."""

    billing_type: Annotated[
        OptionalNullable[QueryParamProductBillingTypeFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""

    customer_id: Annotated[
        OptionalNullable[MetricsGetQueryParamCustomerIDFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by customer ID."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "timezone",
            "organization_id",
            "product_id",
            "billing_type",
            "customer_id",
        ]
        nullable_fields = [
            "organization_id",
            "product_id",
            "billing_type",
            "customer_id",
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
