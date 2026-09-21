import pandas as pd

# Input file
input_file = "data/csv_files/stock.csv"

# Read data
df = pd.read_csv(input_file)

# Convert numeric columns
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Stock", "Close", "Volume"])

# Sort by stock and date
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Stock", "Date"])

# Calculate first and last close for each stock
stock_summary = df.groupby("Stock").agg(
    First_Close=("Close", "first"),
    Last_Close=("Close", "last")
).reset_index()

# Calculate yearly return
stock_summary["Yearly_Return_%"] = (
    (stock_summary["Last_Close"] - stock_summary["First_Close"])
    / stock_summary["First_Close"]
) * 100

# Green and red stocks
green_stocks = stock_summary[
    stock_summary["Yearly_Return_%"] > 0
]

red_stocks = stock_summary[
    stock_summary["Yearly_Return_%"] < 0
]

# Market metrics
total_stocks = stock_summary["Stock"].nunique()
green_count = len(green_stocks)
red_count = len(red_stocks)

average_price = df["Close"].mean()
average_volume = df["Volume"].mean()

# Green and red percentages
green_percentage = (green_count / total_stocks) * 100
red_percentage = (red_count / total_stocks) * 100

# Create market summary dataframe
market_summary = pd.DataFrame({
    "Metric": [
        "Total Stocks",
        "Green Stocks",
        "Red Stocks",
        "Green Stocks %",
        "Red Stocks %",
        "Average Close Price",
        "Average Volume"
    ],
    "Value": [
        total_stocks,
        green_count,
        red_count,
        round(green_percentage, 2),
        round(red_percentage, 2),
        round(average_price, 2),
        round(average_volume, 2)
    ]
})

# Save summary
output_file = "data/csv_files/market_summary.csv"
market_summary.to_csv(output_file, index=False)

# Display results
print("\n========== MARKET SUMMARY ==========")
print(market_summary.to_string(index=False))

print("\n====================================")
print("Market summary created successfully!")
print(f"Saved at: {output_file}")
print("====================================")