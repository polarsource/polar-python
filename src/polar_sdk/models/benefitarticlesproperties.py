"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import TypedDict


class BenefitArticlesPropertiesTypedDict(TypedDict):
    r"""Properties for a benefit of type `articles`."""

    paid_articles: bool
    r"""Whether the user can access paid articles."""


class BenefitArticlesProperties(BaseModel):
    r"""Properties for a benefit of type `articles`."""

    paid_articles: bool
    r"""Whether the user can access paid articles."""
