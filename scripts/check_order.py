import pandas as pd

df = pd.read_csv("data/csv_files/stock.csv")

df["Date"] = pd.to_datetime(df["Date"])

print(df["Date"].is_monotonic_increasing)
