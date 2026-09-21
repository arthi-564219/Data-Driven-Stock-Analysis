import pandas as pd

# Input file
input_file = "data/csv_files/stock.csv"

# Read stock data
df = pd.read_csv(input_file)

# Convert columns
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Stock", "Date", "Close"])

# Sort data
df = df.sort_values(["Stock", "Date"])

# Get first and last closing price for each stock
summary = df.groupby("Stock").agg(
    First_Close=("Close", "first"),
    Last_Close=("Close", "last")
).reset_index()

# Calculate return
summary["Yearly_Return_%"] = (
    (summary["Last_Close"] - summary["First_Close"])
    / summary["First_Close"]
) * 100

# Round return
summary["Yearly_Return_%"] = summary["Yearly_Return_%"].round(2)

# Top 10 gainers
top_gainers = summary.sort_values(
    "Yearly_Return_%",
    ascending=False
).head(10)

# Top 10 losers
top_losers = summary.sort_values(
    "Yearly_Return_%",
    ascending=True
).head(10)

# Save files
top_gainers.to_csv(
    "data/csv_files/top_10_gainers.csv",
    index=False
)

top_losers.to_csv(
    "data/csv_files/top_10_losers.csv",
    index=False
)

# Display results
print("\n========== TOP 10 GAINERS ==========")
print(top_gainers.to_string(index=False))

print("\n========== TOP 10 LOSERS ==========")
print(top_losers.to_string(index=False))

print("\n====================================")
print("Top gainers and losers files created successfully!")
print("====================================")