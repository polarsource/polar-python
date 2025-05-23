"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from polar_sdk.types import BaseModel
from typing import Union
from typing_extensions import TypeAliasType, TypedDict


MetricsTotalsOrdersTypedDict = TypeAliasType(
    "MetricsTotalsOrdersTypedDict", Union[int, float]
)


MetricsTotalsOrders = TypeAliasType("MetricsTotalsOrders", Union[int, float])


MetricsTotalsRevenueTypedDict = TypeAliasType(
    "MetricsTotalsRevenueTypedDict", Union[int, float]
)


MetricsTotalsRevenue = TypeAliasType("MetricsTotalsRevenue", Union[int, float])


MetricsTotalsCumulativeRevenueTypedDict = TypeAliasType(
    "MetricsTotalsCumulativeRevenueTypedDict", Union[int, float]
)


MetricsTotalsCumulativeRevenue = TypeAliasType(
    "MetricsTotalsCumulativeRevenue", Union[int, float]
)


MetricsTotalsAverageOrderValueTypedDict = TypeAliasType(
    "MetricsTotalsAverageOrderValueTypedDict", Union[int, float]
)


MetricsTotalsAverageOrderValue = TypeAliasType(
    "MetricsTotalsAverageOrderValue", Union[int, float]
)


MetricsTotalsOneTimeProductsTypedDict = TypeAliasType(
    "MetricsTotalsOneTimeProductsTypedDict", Union[int, float]
)


MetricsTotalsOneTimeProducts = TypeAliasType(
    "MetricsTotalsOneTimeProducts", Union[int, float]
)


MetricsTotalsOneTimeProductsRevenueTypedDict = TypeAliasType(
    "MetricsTotalsOneTimeProductsRevenueTypedDict", Union[int, float]
)


MetricsTotalsOneTimeProductsRevenue = TypeAliasType(
    "MetricsTotalsOneTimeProductsRevenue", Union[int, float]
)


MetricsTotalsNewSubscriptionsTypedDict = TypeAliasType(
    "MetricsTotalsNewSubscriptionsTypedDict", Union[int, float]
)


MetricsTotalsNewSubscriptions = TypeAliasType(
    "MetricsTotalsNewSubscriptions", Union[int, float]
)


MetricsTotalsNewSubscriptionsRevenueTypedDict = TypeAliasType(
    "MetricsTotalsNewSubscriptionsRevenueTypedDict", Union[int, float]
)


MetricsTotalsNewSubscriptionsRevenue = TypeAliasType(
    "MetricsTotalsNewSubscriptionsRevenue", Union[int, float]
)


MetricsTotalsRenewedSubscriptionsTypedDict = TypeAliasType(
    "MetricsTotalsRenewedSubscriptionsTypedDict", Union[int, float]
)


MetricsTotalsRenewedSubscriptions = TypeAliasType(
    "MetricsTotalsRenewedSubscriptions", Union[int, float]
)


MetricsTotalsRenewedSubscriptionsRevenueTypedDict = TypeAliasType(
    "MetricsTotalsRenewedSubscriptionsRevenueTypedDict", Union[int, float]
)


MetricsTotalsRenewedSubscriptionsRevenue = TypeAliasType(
    "MetricsTotalsRenewedSubscriptionsRevenue", Union[int, float]
)


MetricsTotalsActiveSubscriptionsTypedDict = TypeAliasType(
    "MetricsTotalsActiveSubscriptionsTypedDict", Union[int, float]
)


MetricsTotalsActiveSubscriptions = TypeAliasType(
    "MetricsTotalsActiveSubscriptions", Union[int, float]
)


MetricsTotalsMonthlyRecurringRevenueTypedDict = TypeAliasType(
    "MetricsTotalsMonthlyRecurringRevenueTypedDict", Union[int, float]
)


MetricsTotalsMonthlyRecurringRevenue = TypeAliasType(
    "MetricsTotalsMonthlyRecurringRevenue", Union[int, float]
)


MetricsTotalsCheckoutsTypedDict = TypeAliasType(
    "MetricsTotalsCheckoutsTypedDict", Union[int, float]
)


MetricsTotalsCheckouts = TypeAliasType("MetricsTotalsCheckouts", Union[int, float])


MetricsTotalsSucceededCheckoutsTypedDict = TypeAliasType(
    "MetricsTotalsSucceededCheckoutsTypedDict", Union[int, float]
)


MetricsTotalsSucceededCheckouts = TypeAliasType(
    "MetricsTotalsSucceededCheckouts", Union[int, float]
)


MetricsTotalsCheckoutsConversionTypedDict = TypeAliasType(
    "MetricsTotalsCheckoutsConversionTypedDict", Union[int, float]
)


MetricsTotalsCheckoutsConversion = TypeAliasType(
    "MetricsTotalsCheckoutsConversion", Union[int, float]
)


class MetricsTotalsTypedDict(TypedDict):
    orders: MetricsTotalsOrdersTypedDict
    revenue: MetricsTotalsRevenueTypedDict
    cumulative_revenue: MetricsTotalsCumulativeRevenueTypedDict
    average_order_value: MetricsTotalsAverageOrderValueTypedDict
    one_time_products: MetricsTotalsOneTimeProductsTypedDict
    one_time_products_revenue: MetricsTotalsOneTimeProductsRevenueTypedDict
    new_subscriptions: MetricsTotalsNewSubscriptionsTypedDict
    new_subscriptions_revenue: MetricsTotalsNewSubscriptionsRevenueTypedDict
    renewed_subscriptions: MetricsTotalsRenewedSubscriptionsTypedDict
    renewed_subscriptions_revenue: MetricsTotalsRenewedSubscriptionsRevenueTypedDict
    active_subscriptions: MetricsTotalsActiveSubscriptionsTypedDict
    monthly_recurring_revenue: MetricsTotalsMonthlyRecurringRevenueTypedDict
    checkouts: MetricsTotalsCheckoutsTypedDict
    succeeded_checkouts: MetricsTotalsSucceededCheckoutsTypedDict
    checkouts_conversion: MetricsTotalsCheckoutsConversionTypedDict


class MetricsTotals(BaseModel):
    orders: MetricsTotalsOrders

    revenue: MetricsTotalsRevenue

    cumulative_revenue: MetricsTotalsCumulativeRevenue

    average_order_value: MetricsTotalsAverageOrderValue

    one_time_products: MetricsTotalsOneTimeProducts

    one_time_products_revenue: MetricsTotalsOneTimeProductsRevenue

    new_subscriptions: MetricsTotalsNewSubscriptions

    new_subscriptions_revenue: MetricsTotalsNewSubscriptionsRevenue

    renewed_subscriptions: MetricsTotalsRenewedSubscriptions

    renewed_subscriptions_revenue: MetricsTotalsRenewedSubscriptionsRevenue

    active_subscriptions: MetricsTotalsActiveSubscriptions

    monthly_recurring_revenue: MetricsTotalsMonthlyRecurringRevenue

    checkouts: MetricsTotalsCheckouts

    succeeded_checkouts: MetricsTotalsSucceededCheckouts

    checkouts_conversion: MetricsTotalsCheckoutsConversion
