"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from polar_sdk import utils
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated


class FileNotFoundType(str, Enum):
    FILE_NOT_FOUND = "FileNotFound"


class FileNotFoundData(BaseModel):
    detail: str

    TYPE: Annotated[
        Annotated[
            FileNotFoundType,
            AfterValidator(validate_const(FileNotFoundType.FILE_NOT_FOUND)),
        ],
        pydantic.Field(alias="type"),
    ] = FileNotFoundType.FILE_NOT_FOUND


class FileNotFound(Exception):
    data: FileNotFoundData

    def __init__(self, data: FileNotFoundData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, FileNotFoundData)
