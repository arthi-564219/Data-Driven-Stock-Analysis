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

# Sort data
df = df.sort_values(["Stock", "Date"])

# Calculate daily return
df["Daily_Return"] = df.groupby("Stock")["Close"].pct_change()

# Calculate cumulative return
df["Cumulative_Return"] = (
    df.groupby("Stock")["Daily_Return"]
    .transform(lambda x: (1 + x.fillna(0)).cumprod() - 1)
)

# Get final cumulative return for each stock
final_returns = (
    df.groupby("Stock")["Cumulative_Return"]
    .last()
    .reset_index()
)

# Sort by cumulative return
top_5_stocks = final_returns.sort_values(
    "Cumulative_Return",
    ascending=False
).head(5)

# Get names of top 5 stocks
top_5_names = top_5_stocks["Stock"].tolist()

# Filter data for top 5 stocks
top_5_data = df[df["Stock"].isin(top_5_names)].copy()

# Convert cumulative return to percentage
top_5_data["Cumulative_Return_%"] = (
    top_5_data["Cumulative_Return"] * 100
).round(2)

# Select required columns
output = top_5_data[
    ["Date", "Stock", "Cumulative_Return_%"]
]

# Sort output
output = output.sort_values(["Date", "Stock"])

# Save output
output_file = "data/csv_files/top_5_cumulative_returns.csv"

output.to_csv(
    output_file,
    index=False
)

# Display final top 5
print("\n========== TOP 5 PERFORMING STOCKS ==========")

display_top5 = top_5_stocks.copy()
display_top5["Cumulative_Return_%"] = (
    display_top5["Cumulative_Return"] * 100
).round(2)

display_top5 = display_top5[
    ["Stock", "Cumulative_Return_%"]
]

print(display_top5.to_string(index=False))

print("\n==============================================")
print("Cumulative return analysis completed successfully!")
print(f"Saved at: {output_file}")
print("==============================================")