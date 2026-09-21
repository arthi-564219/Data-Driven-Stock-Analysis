import pandas as pd

# Input file
file_path = "data/csv_files/stock_moving_average.csv"

# Read CSV
df = pd.read_csv(file_path)

# Calculate volatility for each stock
volatility = (
    df.groupby("Stock")["Daily_Return"]
    .std()
)

print("Stock Volatility:")
print(volatility)

# Add volatility column
df["Volatility"] = df["Stock"].map(volatility)

# Save output
output_file = "data/csv_files/stock_volatility.csv"
df.to_csv(output_file, index=False)

print("\nVolatility calculated successfully!")
print("Saved:", output_file)