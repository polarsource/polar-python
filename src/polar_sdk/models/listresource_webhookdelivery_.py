"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .webhookdelivery import WebhookDelivery, WebhookDeliveryTypedDict
from polar_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListResourceWebhookDeliveryTypedDict(TypedDict):
    items: List[WebhookDeliveryTypedDict]
    pagination: PaginationTypedDict


class ListResourceWebhookDelivery(BaseModel):
    items: List[WebhookDelivery]

    pagination: Pagination
