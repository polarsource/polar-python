"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .articleupdate import ArticleUpdate, ArticleUpdateTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class ArticlesUpdateRequestTypedDict(TypedDict):
    id: str
    article_update: ArticleUpdateTypedDict
    

class ArticlesUpdateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    article_update: Annotated[ArticleUpdate, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    