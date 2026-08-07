import pandas as pd

from src.analysis.models.report_models import SalesReport

from .summary import analyze_summary
from .menu import analyze_menu
from .trends import analyze_trends
from .promotions import analyze_promotions



def analyze_sales(df: pd.DataFrame) -> SalesReport:

    return SalesReport(

        summary=analyze_summary(df),

        menu=analyze_menu(df),

        time=analyze_trends(df),

        promotions=analyze_promotions(df)

    )