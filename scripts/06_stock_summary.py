import pandas as pd

# CSV file path
file_path = "data/csv_files/stock.csv"

# Read CSV file
df = pd.read_csv(file_path)

print("Reading file:", file_path)

print("\nStock Summary")
print("----------------")

# Summary calculations
highest_close = df["Close"].max()
lowest_close = df["Close"].min()
average_close = df["Close"].mean()

maximum_volume = df["Volume"].max()
minimum_volume = df["Volume"].min()
average_volume = df["Volume"].mean()
total_volume = df["Volume"].sum()

# Display summary
print("Highest Close Price :", highest_close)
print("Lowest Close Price :", lowest_close)
print("Average Close Price :", round(average_close, 2))

print("Maximum Volume :", maximum_volume)
print("Minimum Volume :", minimum_volume)
print("Average Volume :", round(average_volume, 2))

print("Total Trading Volume :", total_volume)


# Create summary dataframe
summary = pd.DataFrame({
    "Metric": [
        "Highest Close Price",
        "Lowest Close Price",
        "Average Close Price",
        "Maximum Volume",
        "Minimum Volume",
        "Average Volume",
        "Total Trading Volume"
    ],
    "Value": [
        highest_close,
        lowest_close,
        round(average_close, 2),
        maximum_volume,
        minimum_volume,
        round(average_volume, 2),
        total_volume
    ]
})


# Save summary CSV
summary.to_csv(
    "data/csv_files/stock_summary.csv",
    index=False
)

print("\nSummary saved successfully!")
print("Saved: data/csv_files/stock_summary.csv")
