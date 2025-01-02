import base64
import datetime
import uuid
from typing import Dict, Union

import pytest
from pydantic import ValidationError
from standardwebhooks.webhooks import Webhook

from polar_sdk.models import (
    Checkout,
    CheckoutProduct,
    CheckoutStatus,
    PaymentProcessor,
    PaymentProcessorMetadata,
    ProductPriceOneTimeFixed,
    WebhookCheckoutCreatedPayload
)
from polar_sdk.webhooks import WebhookVerificationError, validate_event

ORGANIZATION_ID = str(uuid.uuid4())
PRODUCT_ID = str(uuid.uuid4())
PRICE_ID = str(uuid.uuid4())

price = ProductPriceOneTimeFixed(
    id=PRICE_ID,
    created_at=datetime.datetime.now(datetime.timezone.utc),
    modified_at=None,
    is_archived=False,
    product_id=PRODUCT_ID,
    price_currency="usd",
    price_amount=1000,
    TYPE="one_time",
    AMOUNT_TYPE="fixed"
)

product = CheckoutProduct(
    id=PRODUCT_ID,
    created_at=datetime.datetime.now(datetime.timezone.utc),
    modified_at=None,
    name="Product",
    description=None,
    is_recurring=False,
    is_archived=False,
    organization_id=ORGANIZATION_ID,
    prices=[price],
    benefits=[],
    medias=[],
)

checkout_created = WebhookCheckoutCreatedPayload(
    TYPE="checkout.created",
    data=Checkout(
        id=str(uuid.uuid4()),
        created_at=datetime.datetime.now(datetime.timezone.utc),
        modified_at=None,
        status=CheckoutStatus.OPEN,
        client_secret="CLIENT_SECRET",
        url="https://polar.sh/checkout/CLIENT_SECRET",
        expires_at=datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=1),
        success_url="https://polar.sh/checkout/CLIENT_SECRET/confirmation",
        embed_origin=None,
        tax_amount=0,
        amount=0,
        currency="usd",
        subtotal_amount=1000,
        total_amount=1000,
        product_id=PRODUCT_ID,
        product_price_id=PRICE_ID,
        discount_id=None,
        allow_discount_codes=True,
        is_discount_applicable=True,
        is_free_product_price=False,
        is_payment_required=True,
        is_payment_setup_required=False,
        is_payment_form_required=True,
        customer_id=None,
        customer_name=None,
        customer_email=None,
        customer_ip_address=None,
        customer_billing_address=None,
        customer_tax_id=None,
        payment_processor_metadata=PaymentProcessorMetadata(),
        metadata={},
        product=product,
        product_price=price,
        discount=None,
        subscription_id=None,
        attached_custom_fields=[],
        custom_field_data=None,
        payment_processor=PaymentProcessor.STRIPE,
        customer_metadata={},
    ),
)

WEBHOOK_SECRET = "TestSecret"
WEBHOOK_SECRET_BASE64 = base64.b64encode(WEBHOOK_SECRET.encode()).decode()


def get_headers(
    body: str,
    webhook_id: str = "WEBHOOK_ID",
    timestamp: Union[datetime.datetime, None] = None,
) -> Dict[str, str]:
    timestamp = timestamp or datetime.datetime.now(datetime.timezone.utc)
    signature = Webhook(WEBHOOK_SECRET_BASE64).sign(webhook_id, timestamp, body)
    return {
        "webhook-id": webhook_id,
        "webhook-signature": signature,
        "webhook-timestamp": str(timestamp.timestamp()),
    }


def test_valid_signature() -> None:
    body = checkout_created.model_dump_json(by_alias=True)
    headers = get_headers(body)

    payload = validate_event(body, headers, WEBHOOK_SECRET)
    assert payload == checkout_created


def test_invalid_signature() -> None:
    body = checkout_created.model_dump_json(by_alias=True)
    headers = get_headers(body)

    with pytest.raises(WebhookVerificationError):
        validate_event(body, headers, "AnotherSecret")


def test_invalid_payload() -> None:
    body = '{"type": "unknown"}'
    headers = get_headers(body)

    with pytest.raises(ValidationError):
        validate_event(body, headers, WEBHOOK_SECRET)
