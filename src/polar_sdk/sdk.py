"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from polar_sdk import models, utils
from polar_sdk._hooks import SDKHooks
from polar_sdk.benefits import Benefits
from polar_sdk.checkout_links import CheckoutLinks
from polar_sdk.checkouts import Checkouts
from polar_sdk.custom_fields import CustomFields
from polar_sdk.customer_meters import CustomerMeters
from polar_sdk.customer_portal import CustomerPortal
from polar_sdk.customer_sessions import CustomerSessions
from polar_sdk.customers import Customers
from polar_sdk.discounts import Discounts
from polar_sdk.events import Events
from polar_sdk.files import Files
from polar_sdk.license_keys import LicenseKeys
from polar_sdk.meters import Meters
from polar_sdk.metrics_sdk import MetricsSDK
from polar_sdk.oauth2 import Oauth2
from polar_sdk.orders import Orders
from polar_sdk.organizations import Organizations
from polar_sdk.products import Products
from polar_sdk.refunds import Refunds
from polar_sdk.subscriptions import Subscriptions
from polar_sdk.types import OptionalNullable, UNSET
from typing import Any, Callable, Dict, Optional, Union, cast
import weakref


class Polar(BaseSDK):
    r"""Polar API: Polar HTTP and Webhooks API

    Read the docs at https://docs.polar.sh/api-reference
    """

    organizations: Organizations
    subscriptions: Subscriptions
    oauth2: Oauth2
    benefits: Benefits
    products: Products
    orders: Orders
    refunds: Refunds
    checkouts: Checkouts
    files: Files
    metrics: MetricsSDK
    license_keys: LicenseKeys
    checkout_links: CheckoutLinks
    custom_fields: CustomFields
    discounts: Discounts
    customers: Customers
    customer_portal: CustomerPortal
    customer_sessions: CustomerSessions
    events: Events
    meters: Meters
    customer_meters: CustomerMeters

    def __init__(
        self,
        access_token: Optional[
            Union[Optional[str], Callable[[], Optional[str]]]
        ] = None,
        server: Optional[str] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param access_token: The access_token required for authentication
        :param server: The server by name to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(access_token):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(access_token=access_token())
        else:
            security = models.Security(access_token=access_token)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server=server,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.organizations = Organizations(self.sdk_configuration)
        self.subscriptions = Subscriptions(self.sdk_configuration)
        self.oauth2 = Oauth2(self.sdk_configuration)
        self.benefits = Benefits(self.sdk_configuration)
        self.products = Products(self.sdk_configuration)
        self.orders = Orders(self.sdk_configuration)
        self.refunds = Refunds(self.sdk_configuration)
        self.checkouts = Checkouts(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.metrics = MetricsSDK(self.sdk_configuration)
        self.license_keys = LicenseKeys(self.sdk_configuration)
        self.checkout_links = CheckoutLinks(self.sdk_configuration)
        self.custom_fields = CustomFields(self.sdk_configuration)
        self.discounts = Discounts(self.sdk_configuration)
        self.customers = Customers(self.sdk_configuration)
        self.customer_portal = CustomerPortal(self.sdk_configuration)
        self.customer_sessions = CustomerSessions(self.sdk_configuration)
        self.events = Events(self.sdk_configuration)
        self.meters = Meters(self.sdk_configuration)
        self.customer_meters = CustomerMeters(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
