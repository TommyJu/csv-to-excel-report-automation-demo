import pandas as pd
from src.analysis.models.report_models import MenuPerformance


def analyze_menu(df: pd.DataFrame) -> MenuPerformance:

    sales_by_menu = (
        df.groupby("Menu")["Total_Qty"]
        .sum()
        .sort_values(ascending=False)
    )


    top_products = (
        sales_by_menu
        .head(5)
        .to_dict()
    )


    return MenuPerformance(
        sales_by_menu=sales_by_menu.to_dict(),
        top_products=top_products
    )