import pandas as pd
import os

# Project folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# NIFTY 50 CSV path
nifty_file = os.path.join(BASE_DIR, "data", "NIFTY_50", "nifty_50.csv")

# Read CSV file
df = pd.read_csv(nifty_file)

# Display first 5 rows
print("NIFTY 50 Data")
print("================")
print(df.head())

# Display columns
print("\nColumns:")
print(df.columns)

# Display total rows and columns
print("\nShape:")
print(df.shape)