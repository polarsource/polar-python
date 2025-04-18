"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from polar_sdk.benefit_grants import BenefitGrants
from polar_sdk.downloadables import Downloadables
from polar_sdk.polar_customer_meters import PolarCustomerMeters
from polar_sdk.polar_customers import PolarCustomers
from polar_sdk.polar_license_keys import PolarLicenseKeys
from polar_sdk.polar_orders import PolarOrders
from polar_sdk.polar_organizations import PolarOrganizations
from polar_sdk.polar_subscriptions import PolarSubscriptions


class CustomerPortal(BaseSDK):
    benefit_grants: BenefitGrants
    customers: PolarCustomers
    customer_meters: PolarCustomerMeters
    downloadables: Downloadables
    license_keys: PolarLicenseKeys
    orders: PolarOrders
    organizations: PolarOrganizations
    subscriptions: PolarSubscriptions

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.benefit_grants = BenefitGrants(self.sdk_configuration)
        self.customers = PolarCustomers(self.sdk_configuration)
        self.customer_meters = PolarCustomerMeters(self.sdk_configuration)
        self.downloadables = Downloadables(self.sdk_configuration)
        self.license_keys = PolarLicenseKeys(self.sdk_configuration)
        self.orders = PolarOrders(self.sdk_configuration)
        self.organizations = PolarOrganizations(self.sdk_configuration)
        self.subscriptions = PolarSubscriptions(self.sdk_configuration)
