import os
import pandas as pd

# Project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSV folder path
csv_folder = os.path.join(BASE_DIR, "data", "csv_files")

# Read all CSV files
for file in os.listdir(csv_folder):
    if file.endswith(".csv"):

        csv_path = os.path.join(csv_folder, file)

        df = pd.read_csv(csv_path)

        print("\n====================")
        print("File :", file)
        print("====================")
        print(df)