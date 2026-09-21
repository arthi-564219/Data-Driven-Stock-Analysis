import pandas as pd

# Input files
stock_file = "data/csv_files/stock.csv"
sector_file = "data/csv_files/stock_sectors.csv"

# Read files
df = pd.read_csv(stock_file)
sector_df = pd.read_csv(sector_file)

print("\nSector file columns:", sector_df.columns.tolist())


# ==========================================
# SYMBOL -> STOCK
# ==========================================

sector_df = sector_df.rename(
    columns={"Symbol": "Stock"}
)


# ==========================================
# CONVERT COLUMNS
# ==========================================

df["Date"] = pd.to_datetime(df["Date"])

df["Close"] = pd.to_numeric(
    df["Close"],
    errors="coerce"
)


# ==========================================
# REMOVE INVALID ROWS
# ==========================================

df = df.dropna(
    subset=["Stock", "Date", "Close"]
)


# ==========================================
# SORT DATA
# ==========================================

df = df.sort_values(
    ["Stock", "Date"]
)


# ==========================================
# CALCULATE YEARLY RETURN
# ==========================================

stock_returns = (
    df.groupby("Stock")
    .agg(
        First_Close=("Close", "first"),
        Last_Close=("Close", "last")
    )
    .reset_index()
)


stock_returns["Yearly_Return_%"] = (
    (
        stock_returns["Last_Close"]
        - stock_returns["First_Close"]
    )
    / stock_returns["First_Close"]
) * 100


stock_returns["Yearly_Return_%"] = (
    stock_returns["Yearly_Return_%"]
    .round(2)
)


# ==========================================
# MERGE WITH COMPANY + SECTOR DATA
# ==========================================

merged_df = stock_returns.merge(
    sector_df,
    on="Stock",
    how="left"
)


# ==========================================
# CHECK MISSING SECTORS
# ==========================================

missing_sector = merged_df[
    merged_df["Sector"].isna()
]

if not missing_sector.empty:
    print("\nWARNING: Missing sector mapping:")
    print(
        missing_sector["Stock"].tolist()
    )


# ==========================================
# SECTOR PERFORMANCE
# ==========================================

sector_performance = (
    merged_df
    .groupby("Sector")
    .agg(
        Average_Yearly_Return=(
            "Yearly_Return_%",
            "mean"
        ),
        Number_of_Stocks=(
            "Stock",
            "count"
        )
    )
    .reset_index()
)


# ==========================================
# ROUND RESULT
# ==========================================

sector_performance[
    "Average_Yearly_Return"
] = (
    sector_performance[
        "Average_Yearly_Return"
    ].round(2)
)


# ==========================================
# SORT
# ==========================================

sector_performance = (
    sector_performance
    .sort_values(
        "Average_Yearly_Return",
        ascending=False
    )
)


# ==========================================
# ADD RANK
# ==========================================

sector_performance.insert(
    0,
    "Rank",
    range(
        1,
        len(sector_performance) + 1
    )
)


# ==========================================
# SAVE OUTPUT
# ==========================================

output_file = (
    "data/csv_files/"
    "sector_performance.csv"
)

sector_performance.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULT
# ==========================================

print(
    "\n========== SECTOR-WISE PERFORMANCE =========="
)

print(
    sector_performance
    .to_string(index=False)
)

print(
    "\n=============================================="
)

print(
    "Sector performance analysis "
    "completed successfully!"
)

print(
    f"Saved at: {output_file}"
)

print(
    "=============================================="
)