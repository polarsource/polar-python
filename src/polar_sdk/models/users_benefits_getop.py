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
from polar_sdk.types import BaseModel
from polar_sdk.utils import FieldMetadata, PathParamMetadata, get_discriminator
from pydantic import Discriminator, Tag
from typing import TypedDict, Union
from typing_extensions import Annotated


class UsersBenefitsGetRequestTypedDict(TypedDict):
    id: str
    r"""The benefit ID."""


class UsersBenefitsGetRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The benefit ID."""


UsersBenefitsGetResponseUsersBenefitsGetTypedDict = Union[
    BenefitArticlesSubscriberTypedDict,
    BenefitDiscordSubscriberTypedDict,
    BenefitGitHubRepositorySubscriberTypedDict,
    BenefitDownloadablesSubscriberTypedDict,
    BenefitAdsSubscriberTypedDict,
    BenefitCustomSubscriberTypedDict,
    BenefitLicenseKeysSubscriberTypedDict,
]
r"""Successful Response"""


UsersBenefitsGetResponseUsersBenefitsGet = Annotated[
    Union[
        Annotated[BenefitArticlesSubscriber, Tag("articles")],
        Annotated[BenefitAdsSubscriber, Tag("ads")],
        Annotated[BenefitDiscordSubscriber, Tag("discord")],
        Annotated[BenefitCustomSubscriber, Tag("custom")],
        Annotated[BenefitGitHubRepositorySubscriber, Tag("github_repository")],
        Annotated[BenefitDownloadablesSubscriber, Tag("downloadables")],
        Annotated[BenefitLicenseKeysSubscriber, Tag("license_keys")],
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]
r"""Successful Response"""
