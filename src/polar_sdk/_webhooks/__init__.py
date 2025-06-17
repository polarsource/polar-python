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
    WebhookCheckoutUpdatedPayload,
    WebhookCustomerCreatedPayload,
    WebhookCustomerDeletedPayload,
    WebhookCustomerStateChangedPayload,
    WebhookCustomerUpdatedPayload,
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
        Annotated[WebhookCustomerCreatedPayload, Tag("customer.created")],
        Annotated[WebhookCustomerUpdatedPayload, Tag("customer.updated")],
        Annotated[WebhookCustomerDeletedPayload, Tag("customer.deleted")],
        Annotated[WebhookCustomerStateChangedPayload, Tag("customer.state_changed")],
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

WebhookPayloadAdapter: TypeAdapter[WebhoookPayload] = TypeAdapter(WebhoookPayload)


class WebhookVerificationError(_WebhookVerificationError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def validate_event(
    body: Union[str, bytes], headers: dict[str, str], secret: str
) -> WebhoookPayload:
    base64_secret = base64.b64encode(secret.encode()).decode()
    webhook = Webhook(base64_secret)

    try:
        data = webhook.verify(body, headers)
    except _WebhookVerificationError as e:
        raise WebhookVerificationError(str(e)) from e

    return WebhookPayloadAdapter.validate_python(data)


__all__ = [
    "WebhookVerificationError",
    "WebhoookPayload",
    "validate_event",
]
