from dataclasses import dataclass
from typing import Dict


@dataclass
class SalesSummary:
    """
    High-level business metrics.
    Used for dashboard KPIs.
    """

    total_items_sold: int

    unique_products: int
    total_sales_days: int
    average_daily_sales: float

    best_selling_item: str
    best_selling_item_qty: int

    best_sales_day: str
    best_sales_day_qty: int

    best_sales_month: str
    best_sales_month_qty: int


@dataclass
class MenuPerformance:
    """
    Product-level performance analysis.
    """

    sales_by_menu: dict
    top_products: dict
    product_rankings: list
    product_contribution: dict
    total_products: int


@dataclass
class TimeAnalysis:
    """
    Sales patterns over time.
    """

    sales_by_day: dict
    sales_by_month: dict
    monthly_growth: dict
    sales_by_date: dict
    best_sales_date: str
    average_daily_sales: float
    weekend_vs_weekday: dict


@dataclass
class PromotionAnalysis:
    """
    Measures whether promotions influence sales volume.
    """

    promotion_sales: int
    regular_sales: int
    promotion_lift: dict
    best_promotion_item: str

@dataclass
class SalesReport:
    """
    Complete analysis result.
    Passed into Excel/PDF generators.
    """

    summary: SalesSummary
    menu: MenuPerformance
    time: TimeAnalysis
    promotions: PromotionAnalysis