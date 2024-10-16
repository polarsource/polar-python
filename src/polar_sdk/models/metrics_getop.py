"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .interval import Interval
from .productpricetype import ProductPriceType
from datetime import date
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sdk.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import List, Union
from typing_extensions import Annotated, NotRequired, TypedDict


MetricsGetQueryParamOrganizationIDFilterTypedDict = Union[str, List[str]]
r"""Filter by organization ID."""


MetricsGetQueryParamOrganizationIDFilter = Union[str, List[str]]
r"""Filter by organization ID."""


MetricsGetQueryParamProductIDFilterTypedDict = Union[str, List[str]]
r"""Filter by product ID."""


MetricsGetQueryParamProductIDFilter = Union[str, List[str]]
r"""Filter by product ID."""


MetricsGetQueryParamProductPriceTypeFilterTypedDict = Union[
    ProductPriceType, List[ProductPriceType]
]
r"""Filter by product price type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""


MetricsGetQueryParamProductPriceTypeFilter = Union[
    ProductPriceType, List[ProductPriceType]
]
r"""Filter by product price type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""


class MetricsGetRequestTypedDict(TypedDict):
    start_date: date
    r"""Start date."""
    end_date: date
    r"""End date."""
    interval: Interval
    r"""Interval between two timestamps."""
    organization_id: NotRequired[
        Nullable[MetricsGetQueryParamOrganizationIDFilterTypedDict]
    ]
    r"""Filter by organization ID."""
    product_id: NotRequired[Nullable[MetricsGetQueryParamProductIDFilterTypedDict]]
    r"""Filter by product ID."""
    product_price_type: NotRequired[
        Nullable[MetricsGetQueryParamProductPriceTypeFilterTypedDict]
    ]
    r"""Filter by product price type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""


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
        Interval, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Interval between two timestamps."""

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

    product_price_type: Annotated[
        OptionalNullable[MetricsGetQueryParamProductPriceTypeFilter],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Filter by product price type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "product_id", "product_price_type"]
        nullable_fields = ["organization_id", "product_id", "product_price_type"]
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
