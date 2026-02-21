#!/usr/bin/env python3
"""
PDF report generator using ReportLab.
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


def generate_pdf(path, title, summary_html, table_data):
    """Generate a PDF report."""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(path, pagesize=letter)

    elements = [
        Paragraph(title, styles["h1"]),
        Spacer(1, 20),
        Paragraph(summary_html, styles["BodyText"]),
        Spacer(1, 20),
        Table(table_data)
    ]

    report.build(elements)
