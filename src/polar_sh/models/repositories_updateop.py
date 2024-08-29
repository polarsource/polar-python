"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .repositoryupdate import RepositoryUpdate, RepositoryUpdateTypedDict
from polar_sh.types import BaseModel
from polar_sh.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class RepositoriesUpdateRequestTypedDict(TypedDict):
    id: str
    repository_update: RepositoryUpdateTypedDict
    

class RepositoriesUpdateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    repository_update: Annotated[RepositoryUpdate, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
