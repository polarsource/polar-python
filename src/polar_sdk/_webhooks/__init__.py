import base64
from typing import Annotated, Any, Union

from pydantic import Discriminator, Tag, TypeAdapter
from standardwebhooks.webhooks import Webhook
from standardwebhooks.webhooks import (
    WebhookVerificationError as _WebhookVerificationError,
)

from polar_sdk.models import (
    WebhookBenefitCreatedPayload,
    WebhookBenefitGrantCreatedPayload,
    WebhookBenefitGrantCycledPayload,
    WebhookBenefitGrantRevokedPayload,
    WebhookBenefitGrantUpdatedPayload,
    WebhookBenefitUpdatedPayload,
    WebhookCheckoutCreatedPayload,
    WebhookCheckoutExpiredPayload,
    WebhookCheckoutUpdatedPayload,
    WebhookCustomerCreatedPayload,
    WebhookCustomerDeletedPayload,
    WebhookCustomerSeatAssignedPayload,
    WebhookCustomerSeatClaimedPayload,
    WebhookCustomerSeatRevokedPayload,
    WebhookCustomerStateChangedPayload,
    WebhookCustomerUpdatedPayload,
    WebhookEventType,
    WebhookMemberCreatedPayload,
    WebhookMemberDeletedPayload,
    WebhookMemberUpdatedPayload,
    WebhookOrderCreatedPayload,
    WebhookOrderPaidPayload,
    WebhookOrderRefundedPayload,
    WebhookOrderUpdatedPayload,
    WebhookOrganizationUpdatedPayload,
    WebhookProductCreatedPayload,
    WebhookProductUpdatedPayload,
    WebhookRefundCreatedPayload,
    WebhookRefundUpdatedPayload,
    WebhookSubscriptionActivePayload,
    WebhookSubscriptionCanceledPayload,
    WebhookSubscriptionCreatedPayload,
    WebhookSubscriptionPastDuePayload,
    WebhookSubscriptionRevokedPayload,
    WebhookSubscriptionUncanceledPayload,
    WebhookSubscriptionUpdatedPayload,
)


def _get_discriminator(v: Any) -> Union[str, None]:
    if isinstance(v, dict):
        return v.get("type")
    return getattr(v, "type", None)


WebhoookPayload = Annotated[
    Union[
        Annotated[WebhookCheckoutCreatedPayload, Tag("checkout.created")],
        Annotated[WebhookCheckoutUpdatedPayload, Tag("checkout.updated")],
        Annotated[WebhookCheckoutExpiredPayload, Tag("checkout.expired")],
        Annotated[WebhookCustomerCreatedPayload, Tag("customer.created")],
        Annotated[WebhookCustomerUpdatedPayload, Tag("customer.updated")],
        Annotated[WebhookCustomerDeletedPayload, Tag("customer.deleted")],
        Annotated[WebhookCustomerStateChangedPayload, Tag("customer.state_changed")],
        Annotated[WebhookCustomerSeatAssignedPayload, Tag("customer_seat.assigned")],
        Annotated[WebhookCustomerSeatClaimedPayload, Tag("customer_seat.claimed")],
        Annotated[WebhookCustomerSeatRevokedPayload, Tag("customer_seat.revoked")],
        Annotated[WebhookMemberCreatedPayload, Tag("member.created")],
        Annotated[WebhookMemberUpdatedPayload, Tag("member.updated")],
        Annotated[WebhookMemberDeletedPayload, Tag("member.deleted")],
        Annotated[WebhookOrderCreatedPayload, Tag("order.created")],
        Annotated[WebhookOrderUpdatedPayload, Tag("order.updated")],
        Annotated[WebhookOrderPaidPayload, Tag("order.paid")],
        Annotated[WebhookOrderRefundedPayload, Tag("order.refunded")],
        Annotated[WebhookSubscriptionCreatedPayload, Tag("subscription.created")],
        Annotated[WebhookSubscriptionUpdatedPayload, Tag("subscription.updated")],
        Annotated[WebhookSubscriptionActivePayload, Tag("subscription.active")],
        Annotated[WebhookSubscriptionCanceledPayload, Tag("subscription.canceled")],
        Annotated[WebhookSubscriptionUncanceledPayload, Tag("subscription.uncanceled")],
        Annotated[WebhookSubscriptionRevokedPayload, Tag("subscription.revoked")],
        Annotated[WebhookSubscriptionPastDuePayload, Tag("subscription.past_due")],
        Annotated[WebhookRefundCreatedPayload, Tag("refund.created")],
        Annotated[WebhookRefundUpdatedPayload, Tag("refund.updated")],
        Annotated[WebhookProductCreatedPayload, Tag("product.created")],
        Annotated[WebhookProductUpdatedPayload, Tag("product.updated")],
        Annotated[WebhookBenefitCreatedPayload, Tag("benefit.created")],
        Annotated[WebhookBenefitUpdatedPayload, Tag("benefit.updated")],
        Annotated[WebhookBenefitGrantCreatedPayload, Tag("benefit_grant.created")],
        Annotated[WebhookBenefitGrantCycledPayload, Tag("benefit_grant.cycled")],
        Annotated[WebhookBenefitGrantUpdatedPayload, Tag("benefit_grant.updated")],
        Annotated[WebhookBenefitGrantRevokedPayload, Tag("benefit_grant.revoked")],
        Annotated[WebhookOrganizationUpdatedPayload, Tag("organization.updated")],
    ],
    Discriminator(_get_discriminator),
]


_KNOWN_EVENT_TYPES: frozenset[str] = frozenset(t.value for t in WebhookEventType)


WebhookPayloadAdapter: TypeAdapter[WebhoookPayload] = TypeAdapter(WebhoookPayload)


class WebhookVerificationError(_WebhookVerificationError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class WebhookUnknownTypeError(Exception):
    """Webhook signature was valid, but the event type isn't known to this
    SDK version. Callers may safely ignore (e.g. for forward compatibility)."""

    def __init__(self, event_type: Union[str, None]) -> None:
        self.event_type = event_type
        super().__init__(f"Unknown webhook event type: {event_type!r}")


def validate_event(
    body: Union[str, bytes], headers: dict[str, str], secret: str
) -> WebhoookPayload:
    base64_secret = base64.b64encode(secret.encode()).decode()
    webhook = Webhook(base64_secret)

    try:
        data = webhook.verify(body, headers)
    except _WebhookVerificationError as e:
        raise WebhookVerificationError(str(e)) from e

    if isinstance(data, dict):
        event_type = data.get("type")
        if event_type not in _KNOWN_EVENT_TYPES:
            raise WebhookUnknownTypeError(event_type)

    return WebhookPayloadAdapter.validate_python(data)


__all__ = [
    "WebhookUnknownTypeError",
    "WebhookVerificationError",
    "WebhoookPayload",
    "validate_event",
]
