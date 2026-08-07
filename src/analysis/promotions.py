import pandas as pd
from .models.report_models import PromotionAnalysis


def analyze_promotions(df: pd.DataFrame) -> PromotionAnalysis:

    df = df.copy()

    # Normalize promotion values
    df["Promotion"] = (
        df["Promotion"]
        .str.strip()
        .str.lower()
    )


    # -------------------------
    # Total Sales Summary
    # -------------------------

    promotion_sales = (
        df[df["Promotion"] == "yes"]
        ["Total_Qty"]
        .sum()
    )

    regular_sales = (
        df[df["Promotion"] == "no"]
        ["Total_Qty"]
        .sum()
    )


    # -------------------------
    # Promotion Lift Analysis
    # -------------------------

    # Average sales per product occurrence
    product_promotion = (
        df.groupby(
            ["Menu", "Promotion"]
        )["Total_Qty"]
        .mean()
        .unstack(
            fill_value=0
        )
    )


    # Ensure columns exist
    if "yes" not in product_promotion.columns:
        product_promotion["yes"] = 0

    if "no" not in product_promotion.columns:
        product_promotion["no"] = 0


    promotion_lift = {}


    for product, row in product_promotion.iterrows():

        regular_avg = row["no"]
        promoted_avg = row["yes"]


        if regular_avg > 0:

            lift = (
                (promoted_avg - regular_avg)
                /
                regular_avg
                *
                100
            )

        else:
            lift = 0


        promotion_lift[product] = round(
            lift,
            2
        )


    best_promotion_item = max(
        promotion_lift,
        key=promotion_lift.get
    )


    return PromotionAnalysis(
        promotion_sales=int(
            promotion_sales
        ),

        regular_sales=int(
            regular_sales
        ),

        promotion_lift=promotion_lift,

        best_promotion_item=best_promotion_item
    )