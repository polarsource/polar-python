import base64
from typing import Any, Dict, Union

from pydantic import Discriminator, Tag, TypeAdapter
from standardwebhooks.webhooks import Webhook
from standardwebhooks.webhooks import (
    WebhookVerificationError as _WebhookVerificationError,
)
from typing_extensions import Annotated

from polar_sdk.models import (
    WebhookBenefitCreatedPayload,
    WebhookBenefitCreatedPayloadType,
    WebhookBenefitGrantCreatedPayload,
    WebhookBenefitGrantCreatedPayloadType,
    WebhookBenefitGrantRevokedPayload,
    WebhookBenefitGrantRevokedPayloadType,
    WebhookBenefitGrantUpdatedPayload,
    WebhookBenefitGrantUpdatedPayloadType,
    WebhookBenefitUpdatedPayload,
    WebhookBenefitUpdatedPayloadType,
    WebhookCheckoutCreatedPayload,
    WebhookCheckoutCreatedPayloadType,
    WebhookCheckoutUpdatedPayload,
    WebhookCheckoutUpdatedPayloadType,
    WebhookOrderCreatedPayload,
    WebhookOrderCreatedPayloadType,
    WebhookOrganizationUpdatedPayload,
    WebhookOrganizationUpdatedPayloadType,
    WebhookPledgeCreatedPayload,
    WebhookPledgeCreatedPayloadType,
    WebhookPledgeUpdatedPayload,
    WebhookPledgeUpdatedPayloadType,
    WebhookProductCreatedPayload,
    WebhookProductCreatedPayloadType,
    WebhookProductUpdatedPayload,
    WebhookProductUpdatedPayloadType,
    WebhookSubscriptionActivePayload,
    WebhookSubscriptionActivePayloadType,
    WebhookSubscriptionCanceledPayload,
    WebhookSubscriptionCanceledPayloadType,
    WebhookSubscriptionCreatedPayload,
    WebhookSubscriptionCreatedPayloadType,
    WebhookSubscriptionRevokedPayload,
    WebhookSubscriptionRevokedPayloadType,
    WebhookSubscriptionUpdatedPayload,
    WebhookSubscriptionUpdatedPayloadType,
)


def _get_discriminator(v: Any) -> Union[str, None]:
    if isinstance(v, dict):
        return v.get("type")
    return getattr(v, "type", None)


WebhoookPayload = Annotated[
    Union[
        Annotated[
            WebhookBenefitCreatedPayload,
            Tag(WebhookBenefitCreatedPayloadType.BENEFIT_CREATED),
        ],
        Annotated[
            WebhookBenefitGrantCreatedPayload,
            Tag(WebhookBenefitGrantCreatedPayloadType.BENEFIT_GRANT_CREATED),
        ],
        Annotated[
            WebhookBenefitGrantRevokedPayload,
            Tag(WebhookBenefitGrantRevokedPayloadType.BENEFIT_GRANT_REVOKED),
        ],
        Annotated[
            WebhookBenefitGrantUpdatedPayload,
            Tag(WebhookBenefitGrantUpdatedPayloadType.BENEFIT_GRANT_UPDATED),
        ],
        Annotated[
            WebhookBenefitUpdatedPayload,
            Tag(WebhookBenefitUpdatedPayloadType.BENEFIT_UPDATED),
        ],
        Annotated[
            WebhookCheckoutCreatedPayload,
            Tag(WebhookCheckoutCreatedPayloadType.CHECKOUT_CREATED),
        ],
        Annotated[
            WebhookCheckoutUpdatedPayload,
            Tag(WebhookCheckoutUpdatedPayloadType.CHECKOUT_UPDATED),
        ],
        Annotated[
            WebhookOrderCreatedPayload,
            Tag(WebhookOrderCreatedPayloadType.ORDER_CREATED),
        ],
        Annotated[
            WebhookOrganizationUpdatedPayload,
            Tag(WebhookOrganizationUpdatedPayloadType.ORGANIZATION_UPDATED),
        ],
        Annotated[
            WebhookPledgeCreatedPayload,
            Tag(WebhookPledgeCreatedPayloadType.PLEDGE_CREATED),
        ],
        Annotated[
            WebhookPledgeUpdatedPayload,
            Tag(WebhookPledgeUpdatedPayloadType.PLEDGE_UPDATED),
        ],
        Annotated[
            WebhookProductCreatedPayload,
            Tag(WebhookProductCreatedPayloadType.PRODUCT_CREATED),
        ],
        Annotated[
            WebhookProductUpdatedPayload,
            Tag(WebhookProductUpdatedPayloadType.PRODUCT_UPDATED),
        ],
        Annotated[
            WebhookSubscriptionActivePayload,
            Tag(WebhookSubscriptionActivePayloadType.SUBSCRIPTION_ACTIVE),
        ],
        Annotated[
            WebhookSubscriptionCanceledPayload,
            Tag(WebhookSubscriptionCanceledPayloadType.SUBSCRIPTION_CANCELED),
        ],
        Annotated[
            WebhookSubscriptionCreatedPayload,
            Tag(WebhookSubscriptionCreatedPayloadType.SUBSCRIPTION_CREATED),
        ],
        Annotated[
            WebhookSubscriptionRevokedPayload,
            Tag(WebhookSubscriptionRevokedPayloadType.SUBSCRIPTION_REVOKED),
        ],
        Annotated[
            WebhookSubscriptionUpdatedPayload,
            Tag(WebhookSubscriptionUpdatedPayloadType.SUBSCRIPTION_UPDATED),
        ],
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
