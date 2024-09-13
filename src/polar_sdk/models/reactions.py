"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import TypedDict


class ReactionsTypedDict(TypedDict):
    total_count: int
    plus_one: int
    minus_one: int
    laugh: int
    hooray: int
    confused: int
    heart: int
    rocket: int
    eyes: int


class Reactions(BaseModel):
    total_count: int

    plus_one: int

    minus_one: int

    laugh: int

    hooray: int

    confused: int

    heart: int

    rocket: int

    eyes: int
