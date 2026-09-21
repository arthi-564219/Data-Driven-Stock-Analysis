import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# INPUT FILE
# ==========================================

input_file = "data/csv_files/stock.csv"


# ==========================================
# OUTPUT FILES
# ==========================================

csv_output = "data/csv_files/stock_correlation.csv"

image_output = "data/csv_files/stock_correlation_heatmap.png"


# ==========================================
# READ DATA
# ==========================================

df = pd.read_csv(input_file)


# ==========================================
# CHECK REQUIRED COLUMNS
# ==========================================

required_columns = [
    "Stock",
    "Date",
    "Close"
]

for column in required_columns:

    if column not in df.columns:

        raise ValueError(
            f"stock.csv must contain '{column}' column"
        )


# ==========================================
# CONVERT COLUMNS
# ==========================================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Close"] = pd.to_numeric(
    df["Close"],
    errors="coerce"
)


# ==========================================
# REMOVE INVALID DATA
# ==========================================

df = df.dropna(
    subset=[
        "Stock",
        "Date",
        "Close"
    ]
)


# ==========================================
# ONE-YEAR DATA RANGE
# ==========================================

start_date = df["Date"].min()
end_date = df["Date"].max()

print("\n========== CORRELATION PERIOD ==========")

print(
    f"Start Date : {start_date}"
)

print(
    f"End Date   : {end_date}"
)

print(
    f"Total Days : "
    f"{df['Date'].nunique()}"
)


# ==========================================
# SORT DATA
# ==========================================

df = df.sort_values(
    ["Stock", "Date"]
)


# ==========================================
# CALCULATE DAILY RETURN
# ==========================================

df["Daily_Return"] = (
    df.groupby("Stock")["Close"]
    .pct_change()
)


# ==========================================
# REMOVE INVALID RETURNS
# ==========================================

df = df.dropna(
    subset=["Daily_Return"]
)


# ==========================================
# CREATE RETURN TABLE
# ==========================================

returns_df = df.pivot(
    index="Date",
    columns="Stock",
    values="Daily_Return"
)


# ==========================================
# CALCULATE CORRELATION MATRIX
# ==========================================

correlation_matrix = (
    returns_df.corr()
)


# ==========================================
# ROUND FOR DISPLAY
# ==========================================

display_matrix = (
    correlation_matrix.round(2)
)


# ==========================================
# SAVE CORRELATION MATRIX
# ==========================================

correlation_matrix.to_csv(
    csv_output
)


# ==========================================
# CREATE HEATMAP
# ==========================================

plt.figure(
    figsize=(18, 14)
)


plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    interpolation="nearest",
    aspect="auto"
)


# ==========================================
# COLOR BAR
# ==========================================

plt.colorbar(
    label="Correlation"
)


# ==========================================
# STOCK SYMBOLS
# ==========================================

plt.xticks(
    range(
        len(correlation_matrix.columns)
    ),
    correlation_matrix.columns,
    rotation=90,
    fontsize=7
)


plt.yticks(
    range(
        len(correlation_matrix.index)
    ),
    correlation_matrix.index,
    fontsize=7
)


# ==========================================
# TITLE
# ==========================================

plt.title(
    "NIFTY 50 Stock Daily Return Correlation Heatmap"
)


# ==========================================
# SAVE HEATMAP
# ==========================================

plt.tight_layout()


plt.savefig(
    image_output,
    dpi=300,
    bbox_inches="tight"
)


plt.close()


# ==========================================
# DISPLAY RESULT
# ==========================================

print(
    "\n========== STOCK CORRELATION =========="
)

print(
    display_matrix.to_string()
)


# ==========================================
# FINAL INFORMATION
# ==========================================

print(
    "\n========================================"
)

print(
    "Correlation analysis completed successfully!"
)

print(
    f"Total Stocks : "
    f"{len(correlation_matrix.columns)}"
)

print(
    f"Correlation CSV : "
    f"{csv_output}"
)

print(
    f"Heatmap Image    : "
    f"{image_output}"
)

print(
    "========================================"
)