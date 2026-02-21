#!/usr/bin/env python3

from utils.cars import load_sales_data, summarize_sales, build_table
from reports.pdf import generate_pdf
from emailer.sender import build_email, send_email


def main():
    data = load_sales_data("data/car_sales.json")
    summary = summarize_sales(data)

    summary_html = "<br/>".join(summary)
    table = build_table(data)

    pdf_path = "output/car_sales_report.pdf"
    title = "Monthly Car Sales Summary"

    generate_pdf(pdf_path, title, summary_html, table)

    email = build_email(
        sender="automation@example.com",
        recipient="manager@example.com",
        subject=title,
        body="\n".join(summary),
        attachment_path=pdf_path
    )

    send_email(email)


if __name__ == "__main__":
    main()
