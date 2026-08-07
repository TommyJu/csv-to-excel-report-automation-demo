import pandas as pd
from src.analysis.models.report_models import SalesSummary


def analyze_summary(df: pd.DataFrame) -> SalesSummary:

    df = df.copy()

    df["Date"] = pd.to_datetime(
        df["Date"]
    )


    # -------------------------
    # Overall Metrics
    # -------------------------

    total_items = int(
        df["Total_Qty"].sum()
    )

    unique_products = (
        df["Menu"]
        .nunique()
    )

    total_sales_days = (
        df["Date"]
        .nunique()
    )

    average_daily_sales = (
        total_items /
        total_sales_days
        if total_sales_days > 0
        else 0
    )


    # -------------------------
    # Product Performance
    # -------------------------

    sales_by_menu = (
        df.groupby("Menu")["Total_Qty"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_item = (
        sales_by_menu.index[0]
    )

    best_item_qty = int(
        sales_by_menu.iloc[0]
    )


    # -------------------------
    # Day Performance
    # -------------------------

    sales_by_day = (
        df.groupby("Day")["Total_Qty"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_day = (
        sales_by_day.index[0]
    )

    best_day_qty = int(
        sales_by_day.iloc[0]
    )


    # -------------------------
    # Monthly Performance
    # -------------------------

    sales_by_month = (
        df.groupby(
            df["Date"].dt.month
        )["Total_Qty"]
        .sum()
        .reindex(
            range(1,13),
            fill_value=0
        )
    )


    month_names = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }


    best_month_num = (
        sales_by_month.idxmax()
    )


    best_month = (
        month_names[best_month_num]
    )

    best_month_qty = int(
        sales_by_month.max()
    )


    return SalesSummary(

        total_items_sold=total_items,

        unique_products=unique_products,

        total_sales_days=total_sales_days,

        average_daily_sales=round(
            average_daily_sales,
            2
        ),

        best_selling_item=best_item,

        best_selling_item_qty=best_item_qty,

        best_sales_day=best_day,

        best_sales_day_qty=best_day_qty,

        best_sales_month=best_month,

        best_sales_month_qty=best_month_qty
    )