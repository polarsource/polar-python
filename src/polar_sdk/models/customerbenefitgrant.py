"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customerbenefitgrantads import (
    CustomerBenefitGrantAds,
    CustomerBenefitGrantAdsTypedDict,
)
from .customerbenefitgrantcustom import (
    CustomerBenefitGrantCustom,
    CustomerBenefitGrantCustomTypedDict,
)
from .customerbenefitgrantdiscord import (
    CustomerBenefitGrantDiscord,
    CustomerBenefitGrantDiscordTypedDict,
)
from .customerbenefitgrantdownloadables import (
    CustomerBenefitGrantDownloadables,
    CustomerBenefitGrantDownloadablesTypedDict,
)
from .customerbenefitgrantgithubrepository import (
    CustomerBenefitGrantGitHubRepository,
    CustomerBenefitGrantGitHubRepositoryTypedDict,
)
from .customerbenefitgrantlicensekeys import (
    CustomerBenefitGrantLicenseKeys,
    CustomerBenefitGrantLicenseKeysTypedDict,
)
from typing import Union
from typing_extensions import TypeAliasType


CustomerBenefitGrantTypedDict = TypeAliasType(
    "CustomerBenefitGrantTypedDict",
    Union[
        CustomerBenefitGrantDiscordTypedDict,
        CustomerBenefitGrantGitHubRepositoryTypedDict,
        CustomerBenefitGrantDownloadablesTypedDict,
        CustomerBenefitGrantLicenseKeysTypedDict,
        CustomerBenefitGrantAdsTypedDict,
        CustomerBenefitGrantCustomTypedDict,
    ],
)


CustomerBenefitGrant = TypeAliasType(
    "CustomerBenefitGrant",
    Union[
        CustomerBenefitGrantDiscord,
        CustomerBenefitGrantGitHubRepository,
        CustomerBenefitGrantDownloadables,
        CustomerBenefitGrantLicenseKeys,
        CustomerBenefitGrantAds,
        CustomerBenefitGrantCustom,
    ],
)
