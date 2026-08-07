from openpyxl import Workbook
from pathlib import Path
from .dashboard import create_dashboard_sheet
from .formatting import format_workbook
from . product import create_product_sheet
from .promotion import create_promotion_sheet
from .trends import create_trends_sheet



OUTPUT_DIR = Path("output")
FILE_NAME = "coffee_shop_sales_report.xlsx"

def create_excel_report(
    report,
    filename=FILE_NAME
):
    
    output_dir = Path("output")

    # Create output folder if missing
    output_dir.mkdir(
        exist_ok=True
    )

    filepath = output_dir / filename
    wb = Workbook()


    create_dashboard_sheet(
        wb,
        report
    )

    create_product_sheet(
        wb,
        report
    )

    create_trends_sheet(
        wb,
        report
    )

    create_promotion_sheet(
        wb,
        report
    )


    format_workbook(wb)

    wb.save(filepath)

    print(
        f"Report saved to {filepath}"
    )