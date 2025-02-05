"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class Scope(str, Enum):
    OPENID = "openid"
    PROFILE = "profile"
    EMAIL = "email"
    USER_READ = "user:read"
    ADMIN = "admin"
    WEB_DEFAULT = "web_default"
    ORGANIZATIONS_READ = "organizations:read"
    ORGANIZATIONS_WRITE = "organizations:write"
    CUSTOM_FIELDS_READ = "custom_fields:read"
    CUSTOM_FIELDS_WRITE = "custom_fields:write"
    DISCOUNTS_READ = "discounts:read"
    DISCOUNTS_WRITE = "discounts:write"
    CHECKOUT_LINKS_READ = "checkout_links:read"
    CHECKOUT_LINKS_WRITE = "checkout_links:write"
    CHECKOUTS_READ = "checkouts:read"
    CHECKOUTS_WRITE = "checkouts:write"
    PRODUCTS_READ = "products:read"
    PRODUCTS_WRITE = "products:write"
    BENEFITS_READ = "benefits:read"
    BENEFITS_WRITE = "benefits:write"
    EVENTS_READ = "events:read"
    EVENTS_WRITE = "events:write"
    METERS_READ = "meters:read"
    METERS_WRITE = "meters:write"
    FILES_READ = "files:read"
    FILES_WRITE = "files:write"
    SUBSCRIPTIONS_READ = "subscriptions:read"
    SUBSCRIPTIONS_WRITE = "subscriptions:write"
    CUSTOMERS_READ = "customers:read"
    CUSTOMERS_WRITE = "customers:write"
    CUSTOMER_SESSIONS_WRITE = "customer_sessions:write"
    ORDERS_READ = "orders:read"
    REFUNDS_READ = "refunds:read"
    REFUNDS_WRITE = "refunds:write"
    METRICS_READ = "metrics:read"
    WEBHOOKS_READ = "webhooks:read"
    WEBHOOKS_WRITE = "webhooks:write"
    EXTERNAL_ORGANIZATIONS_READ = "external_organizations:read"
    LICENSE_KEYS_READ = "license_keys:read"
    LICENSE_KEYS_WRITE = "license_keys:write"
    REPOSITORIES_READ = "repositories:read"
    REPOSITORIES_WRITE = "repositories:write"
    ISSUES_READ = "issues:read"
    ISSUES_WRITE = "issues:write"
    CUSTOMER_PORTAL_READ = "customer_portal:read"
    CUSTOMER_PORTAL_WRITE = "customer_portal:write"
