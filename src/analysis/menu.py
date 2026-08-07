import pandas as pd
from src.analysis.models.report_models import MenuPerformance


def analyze_menu(df: pd.DataFrame) -> MenuPerformance:

    df = df.copy()


    # -------------------------
    # Total Sales By Product
    # -------------------------

    sales_by_menu = (
        df.groupby("Menu")["Total_Qty"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


    # -------------------------
    # Top Products
    # -------------------------

    top_products = (
        sales_by_menu
        .head(5)
        .to_dict()
    )


    # -------------------------
    # Product Rankings
    # -------------------------

    product_rankings = (
        sales_by_menu
        .reset_index()
        .rename(
            columns={
                "Total_Qty": "Units_Sold"
            }
        )
    )


    product_rankings["Rank"] = (
        range(
            1,
            len(product_rankings) + 1
        )
    )


    # Move rank to first column
    product_rankings = (
        product_rankings[
            [
                "Rank",
                "Menu",
                "Units_Sold"
            ]
        ]
    )


    # Convert dataframe to list
    product_rankings = (
        product_rankings
        .to_dict(
            orient="records"
        )
    )


    # -------------------------
    # Product Contribution
    # -------------------------

    total_sales = (
        sales_by_menu.sum()
    )


    product_contribution = (
        (
            sales_by_menu /
            total_sales
            *
            100
        )
        .round(2)
        .to_dict()
    )


    return MenuPerformance(

        sales_by_menu=sales_by_menu.to_dict(),

        top_products=top_products,

        product_rankings=product_rankings,

        product_contribution=product_contribution,

        total_products=df["Menu"].nunique()
    )