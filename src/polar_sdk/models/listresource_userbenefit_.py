"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefitadssubscriber import BenefitAdsSubscriber, BenefitAdsSubscriberTypedDict
from .benefitarticlessubscriber import (
    BenefitArticlesSubscriber,
    BenefitArticlesSubscriberTypedDict,
)
from .benefitcustomsubscriber import (
    BenefitCustomSubscriber,
    BenefitCustomSubscriberTypedDict,
)
from .benefitdiscordsubscriber import (
    BenefitDiscordSubscriber,
    BenefitDiscordSubscriberTypedDict,
)
from .benefitdownloadablessubscriber import (
    BenefitDownloadablesSubscriber,
    BenefitDownloadablesSubscriberTypedDict,
)
from .benefitgithubrepositorysubscriber import (
    BenefitGitHubRepositorySubscriber,
    BenefitGitHubRepositorySubscriberTypedDict,
)
from .benefitlicensekeyssubscriber import (
    BenefitLicenseKeysSubscriber,
    BenefitLicenseKeysSubscriberTypedDict,
)
from .pagination import Pagination, PaginationTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import List, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


UserBenefitTypedDict = TypeAliasType(
    "UserBenefitTypedDict",
    Union[
        BenefitArticlesSubscriberTypedDict,
        BenefitAdsSubscriberTypedDict,
        BenefitDiscordSubscriberTypedDict,
        BenefitCustomSubscriberTypedDict,
        BenefitGitHubRepositorySubscriberTypedDict,
        BenefitDownloadablesSubscriberTypedDict,
        BenefitLicenseKeysSubscriberTypedDict,
    ],
)


UserBenefit = Annotated[
    Union[
        Annotated[BenefitAdsSubscriber, Tag("ads")],
        Annotated[BenefitArticlesSubscriber, Tag("articles")],
        Annotated[BenefitCustomSubscriber, Tag("custom")],
        Annotated[BenefitDiscordSubscriber, Tag("discord")],
        Annotated[BenefitDownloadablesSubscriber, Tag("downloadables")],
        Annotated[BenefitGitHubRepositorySubscriber, Tag("github_repository")],
        Annotated[BenefitLicenseKeysSubscriber, Tag("license_keys")],
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]


class ListResourceUserBenefitTypedDict(TypedDict):
    items: List[UserBenefitTypedDict]
    pagination: PaginationTypedDict


class ListResourceUserBenefit(BaseModel):
    items: List[UserBenefit]

    pagination: Pagination
