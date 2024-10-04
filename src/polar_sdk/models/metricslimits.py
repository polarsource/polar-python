"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .metricsintervalslimits import (
    MetricsIntervalsLimits,
    MetricsIntervalsLimitsTypedDict,
)
from datetime import date
from polar_sdk.types import BaseModel
from typing_extensions import TypedDict


class MetricsLimitsTypedDict(TypedDict):
    r"""Date limits to get metrics."""

    min_date: date
    r"""Minimum date to get metrics."""
    intervals: MetricsIntervalsLimitsTypedDict
    r"""Limits for each interval."""


class MetricsLimits(BaseModel):
    r"""Date limits to get metrics."""

    min_date: date
    r"""Minimum date to get metrics."""

    intervals: MetricsIntervalsLimits
    r"""Limits for each interval."""
