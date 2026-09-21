import pandas as pd
import os

# ==========================================
# FILE PATHS
# ==========================================

input_file = "data/csv_files/stock.csv"
output_file = "data/csv_files/stock_return.csv"


# ==========================================
# READ STOCK DATA
# ==========================================

df = pd.read_csv(input_file)

# Convert columns
df["Date"] = pd.to_datetime(df["Date"])
df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Remove invalid rows
df = df.dropna(
    subset=["Stock", "Date", "Open", "Close"]
)

# Sort by Symbol and Date
df = df.sort_values(
    ["Stock", "Date"]
)


# ==========================================
# CALCULATE FIRST & LAST VALUES
# ==========================================

stock_return = (
    df.groupby("Stock")
    .agg(
        First_Date=("Date", "first"),
        First_Open=("Open", "first"),
        First_Close=("Close", "first"),

        Last_Date=("Date", "last"),
        Last_Open=("Open", "last"),
        Last_Close=("Close", "last")
    )
    .reset_index()
)


# ==========================================
# CALCULATE STOCK RETURN
# ==========================================

stock_return["Stock_Return_%"] = (
    (
        (stock_return["Last_Close"] -
         stock_return["First_Close"])
        / stock_return["First_Close"]
    ) * 100
).round(2)


# ==========================================
# RENAME STOCK AS SYMBOL
# ==========================================

stock_return = stock_return.rename(
    columns={
        "Stock": "Symbol"
    }
)


# ==========================================
# SELECT REQUIRED COLUMNS
# ==========================================

stock_return = stock_return[
    [
        "Symbol",
        "First_Date",
        "First_Open",
        "First_Close",
        "Last_Date",
        "Last_Open",
        "Last_Close",
        "Stock_Return_%"
    ]
]


# ==========================================
# SORT BY RETURN
# ==========================================

stock_return = stock_return.sort_values(
    "Stock_Return_%",
    ascending=False
)


# ==========================================
# SAVE CSV
# ==========================================

stock_return.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n========== STOCK RETURN ANALYSIS ==========")

print(
    stock_return.to_string(index=False)
)

print("\n===========================================")
print("Stock return analysis completed successfully!")
print(f"Total symbols: {len(stock_return)}")
print(f"Saved at: {output_file}")
print("===========================================")