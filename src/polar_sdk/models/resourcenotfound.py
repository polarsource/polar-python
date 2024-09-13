"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk import utils
from polar_sdk.types import BaseModel
import pydantic
from typing import Final
from typing_extensions import Annotated


class ResourceNotFoundType(str, Enum):
    RESOURCE_NOT_FOUND = "ResourceNotFound"


class ResourceNotFoundData(BaseModel):
    detail: str

    # fmt: off
    TYPE: Annotated[Final[ResourceNotFoundType], pydantic.Field(alias="type")] = ResourceNotFoundType.RESOURCE_NOT_FOUND # type: ignore
    # fmt: on


class ResourceNotFound(Exception):
    r"""Order not found."""

    data: ResourceNotFoundData

    def __init__(self, data: ResourceNotFoundData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ResourceNotFoundData)
