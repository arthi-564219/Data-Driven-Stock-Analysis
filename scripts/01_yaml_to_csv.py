import os
import glob
import yaml
import pandas as pd


# YAML source folder
raw_data_dir = r"C:\Users\SATHYA COMPUTERS\Downloads\data (1)"

# CSV output folder
output_dir = r"data\csv_files"


def extract_yaml_to_stock_csv(raw_data_dir, output_dir):

    all_records = []

    # Only 2023-11 to 2024-11
    months = pd.date_range(
        start="2023-11-01",
        end="2024-11-01",
        freq="MS"
    ).strftime("%Y-%m").tolist()

    print("Starting YAML processing...\n")

    for month in months:

        month_folder = os.path.join(raw_data_dir, month)

        yaml_files = glob.glob(
            os.path.join(month_folder, "*.yaml")
        )

        print(f"{month}: {len(yaml_files)} YAML files")

        for file_path in yaml_files:

            with open(file_path, "r", encoding="utf-8") as file:
                day_data = yaml.safe_load(file)

            if not day_data:
                continue

            for record in day_data:

                all_records.append({
                    "Stock": record.get("Ticker"),
                    "Close": record.get("close"),
                    "Date": record.get("date"),
                    "High": record.get("high"),
                    "Low": record.get("low"),
                    "Month": record.get("month"),
                    "Open": record.get("open"),
                    "Volume": record.get("volume")
                })

    # Create ONE DataFrame
    df = pd.DataFrame(all_records)

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Convert numeric columns
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Sort
    df = df.sort_values(
        ["Date", "Stock"]
    ).reset_index(drop=True)

    # Create output folder
    os.makedirs(output_dir, exist_ok=True)

    # Save ONE CSV
    output_file = os.path.join(
        output_dir,
        "stock.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print("\n================================")
    print("SUCCESS")
    print("================================")
    print("DataFrame shape:", df.shape)
    print("Number of stocks:", df["Stock"].nunique())
    print("Start date:", df["Date"].min())
    print("End date:", df["Date"].max())
    print("CSV created:", output_file)

    print("\nFirst 5 rows:")
    print(df.head())


# Run function
extract_yaml_to_stock_csv(
    raw_data_dir,
    output_dir
)

