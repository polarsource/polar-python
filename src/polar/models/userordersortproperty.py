"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class UserOrderSortProperty(str, Enum):
    CREATED_AT = "created_at"
    MINUS_CREATED_AT = "-created_at"
    AMOUNT = "amount"
    MINUS_AMOUNT = "-amount"
    ORGANIZATION = "organization"
    MINUS_ORGANIZATION = "-organization"
    PRODUCT = "product"
    MINUS_PRODUCT = "-product"
    SUBSCRIPTION = "subscription"
    MINUS_SUBSCRIPTION = "-subscription"