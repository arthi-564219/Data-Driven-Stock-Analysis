import pandas as pd
import os

# ==========================================
# FILE PATHS
# ==========================================

input_file = "data/csv_files/stock.csv"
output_file = "data/csv_files/volatility_standard.csv"


# ==========================================
# READ STOCK DATA
# ==========================================

df = pd.read_csv(input_file)

# Convert columns
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Stock", "Date", "Close"])

# Sort data
df = df.sort_values(["Stock", "Date"])


# ==========================================
# CALCULATE DAILY RETURN
# ==========================================

df["Daily_Return"] = (
    df.groupby("Stock")["Close"].pct_change()
)


# ==========================================
# CALCULATE STANDARD DEVIATION
# ==========================================

volatility = (
    df.groupby("Stock")["Daily_Return"]
    .std()
    .reset_index()
)

# Rename columns as required by sir
volatility.columns = ["Symbol", "Standard"]


# Round standard deviation
volatility["Standard"] = volatility["Standard"].round(6)


# Sort by Standard deviation
volatility = volatility.sort_values(
    "Standard",
    ascending=False
)


# ==========================================
# SAVE CSV
# ==========================================

volatility.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n========== VOLATILITY STANDARD DEVIATION ==========")
print(volatility.to_string(index=False))

print("\n===================================================")
print("Volatility analysis completed successfully!")
print(f"Total symbols: {len(volatility)}")
print(f"Saved at: {output_file}")
print("===================================================")