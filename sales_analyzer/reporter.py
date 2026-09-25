from pathlib import Path

import pandas as pd


class SalesReporter:
    """Generate sales reports."""

    def __init__(self, report_dir):

        self.report_dir = Path(
            report_dir
        )

        self.report_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def generate_excel_report(
        self,
        stats,
        monthly_data,
        category_data,
        product_data,
        city_data,
        customer_data,
        cleaned_data
    ):
        """Generate Excel report."""

        output_path = (
            self.report_dir /
            "sales_analysis_report.xlsx"
        )

        summary = pd.DataFrame(
            [stats]
        )

        with pd.ExcelWriter(
            output_path,
            engine="openpyxl"
        ) as writer:

            summary.to_excel(
                writer,
                sheet_name="Summary",
                index=False
            )

            monthly_data.to_excel(
                writer,
                sheet_name="Monthly Trends"
            )

            category_data.to_excel(
                writer,
                sheet_name="Category Analysis"
            )

            product_data.to_excel(
                writer,
                sheet_name="Top Products"
            )

            city_data.to_excel(
                writer,
                sheet_name="City Analysis"
            )

            customer_data.head(20).to_excel(
                writer,
                sheet_name="Top Customers"
            )

            cleaned_data.to_excel(
                writer,
                sheet_name="Cleaned Data",
                index=False
            )

        print(
            f"Excel report generated: {output_path}"
        )

        return output_path

    def generate_text_report(
        self,
        stats,
        monthly_data,
        category_data,
        product_data,
        city_data,
        peak_month,
        peak_sales
    ):
        """Generate text summary report."""

        output_path = (
            self.report_dir /
            "sales_summary.txt"
        )

        best_category = (
            category_data.index[0]
        )

        if not product_data.empty:

            best_product = (
                product_data.index[0][1]
            )

        else:

            best_product = "N/A"

        best_city = city_data.index[0]

        report = f"""
SALES DATA ANALYSIS REPORT
==========================

BASIC STATISTICS
----------------
Total Sales: {stats["total_sales"]:.2f}
Average Order Value: {stats["average_order_value"]:.2f}
Total Orders: {stats["total_orders"]}
Unique Customers: {stats["unique_customers"]}
Unique Products: {stats["unique_products"]}
Total Quantity Sold: {stats["total_quantity"]}

TOP PRODUCT CATEGORY
--------------------
{best_category}: {category_data.iloc[0]["total_sales"]:.2f}

TOP PRODUCT
-----------
{best_product}

PEAK SALES MONTH
----------------
{peak_month}: {peak_sales:.2f}

TOP CITY
--------
{best_city}: {city_data.iloc[0]["total_sales"]:.2f}

MONTHLY SALES
-------------
{monthly_data.to_string()}

TOP PRODUCTS
------------
{product_data.to_string()}
"""

        output_path.write_text(
            report.strip(),
            encoding="utf-8"
        )

        print(
            f"Text report generated: {output_path}"
        )

        return output_path
        