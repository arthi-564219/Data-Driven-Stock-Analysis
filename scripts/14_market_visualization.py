import pandas as pd
import matplotlib.pyplot as plt
import os

# Project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSV folder
CSV_DIR = os.path.join(BASE_DIR, "data", "csv_files")


# ==========================================
# FUNCTION: FIND NUMERIC PERFORMANCE COLUMN
# ==========================================

def find_value_column(df, exclude_columns):
    for col in df.columns:
        if col not in exclude_columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                return col

    raise ValueError("No numeric value column found!")


# ==========================================
# 1. TOP 10 GAINERS
# ==========================================

gainers_file = os.path.join(CSV_DIR, "top_10_gainers.csv")
gainers = pd.read_csv(gainers_file)

print("\nGainers columns:", gainers.columns.tolist())

gainer_value = find_value_column(gainers, ["Stock"])

plt.figure(figsize=(10, 6))
plt.bar(gainers["Stock"], gainers[gainer_value])
plt.title("Top 10 Gainers")
plt.xlabel("Stock")
plt.ylabel(gainer_value)
plt.xticks(rotation=45)
plt.tight_layout()

gainers_chart = os.path.join(CSV_DIR, "top_10_gainers.png")
plt.savefig(gainers_chart)
plt.close()


# ==========================================
# 2. TOP 10 LOSERS
# ==========================================

losers_file = os.path.join(CSV_DIR, "top_10_losers.csv")
losers = pd.read_csv(losers_file)

print("Losers columns:", losers.columns.tolist())

loser_value = find_value_column(losers, ["Stock"])

plt.figure(figsize=(10, 6))
plt.bar(losers["Stock"], losers[loser_value])
plt.title("Top 10 Losers")
plt.xlabel("Stock")
plt.ylabel(loser_value)
plt.xticks(rotation=45)
plt.tight_layout()

losers_chart = os.path.join(CSV_DIR, "top_10_losers.png")
plt.savefig(losers_chart)
plt.close()


# ==========================================
# 3. TOP 10 VOLATILITY
# ==========================================

volatility_file = os.path.join(CSV_DIR, "top_10_volatility.csv")
volatility = pd.read_csv(volatility_file)

print("Volatility columns:", volatility.columns.tolist())

volatility_value = find_value_column(
    volatility,
    ["Stock", "Rank"]
)

plt.figure(figsize=(10, 6))
plt.bar(volatility["Stock"], volatility[volatility_value])
plt.title("Top 10 Most Volatile Stocks")
plt.xlabel("Stock")
plt.ylabel(volatility_value)
plt.xticks(rotation=45)
plt.tight_layout()

volatility_chart = os.path.join(CSV_DIR, "top_10_volatility.png")
plt.savefig(volatility_chart)
plt.close()


# ==========================================
# 4. SECTOR PERFORMANCE
# ==========================================

sector_file = os.path.join(CSV_DIR, "sector_performance.csv")
sector = pd.read_csv(sector_file)

print("Sector columns:", sector.columns.tolist())

sector_value = find_value_column(
    sector,
    ["Sector", "Rank", "Number_of_Stocks"]
)

plt.figure(figsize=(12, 7))
plt.barh(sector["Sector"], sector[sector_value])
plt.title("Sector-wise Stock Performance")
plt.xlabel(sector_value)
plt.ylabel("Sector")
plt.tight_layout()

sector_chart = os.path.join(CSV_DIR, "sector_performance.png")
plt.savefig(sector_chart)
plt.close()


# ==========================================
# 5. TOP 5 CUMULATIVE RETURN
# ==========================================

cumulative_file = os.path.join(
    CSV_DIR,
    "top_5_cumulative_returns.csv"
)

cumulative = pd.read_csv(cumulative_file)

print("Cumulative return columns:", cumulative.columns.tolist())

# Convert Date column
cumulative["Date"] = pd.to_datetime(cumulative["Date"])

# Sort by Date
cumulative = cumulative.sort_values(
    ["Date", "Stock"]
)

# Create line chart
plt.figure(figsize=(12, 7))

for stock in cumulative["Stock"].unique():

    stock_data = cumulative[
        cumulative["Stock"] == stock
    ]

    plt.plot(
        stock_data["Date"],
        stock_data["Cumulative_Return_%"],
        label=stock
    )

plt.title("Cumulative Return - Top 5 Performing Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Return (%)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

cumulative_chart = os.path.join(
    CSV_DIR,
    "top_5_cumulative_returns.png"
)

plt.savefig(
    cumulative_chart,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# FINAL MESSAGE
# ==========================================

print("\n========================================")
print("Market visualization completed successfully!")
print("Saved files:")
print("1. data/csv_files/top_10_gainers.png")
print("2. data/csv_files/top_10_losers.png")
print("3. data/csv_files/top_10_volatility.png")
print("4. data/csv_files/sector_performance.png")
print("5. data/csv_files/top_5_cumulative_returns.png")
print("========================================")

