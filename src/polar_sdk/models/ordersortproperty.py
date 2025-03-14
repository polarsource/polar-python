"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class OrderSortProperty(str, Enum):
    CREATED_AT = "created_at"
    MINUS_CREATED_AT = "-created_at"
    AMOUNT = "amount"
    MINUS_AMOUNT = "-amount"
    NET_AMOUNT = "net_amount"
    MINUS_NET_AMOUNT = "-net_amount"
    CUSTOMER = "customer"
    MINUS_CUSTOMER = "-customer"
    PRODUCT = "product"
    MINUS_PRODUCT = "-product"
    DISCOUNT = "discount"
    MINUS_DISCOUNT = "-discount"
    SUBSCRIPTION = "subscription"
    MINUS_SUBSCRIPTION = "-subscription"
