import pandas as pd


def load_sales_data(file_path):
    """Load sales data from CSV file."""

    try:
        df = pd.read_csv(file_path)

        print(f"Data loaded successfully.")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        return df

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()

    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def explore_data(df):
    """Explore basic dataset information."""

    if df.empty:
        print("No data available.")
        return

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())
    