import pandas as pd
from .models.report_models import PromotionAnalysis


def analyze_promotions(df: pd.DataFrame):

    promo = df[
        df["Promotion"] == "Yes"
    ]

    regular = df[
        df["Promotion"] != "Yes"
    ]


    promotion_sales = promo["Total_Qty"].sum()

    regular_sales = regular["Total_Qty"].sum()


    promo_avg = (
        promo["Total_Qty"].sum()
        /
        promo["Date"].nunique()
    )


    regular_avg = (
        regular["Total_Qty"].sum()
        /
        regular["Date"].nunique()
    )


    impact = (
        ((promo_avg - regular_avg) / regular_avg) * 100
        if regular_avg > 0
        else 0
    )


    return PromotionAnalysis(
        promotion_sales=int(promotion_sales),
        regular_sales=int(regular_sales),
        promotion_percentage=round(
            impact,
            2
        )
    )