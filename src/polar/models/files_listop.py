"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listresource_annotated_union_downloadablefileread_productmediafileread_organizationavatarfileread_discriminator_mergejsonschema_ import ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchema, ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchemaTypedDict
from polar.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from polar.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Callable, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class FilesListRequestTypedDict(TypedDict):
    organization_id: NotRequired[Nullable[str]]
    ids: NotRequired[Nullable[List[str]]]
    r"""List of file IDs to get."""
    page: NotRequired[int]
    r"""Page number, defaults to 1."""
    limit: NotRequired[int]
    r"""Size of a page, defaults to 10. Maximum is 100."""
    

class FilesListRequest(BaseModel):
    organization_id: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    ids: Annotated[OptionalNullable[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""List of file IDs to get."""
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""Page number, defaults to 1."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Size of a page, defaults to 10. Maximum is 100."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["organization_id", "ids", "page", "limit"]
        nullable_fields = ["organization_id", "ids"]
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
        

class FilesListResponseTypedDict(TypedDict):
    result: ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchemaTypedDict
    

class FilesListResponse(BaseModel):
    next: Callable[[], Optional[FilesListResponse]]
    
    result: ListResourceAnnotatedUnionDownloadableFileReadProductMediaFileReadOrganizationAvatarFileReadDiscriminatorMergeJSONSchema
    