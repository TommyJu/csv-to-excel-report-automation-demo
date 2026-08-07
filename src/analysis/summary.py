import pandas as pd
from src.analysis.models.report_models import SalesSummary


def analyze_summary(df: pd.DataFrame) -> SalesSummary:

    total_items = int(
        df["Total_Qty"].sum()
    )

    sales_by_menu = (
        df.groupby("Menu")["Total_Qty"]
        .sum()
        .sort_values(ascending=False)
    )

    sales_by_day = (
        df.groupby("Day")["Total_Qty"]
        .sum()
        .sort_values(ascending=False)
    )

    sales_by_month = (
        df.groupby("Month")["Total_Qty"]
        .sum()
        .sort_values(ascending=False)
    )


    return SalesSummary(
        total_items_sold=total_items,
        best_selling_item=sales_by_menu.index[0],
        best_sales_day=sales_by_day.index[0],
        best_sales_month=sales_by_month.index[0]
    )