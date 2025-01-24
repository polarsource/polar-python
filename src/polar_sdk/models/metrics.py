"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .metric import Metric, MetricTypedDict
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class MetricsTypedDict(TypedDict):
    orders: MetricTypedDict
    r"""Information about a metric."""
    revenue: MetricTypedDict
    r"""Information about a metric."""
    cumulative_revenue: MetricTypedDict
    r"""Information about a metric."""
    average_order_value: MetricTypedDict
    r"""Information about a metric."""
    one_time_products: MetricTypedDict
    r"""Information about a metric."""
    one_time_products_revenue: MetricTypedDict
    r"""Information about a metric."""
    new_subscriptions: MetricTypedDict
    r"""Information about a metric."""
    new_subscriptions_revenue: MetricTypedDict
    r"""Information about a metric."""
    renewed_subscriptions: MetricTypedDict
    r"""Information about a metric."""
    renewed_subscriptions_revenue: MetricTypedDict
    r"""Information about a metric."""
    active_subscriptions: MetricTypedDict
    r"""Information about a metric."""
    monthly_recurring_revenue: MetricTypedDict
    r"""Information about a metric."""


class Metrics(BaseModel):
    orders: Metric
    r"""Information about a metric."""

    revenue: Metric
    r"""Information about a metric."""

    cumulative_revenue: Metric
    r"""Information about a metric."""

    average_order_value: Metric
    r"""Information about a metric."""

    one_time_products: Metric
    r"""Information about a metric."""

    one_time_products_revenue: Metric
    r"""Information about a metric."""

    new_subscriptions: Metric
    r"""Information about a metric."""

    new_subscriptions_revenue: Metric
    r"""Information about a metric."""

    renewed_subscriptions: Metric
    r"""Information about a metric."""

    renewed_subscriptions_revenue: Metric
    r"""Information about a metric."""

    active_subscriptions: Metric
    r"""Information about a metric."""

    monthly_recurring_revenue: Metric
    r"""Information about a metric."""
