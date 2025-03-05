import base64
from typing import Any, Dict, Union

from pydantic import Discriminator, Tag, TypeAdapter
from standardwebhooks.webhooks import Webhook
from standardwebhooks.webhooks import (
    WebhookVerificationError as _WebhookVerificationError,
)
from typing_extensions import Annotated

from polar_sdk.models import (
    WebhookCustomerCreatedPayload,
    WebhookCustomerUpdatedPayload,
    WebhookCustomerDeletedPayload,
    WebhookCustomerStateChangedPayload,
    WebhookBenefitCreatedPayload,
    WebhookBenefitGrantCreatedPayload,
    WebhookBenefitGrantRevokedPayload,
    WebhookBenefitGrantUpdatedPayload,
    WebhookBenefitUpdatedPayload,
    WebhookCheckoutCreatedPayload,
    WebhookCheckoutUpdatedPayload,
    WebhookOrderCreatedPayload,
    WebhookOrganizationUpdatedPayload,
    WebhookPledgeCreatedPayload,
    WebhookPledgeUpdatedPayload,
    WebhookProductCreatedPayload,
    WebhookProductUpdatedPayload,
    WebhookSubscriptionActivePayload,
    WebhookSubscriptionCanceledPayload,
    WebhookSubscriptionCreatedPayload,
    WebhookSubscriptionRevokedPayload,
    WebhookSubscriptionUpdatedPayload,
)


def _get_discriminator(v: Any) -> Union[str, None]:
    if isinstance(v, dict):
        return v.get("type")
    return getattr(v, "type", None)


WebhoookPayload = Annotated[
    Union[
        Annotated[WebhookCustomerCreatedPayload, Tag("customer.created")],
        Annotated[WebhookCustomerUpdatedPayload, Tag("customer.updated")],
        Annotated[WebhookCustomerDeletedPayload, Tag("customer.deleted")],
        Annotated[WebhookCustomerStateChangedPayload, Tag("customer.state_changed")],
        Annotated[WebhookBenefitCreatedPayload, Tag("benefit.created")],
        Annotated[WebhookBenefitGrantCreatedPayload, Tag("benefit_grant.created")],
        Annotated[WebhookBenefitGrantRevokedPayload, Tag("benefit_grant.revoked")],
        Annotated[WebhookBenefitGrantUpdatedPayload, Tag("benefit_grant.updated")],
        Annotated[WebhookBenefitUpdatedPayload, Tag("benefit.updated")],
        Annotated[WebhookCheckoutCreatedPayload, Tag("checkout.created")],
        Annotated[WebhookCheckoutUpdatedPayload, Tag("checkout.updated")],
        Annotated[WebhookOrderCreatedPayload, Tag("order.created")],
        Annotated[WebhookOrganizationUpdatedPayload, Tag("organization.updated")],
        Annotated[WebhookPledgeCreatedPayload, Tag("pledge.created")],
        Annotated[WebhookPledgeUpdatedPayload, Tag("pledge.updated")],
        Annotated[WebhookProductCreatedPayload, Tag("product.created")],
        Annotated[WebhookProductUpdatedPayload, Tag("product.updated")],
        Annotated[WebhookSubscriptionActivePayload, Tag("subscription.active")],
        Annotated[WebhookSubscriptionCanceledPayload, Tag("subscription.canceled")],
        Annotated[WebhookSubscriptionCreatedPayload, Tag("subscription.created")],
        Annotated[WebhookSubscriptionRevokedPayload, Tag("subscription.revoked")],
        Annotated[WebhookSubscriptionUpdatedPayload, Tag("subscription.updated")],
    ],
    Discriminator(_get_discriminator),
]

WebhookPayloadAdapter: TypeAdapter[WebhoookPayload] = TypeAdapter(WebhoookPayload)


class WebhookVerificationError(_WebhookVerificationError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def validate_event(
    body: Union[str, bytes], headers: Dict[str, str], secret: str
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
