import pandas as pd

# Input file
file_path = "data/csv_files/stock_returns.csv"

# Read CSV
df = pd.read_csv(file_path)

# Calculate Moving Average (5 days)
df["Moving_Average"] = (
    df.groupby("Stock")["Close"]
    .transform(lambda x: x.rolling(window=5).mean())
)

# Display output
print(df.head(15))

# Save file
output_file = "data/csv_files/stock_moving_average.csv"
df.to_csv(output_file, index=False)

print("\nMoving Average calculated successfully!")
print("Saved:", output_file)