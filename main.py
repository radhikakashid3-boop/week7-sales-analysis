from pathlib import Path

from sales_analyzer.data_loader import (
    load_sales_data,
    explore_data
)

from sales_analyzer.data_cleaner import (
    clean_sales_data,
    save_cleaned_data
)

from sales_analyzer.analyzer import (
    SalesAnalyzer
)

from sales_analyzer.visualizer import (
    SalesVisualizer
)

from sales_analyzer.reporter import (
    SalesReporter
)


BASE_DIR = Path(
    __file__
).resolve().parent

RAW_DATA = (
    BASE_DIR /
    "data" /
    "raw" /
    "sales_data.csv"
)

PROCESSED_DATA = (
    BASE_DIR /
    "data" /
    "processed" /
    "cleaned_sales_data.csv"
)

REPORT_DIR = (
    BASE_DIR /
    "data" /
    "reports"
)


def main():

    print("=" * 60)

    print(
        "SALES DATA ANALYSIS DASHBOARD"
    )

    print("=" * 60)

    # Load data

    df = load_sales_data(
        RAW_DATA
    )

    if df.empty:

        print(
            "Unable to continue because dataset is empty."
        )

        return

    # Explore data

    explore_data(df)

    # Clean data

    cleaned_df = clean_sales_data(
        df
    )

    save_cleaned_data(
        cleaned_df,
        PROCESSED_DATA
    )

    # Create analyzer

    analyzer = SalesAnalyzer(
        cleaned_df
    )

    # Basic statistics

    stats = (
        analyzer.calculate_basic_stats()
    )

    # Category analysis

    category_data = (
        analyzer.sales_by_category()
    )

    # Top products

    product_data = (
        analyzer.top_products()
    )

    # Monthly analysis

    monthly_data = (
        analyzer.monthly_sales()
    )

    # City analysis

    city_data = (
        analyzer.sales_by_city()
    )

    # Customer analysis

    customer_data = (
        analyzer.customer_analysis()
    )

    # Peak sales

    peak_month, peak_sales = (
        analyzer.peak_sales_period()
    )

    print("\n")
    print("=" * 60)

    print(
        "BASIC STATISTICS"
    )

    print("=" * 60)

    for key, value in stats.items():

        if isinstance(
            value,
            float
        ):

            print(
                f"{key}: {value:.2f}"
            )

        else:

            print(
                f"{key}: {value}"
            )

    print("\n")
    print(
        "SALES BY CATEGORY"
    )

    print(
        category_data
    )

    print("\n")
    print(
        "TOP PRODUCTS"
    )

    print(
        product_data
    )

    print("\n")
    print(
        "MONTHLY SALES"
    )

    print(
        monthly_data
    )

    print("\n")
    print(
        "SALES BY CITY"
    )

    print(
        city_data
    )

    print("\n")
    print(
        "PEAK SALES PERIOD"
    )

    print(
        f"{peak_month}: {peak_sales:.2f}"
    )

    # Visualization

    visualizer = SalesVisualizer(
        REPORT_DIR /
        "charts"
    )

    visualizer.monthly_sales_chart(
        monthly_data
    )

    visualizer.category_sales_chart(
        category_data
    )

    visualizer.category_pie_chart(
        category_data
    )

    visualizer.city_sales_chart(
        city_data
    )

    visualizer.order_distribution(
        cleaned_df
    )

    # Reporting

    reporter = SalesReporter(
        REPORT_DIR
    )

    excel_path = (
        reporter.generate_excel_report(
            stats,
            monthly_data,
            category_data,
            product_data,
            city_data,
            customer_data,
            cleaned_df
        )
    )

    text_path = (
        reporter.generate_text_report(
            stats,
            monthly_data,
            category_data,
            product_data,
            city_data,
            peak_month,
            peak_sales
        )
    )

    print("\n")
    print("=" * 60)

    print(
        "PROJECT COMPLETED SUCCESSFULLY"
    )

    print("=" * 60)

    print(
        f"Excel Report: {excel_path}"
    )

    print(
        f"Text Report: {text_path}"
    )

    print(
        f"Charts: {REPORT_DIR / 'charts'}"
    )


if __name__ == "__main__":
    main()
    