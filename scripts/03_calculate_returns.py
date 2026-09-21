import pandas as pd

file_path = "data/csv_files/stock.csv"

df = pd.read_csv(file_path)

# Calculate return separately for each stock
df["Daily_Return"] = df.groupby("Stock")["Close"].pct_change()

print(df.head(15))

output_file = "data/csv_files/stock_returns.csv"
df.to_csv(output_file, index=False)

print("\nDaily Return calculated successfully!")
print("Saved:", output_file)