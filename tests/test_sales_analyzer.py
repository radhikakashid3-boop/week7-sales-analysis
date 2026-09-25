import unittest
import pandas as pd

from sales_analyzer.data_cleaner import clean_sales_data
from sales_analyzer.analyzer import SalesAnalyzer


class TestSalesData(unittest.TestCase):

    def setUp(self):

        self.df = pd.DataFrame({
            "order_id": [1, 2, 3],
            "customer_id": ["C001", "C002", "C001"],
            "product_id": ["P001", "P002", "P001"],
            "product_name": ["Laptop", "Mobile", "Laptop"],
            "category": ["Electronics", "Electronics", "Electronics"],
            "city": ["Pune", "Mumbai", "Pune"],
            "order_date": [
                "2024-01-01",
                "2024-01-05",
                "2024-02-01"
            ],
            "quantity": [1, 2, 1],
            "unit_price": [50000, 20000, 50000],
            "total_amount": [50000, 40000, 50000]
        })

    def test_data_cleaning(self):

        cleaned_df = clean_sales_data(self.df)

        self.assertFalse(cleaned_df.empty)
        self.assertEqual(len(cleaned_df), 3)
        self.assertTrue(
            pd.api.types.is_datetime64_any_dtype(
                cleaned_df["order_date"]
            )
        )

    def test_total_sales(self):

        cleaned_df = clean_sales_data(self.df)

        analyzer = SalesAnalyzer(cleaned_df)

        stats = analyzer.calculate_basic_stats()

        self.assertEqual(
            stats["total_sales"],
            140000
        )

    def test_total_orders(self):

        cleaned_df = clean_sales_data(self.df)

        analyzer = SalesAnalyzer(cleaned_df)

        stats = analyzer.calculate_basic_stats()

        self.assertEqual(
            stats["total_orders"],
            3
        )

    def test_unique_customers(self):

        cleaned_df = clean_sales_data(self.df)

        analyzer = SalesAnalyzer(cleaned_df)

        stats = analyzer.calculate_basic_stats()

        self.assertEqual(
            stats["unique_customers"],
            2
        )

    def test_category_analysis(self):

        cleaned_df = clean_sales_data(self.df)

        analyzer = SalesAnalyzer(cleaned_df)

        category_data = analyzer.sales_by_category()

        self.assertIn(
            "Electronics",
            category_data.index
        )

        self.assertEqual(
            category_data.loc[
                "Electronics",
                "total_sales"
            ],
            140000
        )

    def test_top_products(self):

        cleaned_df = clean_sales_data(self.df)

        analyzer = SalesAnalyzer(cleaned_df)

        products = analyzer.top_products()

        self.assertEqual(
            products.iloc[0]["total_sales"],
            100000
        )

    def test_monthly_sales(self):

        cleaned_df = clean_sales_data(self.df)

        analyzer = SalesAnalyzer(cleaned_df)

        monthly_data = analyzer.monthly_sales()

        self.assertEqual(
            len(monthly_data),
            2
        )

        self.assertEqual(
            monthly_data.iloc[0]["total_sales"],
            90000
        )


if __name__ == "__main__":
    unittest.main()
    