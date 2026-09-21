import pandas as pd

# Input file
input_file = "data/csv_files/stock.csv"

# Read data
df = pd.read_csv(input_file)

# Convert columns
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Stock", "Date", "Close"])

# Sort by stock and date
df = df.sort_values(["Stock", "Date"])

# Calculate daily return for each stock
df["Daily_Return"] = df.groupby("Stock")["Close"].pct_change()

# Calculate volatility
volatility = df.groupby("Stock")["Daily_Return"].std().reset_index()

# Rename column
volatility.columns = ["Stock", "Volatility"]

# Convert volatility to percentage
volatility["Volatility_%"] = volatility["Volatility"] * 100

# Round values
volatility["Volatility"] = volatility["Volatility"].round(6)
volatility["Volatility_%"] = volatility["Volatility_%"].round(2)

# Sort from highest volatility
top_10_volatility = volatility.sort_values(
    "Volatility",
    ascending=False
).head(10)

# Add ranking
top_10_volatility.insert(
    0,
    "Rank",
    range(1, len(top_10_volatility) + 1)
)

# Save output
output_file = "data/csv_files/top_10_volatility.csv"

top_10_volatility.to_csv(
    output_file,
    index=False
)

# Display result
print("\n========== TOP 10 MOST VOLATILE STOCKS ==========")
print(top_10_volatility.to_string(index=False))

print("\n==================================================")
print("Top 10 volatility analysis completed successfully!")
print(f"Saved at: {output_file}")
print("==================================================")