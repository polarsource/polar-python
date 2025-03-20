"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .order import Order, OrderTypedDict
from polar_sdk.types import BaseModel
from polar_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WebhookOrderCreatedPayloadTypedDict(TypedDict):
    r"""Sent when a new order is created.

    A new order is created when:

    * A customer purchases a one-time product. In this case, `billing_reason` is set to `purchase`.
    * A customer starts a subscription. In this case, `billing_reason` is set to `subscription_create`.
    * A subscription is renewed. In this case, `billing_reason` is set to `subscription_cycle`.
    * A subscription is upgraded or downgraded with an immediate proration invoice. In this case, `billing_reason` is set to `subscription_update`.

    <Warning>The order might not be paid yet, so the `status` field might be `pending`.</Warning>

    **Discord & Slack support:** Full
    """

    data: OrderTypedDict
    type: Literal["order.created"]


class WebhookOrderCreatedPayload(BaseModel):
    r"""Sent when a new order is created.

    A new order is created when:

    * A customer purchases a one-time product. In this case, `billing_reason` is set to `purchase`.
    * A customer starts a subscription. In this case, `billing_reason` is set to `subscription_create`.
    * A subscription is renewed. In this case, `billing_reason` is set to `subscription_cycle`.
    * A subscription is upgraded or downgraded with an immediate proration invoice. In this case, `billing_reason` is set to `subscription_update`.

    <Warning>The order might not be paid yet, so the `status` field might be `pending`.</Warning>

    **Discord & Slack support:** Full
    """

    data: Order

    TYPE: Annotated[
        Annotated[
            Literal["order.created"], AfterValidator(validate_const("order.created"))
        ],
        pydantic.Field(alias="type"),
    ] = "order.created"
