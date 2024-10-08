"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitads import BenefitAds, BenefitAdsTypedDict
from .benefitarticles import BenefitArticles, BenefitArticlesTypedDict
from .benefitcustom import BenefitCustom, BenefitCustomTypedDict
from .benefitdiscord import BenefitDiscord, BenefitDiscordTypedDict
from .benefitdownloadables import BenefitDownloadables, BenefitDownloadablesTypedDict
from .benefitgithubrepository import (
    BenefitGitHubRepository,
    BenefitGitHubRepositoryTypedDict,
)
from .benefitlicensekeys import BenefitLicenseKeys, BenefitLicenseKeysTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypedDict


class BenefitsGetRequestTypedDict(TypedDict):
    id: str


class BenefitsGetRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


BenefitsGetResponseBenefitsGetTypedDict = Union[
    BenefitArticlesTypedDict,
    BenefitAdsTypedDict,
    BenefitDiscordTypedDict,
    BenefitGitHubRepositoryTypedDict,
    BenefitDownloadablesTypedDict,
    BenefitLicenseKeysTypedDict,
    BenefitCustomTypedDict,
]
r"""Successful Response"""


BenefitsGetResponseBenefitsGet = Union[
    BenefitArticles,
    BenefitAds,
    BenefitDiscord,
    BenefitGitHubRepository,
    BenefitDownloadables,
    BenefitLicenseKeys,
    BenefitCustom,
]
r"""Successful Response"""
