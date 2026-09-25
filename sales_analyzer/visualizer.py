from pathlib import Path

import matplotlib.pyplot as plt


class SalesVisualizer:
    """Create sales visualizations."""

    def __init__(self, output_dir):

        self.output_dir = Path(
            output_dir
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def monthly_sales_chart(
        self,
        monthly_data
    ):
        """Create monthly sales line chart."""

        if monthly_data.empty:
            return

        plt.figure(
            figsize=(12, 6)
        )

        plt.plot(
            monthly_data.index.astype(str),
            monthly_data["total_sales"],
            marker="o"
        )

        plt.title(
            "Monthly Sales Trend"
        )

        plt.xlabel(
            "Month"
        )

        plt.ylabel(
            "Total Sales"
        )

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir /
            "monthly_sales_trend.png"
        )

        plt.close()

    def category_sales_chart(
        self,
        category_data
    ):
        """Create category sales bar chart."""

        if category_data.empty:
            return

        plt.figure(
            figsize=(10, 6)
        )

        plt.bar(
            category_data.index,
            category_data["total_sales"]
        )

        plt.title(
            "Sales by Product Category"
        )

        plt.xlabel(
            "Category"
        )

        plt.ylabel(
            "Total Sales"
        )

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir /
            "category_sales.png"
        )

        plt.close()

    def category_pie_chart(
        self,
        category_data
    ):
        """Create category sales pie chart."""

        if category_data.empty:
            return

        plt.figure(
            figsize=(8, 8)
        )

        plt.pie(
            category_data["total_sales"],
            labels=category_data.index,
            autopct="%1.1f%%"
        )

        plt.title(
            "Sales Distribution by Category"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir /
            "category_distribution.png"
        )

        plt.close()

    def city_sales_chart(
        self,
        city_data
    ):
        """Create city sales bar chart."""

        if city_data.empty:
            return

        plt.figure(
            figsize=(10, 6)
        )

        plt.bar(
            city_data.index,
            city_data["total_sales"]
        )

        plt.title(
            "Sales by City"
        )

        plt.xlabel(
            "City"
        )

        plt.ylabel(
            "Total Sales"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir /
            "city_sales.png"
        )

        plt.close()

    def order_distribution(
        self,
        df
    ):
        """Create order value distribution."""

        if df.empty:
            return

        plt.figure(
            figsize=(10, 6)
        )

        plt.hist(
            df["total_amount"],
            bins=15,
            edgecolor="black"
        )

        plt.title(
            "Order Value Distribution"
        )

        plt.xlabel(
            "Order Value"
        )

        plt.ylabel(
            "Frequency"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir /
            "order_value_distribution.png"
        )

        plt.close()
        