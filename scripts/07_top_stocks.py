import pandas as pd

# Input file
file_path = "data/csv_files/stock.csv"

# Read stock data
df = pd.read_csv(file_path)

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Sort data
df = df.sort_values(["Stock", "Date"])

# Calculate first and last close for each stock
stock_returns = (
    df.groupby("Stock")
    .agg(
        First_Close=("Close", "first"),
        Last_Close=("Close", "last")
    )
    .reset_index()
)

# Calculate yearly return
stock_returns["Yearly_Return_%"] = (
    (stock_returns["Last_Close"] - stock_returns["First_Close"])
    / stock_returns["First_Close"]
) * 100

# Round values
stock_returns["First_Close"] = stock_returns["First_Close"].round(2)
stock_returns["Last_Close"] = stock_returns["Last_Close"].round(2)
stock_returns["Yearly_Return_%"] = stock_returns["Yearly_Return_%"].round(2)

# Top 10 Green Stocks
top_green = stock_returns.sort_values(
    "Yearly_Return_%",
    ascending=False
).head(10)

# Top 10 Loss Stocks
top_loss = stock_returns.sort_values(
    "Yearly_Return_%",
    ascending=True
).head(10)

print("\n========== TOP 10 GREEN STOCKS ==========\n")
print(top_green.to_string(index=False))

print("\n========== TOP 10 LOSS STOCKS ==========\n")
print(top_loss.to_string(index=False))

# Save results
top_green.to_csv(
    "data/csv_files/top_10_gainers.csv",
    index=False
)

top_loss.to_csv(
    "data/csv_files/top_10_losers.csv",
    index=False
)

print("\nResults saved successfully!")
print("Saved: data/csv_files/top_10_gainers.csv")
print("Saved: data/csv_files/top_10_losers.csv")