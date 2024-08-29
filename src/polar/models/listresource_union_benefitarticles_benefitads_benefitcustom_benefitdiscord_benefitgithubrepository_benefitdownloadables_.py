"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitads import BenefitAds, BenefitAdsTypedDict
from .benefitarticles import BenefitArticles, BenefitArticlesTypedDict
from .benefitcustom import BenefitCustom, BenefitCustomTypedDict
from .benefitdiscord_output import BenefitDiscordOutput, BenefitDiscordOutputTypedDict
from .benefitdownloadables import BenefitDownloadables, BenefitDownloadablesTypedDict
from .benefitgithubrepository import BenefitGitHubRepository, BenefitGitHubRepositoryTypedDict
from .pagination import Pagination, PaginationTypedDict
from polar.types import BaseModel
from typing import List, Optional, TypedDict, Union
from typing_extensions import NotRequired


ItemsTypedDict = Union[BenefitArticlesTypedDict, BenefitAdsTypedDict, BenefitDiscordOutputTypedDict, BenefitGitHubRepositoryTypedDict, BenefitDownloadablesTypedDict, BenefitCustomTypedDict]


Items = Union[BenefitArticles, BenefitAds, BenefitDiscordOutput, BenefitGitHubRepository, BenefitDownloadables, BenefitCustom]


class ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadablesTypedDict(TypedDict):
    pagination: PaginationTypedDict
    items: NotRequired[List[ItemsTypedDict]]
    

class ListResourceUnionBenefitArticlesBenefitAdsBenefitCustomBenefitDiscordBenefitGitHubRepositoryBenefitDownloadables(BaseModel):
    pagination: Pagination
    items: Optional[List[Items]] = None
    