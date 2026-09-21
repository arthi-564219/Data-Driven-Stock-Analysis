import os
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD STOCK DATA
# ============================================================

input_file = "data/csv_files/stock.csv"

df = pd.read_csv(input_file)

# Convert columns
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Stock", "Date", "Close"])

# Create Month column if it does not exist
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Sort data
df = df.sort_values(["Stock", "Month", "Date"])


# ============================================================
# 2. CALCULATE MONTHLY RETURNS
# ============================================================

monthly_returns = (
    df.groupby(["Month", "Stock"])
    .agg(
        First_Close=("Close", "first"),
        Last_Close=("Close", "last"),
        Trading_Days=("Date", "count")
    )
    .reset_index()
)

# Keep months having at least 2 trading days
monthly_returns = monthly_returns[
    monthly_returns["Trading_Days"] >= 2
].copy()


# ============================================================
# 3. CALCULATE MONTHLY RETURN %
# ============================================================

monthly_returns["Monthly_Return"] = (
    (monthly_returns["Last_Close"] - monthly_returns["First_Close"])
    / monthly_returns["First_Close"]
) * 100


# ============================================================
# 4. TOP 5 GAINERS
# ============================================================

top_gainers = (
    monthly_returns
    .sort_values(
        ["Month", "Monthly_Return"],
        ascending=[True, False]
    )
    .groupby("Month")
    .head(5)
    .reset_index(drop=True)
)


# ============================================================
# 5. TOP 5 LOSERS
# ============================================================

top_losers = (
    monthly_returns
    .sort_values(
        ["Month", "Monthly_Return"],
        ascending=[True, True]
    )
    .groupby("Month")
    .head(5)
    .reset_index(drop=True)
)


# ============================================================
# 6. CREATE OUTPUT FOLDER
# ============================================================

output_folder = "data/csv_files"

os.makedirs(output_folder, exist_ok=True)


# ============================================================
# 7. SAVE CSV FILES
# ============================================================

gainer_csv = f"{output_folder}/monthly_top_5_gainers.csv"
loser_csv = f"{output_folder}/monthly_top_5_losers.csv"

top_gainers.to_csv(gainer_csv, index=False)
top_losers.to_csv(loser_csv, index=False)


# ============================================================
# 8. CREATE CHART FOLDER
# ============================================================

chart_folder = f"{output_folder}/monthly_charts"

os.makedirs(chart_folder, exist_ok=True)


# ============================================================
# 9. GET MONTHS
# ============================================================

months = sorted(monthly_returns["Month"].unique())

print("\n========== MONTHLY ANALYSIS ==========")
print(f"Total Months : {len(months)}")


# ============================================================
# 10. CREATE CHARTS
# ============================================================

for month in months:

    # Get current month's gainers
    gainers = top_gainers[
        top_gainers["Month"] == month
    ].sort_values(
        "Monthly_Return",
        ascending=True
    )

    # Get current month's losers
    losers = top_losers[
        top_losers["Month"] == month
    ].sort_values(
        "Monthly_Return",
        ascending=True
    )

    # Create figure with 2 charts
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(16, 6)
    )


    # --------------------------------------------------------
    # GAINERS CHART
    # --------------------------------------------------------

    axes[0].barh(
        gainers["Stock"],
        gainers["Monthly_Return"]
    )

    axes[0].set_title(
        f"Top 5 Gainers - {month}"
    )

    axes[0].set_xlabel(
        "Monthly Return (%)"
    )

    axes[0].set_ylabel(
        "Stock"
    )


    # --------------------------------------------------------
    # LOSERS CHART
    # --------------------------------------------------------

    axes[1].barh(
        losers["Stock"],
        losers["Monthly_Return"]
    )

    axes[1].set_title(
        f"Top 5 Losers - {month}"
    )

    axes[1].set_xlabel(
        "Monthly Return (%)"
    )

    axes[1].set_ylabel(
        "Stock"
    )


    # --------------------------------------------------------
    # MAIN TITLE
    # --------------------------------------------------------

    fig.suptitle(
        f"Top 5 Gainers and Losers - {month}",
        fontsize=16
    )

    plt.tight_layout()


    # --------------------------------------------------------
    # SAVE CHART
    # --------------------------------------------------------

    chart_file = (
        f"{chart_folder}/"
        f"top_5_gainers_losers_{month}.png"
    )

    plt.savefig(
        chart_file,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# 11. DISPLAY RESULTS
# ============================================================

print("\n========== TOP 5 GAINERS BY MONTH ==========")

print(
    top_gainers[
        [
            "Month",
            "Stock",
            "First_Close",
            "Last_Close",
            "Trading_Days",
            "Monthly_Return"
        ]
    ].to_string(index=False)
)


print("\n========== TOP 5 LOSERS BY MONTH ==========")

print(
    top_losers[
        [
            "Month",
            "Stock",
            "First_Close",
            "Last_Close",
            "Trading_Days",
            "Monthly_Return"
        ]
    ].to_string(index=False)
)


# ============================================================
# 12. FINAL MESSAGE
# ============================================================

print("\n==============================================")
print("Monthly Top 5 Gainers and Losers completed!")
print("==============================================")

print(f"Gainers CSV : {gainer_csv}")
print(f"Losers CSV  : {loser_csv}")
print(f"Charts Folder: {chart_folder}")

print("==============================================")