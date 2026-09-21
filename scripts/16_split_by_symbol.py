import pandas as pd
import os

# Input file
input_file = "data/csv_files/stock.csv"

# Output folder
output_folder = "data/csv_files/nifty_50"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read stock data
df = pd.read_csv(input_file)

# Remove invalid Stock values
df = df.dropna(subset=["Stock"])

# Get unique stock symbols
stocks = df["Stock"].unique()

print("\n========== SPLITTING STOCK DATA ==========")
print(f"Total unique stocks: {len(stocks)}")

# Create one CSV for each stock
for stock in stocks:

    stock_data = df[df["Stock"] == stock].copy()

    output_file = os.path.join(
        output_folder,
        f"{stock}.csv"
    )

    stock_data.to_csv(
        output_file,
        index=False
    )

    print(f"Created: {stock}.csv")

print("\n==========================================")
print("Symbol-wise CSV creation completed successfully!")
print(f"Total CSV files created: {len(stocks)}")
print(f"Saved inside: {output_folder}")
print("==========================================")