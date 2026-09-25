import pandas as pd


def clean_sales_data(df):
    """Clean sales dataset."""

    if df.empty:
        return df

    cleaned_df = df.copy()

    print("\nStarting Data Cleaning...")

    # Remove duplicate rows
    initial_rows = len(cleaned_df)

    cleaned_df = cleaned_df.drop_duplicates()

    removed_duplicates = initial_rows - len(cleaned_df)

    print(f"Duplicate rows removed: {removed_duplicates}")

    # Convert order_date to datetime
    cleaned_df["order_date"] = pd.to_datetime(
        cleaned_df["order_date"],
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "quantity",
        "unit_price",
        "total_amount"
    ]

    for column in numeric_columns:

        cleaned_df[column] = pd.to_numeric(
            cleaned_df[column],
            errors="coerce"
        )

        if cleaned_df[column].isnull().any():

            median_value = cleaned_df[column].median()

            cleaned_df[column] = cleaned_df[column].fillna(
                median_value
            )

    # Handle categorical missing values
    categorical_columns = [
        "customer_id",
        "product_id",
        "product_name",
        "category",
        "city"
    ]

    for column in categorical_columns:

        if cleaned_df[column].isnull().any():

            mode_value = cleaned_df[column].mode()[0]

            cleaned_df[column] = cleaned_df[column].fillna(
                mode_value
            )

    # Recalculate total amount
    cleaned_df["total_amount"] = (
        cleaned_df["quantity"] *
        cleaned_df["unit_price"]
    )

    # Remove invalid dates
    cleaned_df = cleaned_df.dropna(
        subset=["order_date"]
    )

    # Sort by date
    cleaned_df = cleaned_df.sort_values(
        "order_date"
    )

    # Reset index
    cleaned_df = cleaned_df.reset_index(
        drop=True
    )

    print("Data cleaning completed.")

    return cleaned_df


def save_cleaned_data(df, output_path):
    """Save cleaned data."""

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Cleaned data saved to: {output_path}"
    )
    