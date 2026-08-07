from dataclasses import dataclass
from typing import Dict


@dataclass
class SalesSummary:
    """
    High-level business metrics.
    Used for dashboard KPIs.
    """

    total_items_sold: int
    best_selling_item: str
    best_sales_day: str
    best_sales_month: str


@dataclass
class MenuPerformance:
    """
    Product-level performance analysis.
    """

    sales_by_menu: Dict[str, int]
    top_products: Dict[str, int]


@dataclass
class TimeAnalysis:
    """
    Sales patterns over time.
    """

    sales_by_day: Dict[str, int]
    sales_by_month: Dict[str, int]


@dataclass
class PromotionAnalysis:
    """
    Measures whether promotions influence sales volume.
    """

    promotion_sales: int
    regular_sales: int
    promotion_percentage: float


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