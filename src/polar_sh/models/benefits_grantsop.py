"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_benefitgrant_ import ListResourceBenefitGrant, ListResourceBenefitGrantTypedDict
from polar_sh.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar_sh.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BenefitsGrantsRequestTypedDict(TypedDict):
    id: str
    is_granted: NotRequired[Nullable[bool]]
    r"""Filter by granted status. If `true`, only granted benefits will be returned. If `false`, only revoked benefits will be returned."""
    user_id: NotRequired[Nullable[str]]
    r"""Filter by user ID."""
    github_user_id: NotRequired[Nullable[int]]
    r"""Filter by GitHub user ID. Only available for users who have linked their GitHub account on Polar."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    

class BenefitsGrantsRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    is_granted: Annotated[OptionalNullable[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by granted status. If `true`, only granted benefits will be returned. If `false`, only revoked benefits will be returned."""
    user_id: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by user ID."""
    github_user_id: Annotated[OptionalNullable[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""Filter by GitHub user ID. Only available for users who have linked their GitHub account on Polar."""
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""Page number, defaults to 1."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["is_granted", "user_id", "github_user_id", "page", "limit"]
        nullable_fields = ["is_granted", "user_id", "github_user_id"]
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
        

class BenefitsGrantsResponseTypedDict(TypedDict):
    result: ListResourceBenefitGrantTypedDict
    

class BenefitsGrantsResponse(BaseModel):
    next: Callable[[], Optional[BenefitsGrantsResponse]]
    
    result: ListResourceBenefitGrant
    
