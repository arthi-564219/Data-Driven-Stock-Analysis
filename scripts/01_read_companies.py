import pandas as pd

# Load stock dataset
stock = pd.read_csv("data/csv_files/stock.csv")

# Display first 5 rows
print(stock.head())

# Display dataset information
print("\nTotal Records:", len(stock))
print("\nColumns:")
print(stock.columns)