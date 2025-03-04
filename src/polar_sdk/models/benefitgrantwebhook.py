"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .benefit import Benefit, BenefitTypedDict
from .benefitgrantcustomproperties import (
    BenefitGrantCustomProperties,
    BenefitGrantCustomPropertiesTypedDict,
)
from .benefitgrantdiscordproperties import (
    BenefitGrantDiscordProperties,
    BenefitGrantDiscordPropertiesTypedDict,
)
from .benefitgrantdownloadablesproperties import (
    BenefitGrantDownloadablesProperties,
    BenefitGrantDownloadablesPropertiesTypedDict,
)
from .benefitgrantgithubrepositoryproperties import (
    BenefitGrantGitHubRepositoryProperties,
    BenefitGrantGitHubRepositoryPropertiesTypedDict,
)
from .benefitgrantlicensekeysproperties import (
    BenefitGrantLicenseKeysProperties,
    BenefitGrantLicenseKeysPropertiesTypedDict,
)
from .customer import Customer, CustomerTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


BenefitGrantWebhookPropertiesTypedDict = TypeAliasType(
    "BenefitGrantWebhookPropertiesTypedDict",
    Union[
        BenefitGrantCustomPropertiesTypedDict,
        BenefitGrantDownloadablesPropertiesTypedDict,
        BenefitGrantLicenseKeysPropertiesTypedDict,
        BenefitGrantDiscordPropertiesTypedDict,
        BenefitGrantGitHubRepositoryPropertiesTypedDict,
    ],
)


BenefitGrantWebhookProperties = TypeAliasType(
    "BenefitGrantWebhookProperties",
    Union[
        BenefitGrantCustomProperties,
        BenefitGrantDownloadablesProperties,
        BenefitGrantLicenseKeysProperties,
        BenefitGrantDiscordProperties,
        BenefitGrantGitHubRepositoryProperties,
    ],
)


PreviousPropertiesTypedDict = TypeAliasType(
    "PreviousPropertiesTypedDict",
    Union[
        BenefitGrantCustomPropertiesTypedDict,
        BenefitGrantDownloadablesPropertiesTypedDict,
        BenefitGrantLicenseKeysPropertiesTypedDict,
        BenefitGrantDiscordPropertiesTypedDict,
        BenefitGrantGitHubRepositoryPropertiesTypedDict,
    ],
)


PreviousProperties = TypeAliasType(
    "PreviousProperties",
    Union[
        BenefitGrantCustomProperties,
        BenefitGrantDownloadablesProperties,
        BenefitGrantLicenseKeysProperties,
        BenefitGrantDiscordProperties,
        BenefitGrantGitHubRepositoryProperties,
    ],
)


class BenefitGrantWebhookTypedDict(TypedDict):
    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the grant."""
    is_granted: bool
    r"""Whether the benefit is granted."""
    is_revoked: bool
    r"""Whether the benefit is revoked."""
    subscription_id: Nullable[str]
    r"""The ID of the subscription that granted this benefit."""
    order_id: Nullable[str]
    r"""The ID of the order that granted this benefit."""
    customer_id: str
    r"""The ID of the customer concerned by this grant."""
    user_id: str
    benefit_id: str
    r"""The ID of the benefit concerned by this grant."""
    customer: CustomerTypedDict
    r"""A customer in an organization."""
    properties: BenefitGrantWebhookPropertiesTypedDict
    benefit: BenefitTypedDict
    granted_at: NotRequired[Nullable[datetime]]
    r"""The timestamp when the benefit was granted. If `None`, the benefit is not granted."""
    revoked_at: NotRequired[Nullable[datetime]]
    r"""The timestamp when the benefit was revoked. If `None`, the benefit is not revoked."""
    previous_properties: NotRequired[Nullable[PreviousPropertiesTypedDict]]


class BenefitGrantWebhook(BaseModel):
    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the grant."""

    is_granted: bool
    r"""Whether the benefit is granted."""

    is_revoked: bool
    r"""Whether the benefit is revoked."""

    subscription_id: Nullable[str]
    r"""The ID of the subscription that granted this benefit."""

    order_id: Nullable[str]
    r"""The ID of the order that granted this benefit."""

    customer_id: str
    r"""The ID of the customer concerned by this grant."""

    user_id: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    benefit_id: str
    r"""The ID of the benefit concerned by this grant."""

    customer: Customer
    r"""A customer in an organization."""

    properties: BenefitGrantWebhookProperties

    benefit: Benefit

    granted_at: OptionalNullable[datetime] = UNSET
    r"""The timestamp when the benefit was granted. If `None`, the benefit is not granted."""

    revoked_at: OptionalNullable[datetime] = UNSET
    r"""The timestamp when the benefit was revoked. If `None`, the benefit is not revoked."""

    previous_properties: OptionalNullable[PreviousProperties] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["granted_at", "revoked_at", "previous_properties"]
        nullable_fields = [
            "modified_at",
            "subscription_id",
            "order_id",
            "granted_at",
            "revoked_at",
            "previous_properties",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
