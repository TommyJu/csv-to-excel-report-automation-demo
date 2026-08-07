import pandas as pd
from src.analysis.models.report_models import TimeAnalysis


def analyze_trends(df: pd.DataFrame) -> TimeAnalysis:

    df = df.copy()

    df["Date"] = pd.to_datetime(
        df["Date"]
    )


    # Daily patterns

    sales_by_day = (
        df.groupby("Day")["Total_Qty"]
        .sum()
        .sort_values(ascending=False)
    )


    # Monthly trends

    monthly_sales = (
        df.groupby(
            df["Date"].dt.month
        )["Total_Qty"]
        .sum()
    )


    # Fill missing months

    monthly_sales = monthly_sales.reindex(
        range(1, 13),
        fill_value=0
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
        monthly_sales.index.map(month_names)
    )


    return TimeAnalysis(
        sales_by_day=sales_by_day.to_dict(),
        sales_by_month=monthly_sales.to_dict()
    )