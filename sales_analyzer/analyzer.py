import pandas as pd


class SalesAnalyzer:
    """Analyze sales data and generate business insights."""

    def __init__(self, df):

        self.df = df.copy()

    def calculate_basic_stats(self):
        """Calculate basic sales statistics."""

        stats = {

            "total_sales":
                self.df["total_amount"].sum(),

            "average_order_value":
                self.df["total_amount"].mean(),

            "total_orders":
                self.df["order_id"].nunique(),

            "unique_customers":
                self.df["customer_id"].nunique(),

            "unique_products":
                self.df["product_id"].nunique(),

            "total_quantity":
                self.df["quantity"].sum()
        }

        return stats

    def sales_by_category(self):
        """Analyze sales by category."""

        category_sales = (

            self.df
            .groupby("category")
            .agg(

                total_sales=(
                    "total_amount",
                    "sum"
                ),

                total_quantity=(
                    "quantity",
                    "sum"
                ),

                order_count=(
                    "order_id",
                    "nunique"
                )
            )
            .sort_values(
                "total_sales",
                ascending=False
            )
        )

        return category_sales

    def top_products(self, n=5):
        """Find top selling products."""

        products = (

            self.df
            .groupby(
                [
                    "product_id",
                    "product_name"
                ]
            )
            .agg(

                total_sales=(
                    "total_amount",
                    "sum"
                ),

                quantity_sold=(
                    "quantity",
                    "sum"
                )
            )
            .sort_values(
                "total_sales",
                ascending=False
            )
            .head(n)
        )

        return products

    def monthly_sales(self):
        """Analyze monthly sales."""

        data = self.df.copy()

        data["month"] = (
            data["order_date"]
            .dt
            .to_period("M")
        )

        monthly_sales = (

            data
            .groupby("month")
            .agg(

                total_sales=(
                    "total_amount",
                    "sum"
                ),

                total_quantity=(
                    "quantity",
                    "sum"
                ),

                unique_customers=(
                    "customer_id",
                    "nunique"
                ),

                order_count=(
                    "order_id",
                    "nunique"
                )
            )
            .sort_index()
        )

        monthly_sales["growth_rate"] = (

            monthly_sales["total_sales"]
            .pct_change()
            * 100
        )

        return monthly_sales

    def sales_by_city(self):
        """Analyze sales by city."""

        city_sales = (

            self.df
            .groupby("city")
            .agg(

                total_sales=(
                    "total_amount",
                    "sum"
                ),

                order_count=(
                    "order_id",
                    "nunique"
                )
            )
            .sort_values(
                "total_sales",
                ascending=False
            )
        )

        return city_sales

    def customer_analysis(self):
        """Analyze customer purchase patterns."""

        customer_data = (

            self.df
            .groupby("customer_id")
            .agg(

                total_sales=(
                    "total_amount",
                    "sum"
                ),

                order_count=(
                    "order_id",
                    "nunique"
                ),

                total_quantity=(
                    "quantity",
                    "sum"
                )
            )
            .sort_values(
                "total_sales",
                ascending=False
            )
        )

        return customer_data

    def peak_sales_period(self):
        """Find highest sales month."""

        monthly_data = self.monthly_sales()

        peak_month = (
            monthly_data["total_sales"]
            .idxmax()
        )

        peak_sales = (
            monthly_data["total_sales"]
            .max()
        )

        return peak_month, peak_sales
        