"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .metricsintervallimit import MetricsIntervalLimit, MetricsIntervalLimitTypedDict
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class MetricsIntervalsLimitsTypedDict(TypedDict):
    r"""Date interval limits to get metrics for each interval."""

    hour: MetricsIntervalLimitTypedDict
    r"""Limits for the hour interval."""
    day: MetricsIntervalLimitTypedDict
    r"""Limits for the day interval."""
    week: MetricsIntervalLimitTypedDict
    r"""Limits for the week interval."""
    month: MetricsIntervalLimitTypedDict
    r"""Limits for the month interval."""
    year: MetricsIntervalLimitTypedDict
    r"""Limits for the year interval."""


class MetricsIntervalsLimits(BaseModel):
    r"""Date interval limits to get metrics for each interval."""

    hour: MetricsIntervalLimit
    r"""Limits for the hour interval."""

    day: MetricsIntervalLimit
    r"""Limits for the day interval."""

    week: MetricsIntervalLimit
    r"""Limits for the week interval."""

    month: MetricsIntervalLimit
    r"""Limits for the month interval."""

    year: MetricsIntervalLimit
    r"""Limits for the year interval."""
