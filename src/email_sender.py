import os
import smtplib

from pathlib import Path
from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()

# Configuration
SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

RECIPIENT_EMAIL = "tommyju.dev@gmail.com"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

REPORT_PATH = Path("output/coffee_shop_sales_report.xlsx")


def send_email():

    msg = EmailMessage()

    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = "Weekly Coffee Shop Sales Report"

    msg.set_content(
        """
Hello,

Your weekly coffee shop sales report has been generated successfully.

The attached Excel workbook contains the latest sales analysis,
including key metrics and insights for review.

This report was automatically generated and delivered by the
Coffee Shop Sales Automation System.

Regards,
Automation System
        """
    )

    # Attach Excel report
    with open(REPORT_PATH, "rb") as file:
        report_data = file.read()

    msg.add_attachment(
        report_data,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=REPORT_PATH.name
    )

    with smtplib.SMTP_SSL(
        SMTP_SERVER,
        SMTP_PORT
    ) as smtp:

        smtp.login(
            SENDER_EMAIL,
            EMAIL_PASSWORD
        )

        smtp.send_message(msg)

    print("Report email sent successfully!")