import pandas as pd
import matplotlib.pyplot as plt


# Load monthly gainers and losers
gainers_file = "data/csv_files/monthly_top_5_gainers.csv"
losers_file = "data/csv_files/monthly_top_5_losers.csv"

gainers = pd.read_csv(gainers_file)
losers = pd.read_csv(losers_file)


# Get available months
months = gainers["Month"].unique()


# Create one chart for each available month
for month in months:

    month_gainers = gainers[gainers["Month"] == month]
    month_losers = losers[losers["Month"] == month]

    # Combine gainers and losers
    combined = pd.concat(
        [month_gainers, month_losers],
        ignore_index=True
    )

    # Create bar chart
    plt.figure(figsize=(10, 6))

    plt.bar(
        combined["Stock"],
        combined["Monthly_Return"]
    )

    plt.axhline(0, linewidth=1)

    plt.title(f"Top 5 Gainers and Losers - {month}")
    plt.xlabel("Stock")
    plt.ylabel("Monthly Return (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save chart
    output_file = (
        f"data/csv_files/monthly_gainers_losers_{month}.png"
    )

    plt.savefig(output_file)
    plt.show()

    print(f"Chart saved: {output_file}")