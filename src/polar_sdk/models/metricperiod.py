"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from polar_sdk.types import BaseModel
from typing import TypedDict


class MetricPeriodTypedDict(TypedDict):
    timestamp: datetime
    r"""Timestamp of this period data."""
    orders: int
    revenue: int
    average_order_value: int
    one_time_products: int
    one_time_products_revenue: int
    new_subscriptions: int
    new_subscriptions_revenue: int
    renewed_subscriptions: int
    renewed_subscriptions_revenue: int
    active_subscriptions: int
    monthly_recurring_revenue: int


class MetricPeriod(BaseModel):
    timestamp: datetime
    r"""Timestamp of this period data."""

    orders: int

    revenue: int

    average_order_value: int

    one_time_products: int

    one_time_products_revenue: int

    new_subscriptions: int

    new_subscriptions_revenue: int

    renewed_subscriptions: int

    renewed_subscriptions_revenue: int

    active_subscriptions: int

    monthly_recurring_revenue: int
