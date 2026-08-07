import pandas as pd
from src.analysis.models.report_models import TimeAnalysis


def analyze_trends(df: pd.DataFrame) -> TimeAnalysis:

    df = df.copy()

    df["Date"] = pd.to_datetime(
        df["Date"]
    )


    # -------------------------
    # Sales by Day of Week
    # -------------------------

    sales_by_day = (
        df.groupby("Day")["Total_Qty"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


    # -------------------------
    # Monthly Sales
    # -------------------------

    monthly_sales = (
        df.groupby(
            df["Date"].dt.month
        )["Total_Qty"]
        .sum()
        .reindex(
            range(1, 13),
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


    monthly_sales.index = (
        monthly_sales.index
        .map(month_names)
    )


    # -------------------------
    # Monthly Growth
    # -------------------------

    monthly_growth = (
        monthly_sales
        .pct_change()
        .fillna(0)
        * 100
    )


    monthly_growth = (
        monthly_growth
        .round(2)
    )


    # -------------------------
    # Daily Sales Trends
    # -------------------------

    sales_by_date = (
        df.groupby("Date")["Total_Qty"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


    best_sales_date = (
        sales_by_date
        .idxmax()
        .strftime("%Y-%m-%d")
    )


    average_daily_sales = (
        sales_by_date
        .mean()
    )


    # -------------------------
    # Weekend vs Weekday
    # -------------------------

    df["Day_Type"] = df["Date"].dt.dayofweek.map(
        lambda x: "Weekend"
        if x >= 5
        else "Weekday"
    )


    weekend_vs_weekday = (
        df.groupby("Day_Type")["Total_Qty"]
        .sum()
    )


    return TimeAnalysis(

        sales_by_day=sales_by_day.to_dict(),

        sales_by_month=monthly_sales.to_dict(),

        monthly_growth=monthly_growth.to_dict(),

        sales_by_date=sales_by_date.to_dict(),

        best_sales_date=best_sales_date,

        average_daily_sales=round(
            average_daily_sales,
            2
        ),

        weekend_vs_weekday=
            weekend_vs_weekday.to_dict()
    )