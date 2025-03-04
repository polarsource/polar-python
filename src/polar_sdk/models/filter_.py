"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filterclause import FilterClause, FilterClauseTypedDict
from .filterconjunction import FilterConjunction
from polar_sdk.types import BaseModel
from typing import List, Union
from typing_extensions import TypeAliasType, TypedDict


class FilterTypedDict(TypedDict):
    conjunction: FilterConjunction
    clauses: List[ClausesTypedDict]


class Filter(BaseModel):
    conjunction: FilterConjunction

    clauses: List[Clauses]


ClausesTypedDict = TypeAliasType(
    "ClausesTypedDict", Union["FilterTypedDict", FilterClauseTypedDict]
)


Clauses = TypeAliasType("Clauses", Union["Filter", FilterClause])
