"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhookevent import WebhookEvent, WebhookEventTypedDict
from datetime import datetime
from polar_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class WebhookDeliveryTypedDict(TypedDict):
    r"""A webhook delivery for a webhook event."""

    created_at: datetime
    r"""Creation timestamp of the object."""
    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""
    id: str
    r"""The ID of the object."""
    succeeded: bool
    r"""Whether the delivery was successful."""
    webhook_event: WebhookEventTypedDict
    r"""A webhook event.

    An event represent something that happened in the system
    that should be sent to the webhook endpoint.

    It can be delivered multiple times until it's marked as succeeded,
    each one creating a new delivery.
    """
    http_code: NotRequired[Nullable[int]]
    r"""The HTTP code returned by the URL. `null` if the endpoint was unreachable."""


class WebhookDelivery(BaseModel):
    r"""A webhook delivery for a webhook event."""

    created_at: datetime
    r"""Creation timestamp of the object."""

    modified_at: Nullable[datetime]
    r"""Last modification timestamp of the object."""

    id: str
    r"""The ID of the object."""

    succeeded: bool
    r"""Whether the delivery was successful."""

    webhook_event: WebhookEvent
    r"""A webhook event.

    An event represent something that happened in the system
    that should be sent to the webhook endpoint.

    It can be delivered multiple times until it's marked as succeeded,
    each one creating a new delivery.
    """

    http_code: OptionalNullable[int] = UNSET
    r"""The HTTP code returned by the URL. `null` if the endpoint was unreachable."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["http_code"]
        nullable_fields = ["modified_at", "http_code"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
