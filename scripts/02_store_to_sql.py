import os
import pandas as pd
from sqlalchemy import create_engine, URL


# ============================================================
# 1. MySQL DATABASE CONNECTION
# ============================================================

connection_url = URL.create(
    "mysql+pymysql",
    username="root",
    password="Arthi@12465_mysql",
    host="localhost",
    port=3306,
    database="stock_analysis"
)

engine = create_engine(connection_url)


# ============================================================
# 2. TEST MYSQL CONNECTION
# ============================================================

with engine.connect():
    print("MySQL database connection successful!")


# ============================================================
# 3. CSV DIRECTORY
# ============================================================

csv_dir = "data/csv_files"


# ============================================================
# 4. COMBINE MONTHLY GAINERS + LOSERS
#    Requirement 5 = ONE DATAFRAME
# ============================================================

gainers_file = os.path.join(
    csv_dir,
    "monthly_top_5_gainers.csv"
)

losers_file = os.path.join(
    csv_dir,
    "monthly_top_5_losers.csv"
)


gainers_df = pd.read_csv(gainers_file)
losers_df = pd.read_csv(losers_file)


# Add type column
gainers_df["Type"] = "Gainer"
losers_df["Type"] = "Loser"


# Combine both DataFrames
monthly_gainers_losers_df = pd.concat(
    [gainers_df, losers_df],
    ignore_index=True
)


# Save as ONE CSV
combined_file = os.path.join(
    csv_dir,
    "monthly_gainers_losers.csv"
)

monthly_gainers_losers_df.to_csv(
    combined_file,
    index=False
)


print(
    "Created monthly_gainers_losers.csv ->",
    len(monthly_gainers_losers_df),
    "rows"
)


# ============================================================
# 5. FINAL 5 CSV FILES
# ============================================================

csv_files = {
    "stock_volatility": "stock_volatility.csv",

    "top_5_cumulative_returns": "top_5_cumulative_returns.csv",

    "sector_performance": "sector_performance.csv",

    "stock_correlation": "stock_correlation.csv",

    "monthly_gainers_losers": "monthly_gainers_losers.csv"
}


# ============================================================
# 6. LOAD 5 CSV FILES INTO MYSQL
# ============================================================

print("\nStarting CSV to MySQL loading...\n")


for table_name, file_name in csv_files.items():

    file_path = os.path.join(
        csv_dir,
        file_name
    )

    # Read CSV
    df = pd.read_csv(file_path)

    # Save DataFrame into MySQL table
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    print(
        f"Loaded: {file_name} -> "
        f"{table_name} ({len(df)} rows)"
    )


# ============================================================
# 7. COMPLETION MESSAGE
# ============================================================

print("\n========================================")
print("All 5 datasets successfully loaded!")
print("========================================")