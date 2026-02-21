#!/usr/bin/env python3
"""
Utilities for loading and analyzing car sales data.
"""

import json
import locale
from collections import defaultdict


def load_sales_data(path):
    """Load JSON sales data from disk."""
    with open(path) as f:
        return json.load(f)


def format_car(car):
    """Return a human-readable car name."""
    return f"{car['car_make']} {car['car_model']} ({car['car_year']})"


def summarize_sales(data):
    """
    Analyze sales data and return a list of summary strings.
    """
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    max_revenue_item = None
    max_sales_item = None
    year_totals = defaultdict(int)

    for item in data:
        price = locale.atof(item["price"].strip("$"))
        revenue = item["total_sales"] * price

        if not max_revenue_item or revenue > max_revenue_item["revenue"]:
            item["revenue"] = revenue
            max_revenue_item = item

        if not max_sales_item or item["total_sales"] > max_sales_item["total_sales"]:
            max_sales_item = item

        year_totals[item["car"]["car_year"]] += item["total_sales"]

    most_popular_year = max(year_totals.items(), key=lambda x: x[1])

    return [
        f"The {format_car(max_revenue_item['car'])} generated the most revenue: ${max_revenue_item['revenue']:.2f}",
        f"The {format_car(max_sales_item['car'])} had the most sales: {max_sales_item['total_sales']}",
        f"The most popular year was {most_popular_year[0]} with {most_popular_year[1]} sales."
    ]


def build_table(data):
    """Convert car data into a table for PDF output."""
    table = [["ID", "Car", "Price", "Total Sales"]]
    for item in data:
        table.append([
            item["id"],
            format_car(item["car"]),
            item["price"],
            item["total_sales"]
        ])
    return table
