from src.data_loader import load_sales
from src.cleaner import clean_sales
from src.analysis.sales_analysis import analyze_sales
from src.create_excel_report.excel_report import create_excel_report
from src.email_sender import send_email


def main():
    data = load_sales()
    clean_sales(data)
    sales_report = analyze_sales(data)
    create_excel_report(sales_report)
    send_email()
    
    
if __name__ == "__main__":
    main()