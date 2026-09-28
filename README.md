
# Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends

## Project Overview

Data-Driven Stock Analysis is a data analytics project focused on analyzing historical NIFTY 50 stock market data from November 2023 to November 2024.

The project uses Python, Pandas, SQL, Streamlit, and Power BI to extract, clean, transform, analyze, and visualize stock market data.

It provides insights into stock returns, market performance, volatility, cumulative returns, sector-wise performance, stock price correlations, and monthly gainers and losers.

The project combines data processing, statistical analysis, MySQL database management, and interactive dashboard development to understand historical stock market trends.

---

## Objectives

- Analyze historical NIFTY 50 stock market data.
- Extract and clean raw YAML data.
- Convert YAML data into structured CSV datasets.
- Store processed stock data in a MySQL database.
- Identify the top 10 performing stocks.
- Identify the top 10 underperforming stocks.
- Calculate market summary statistics.
- Analyze stock volatility and daily returns.
- Calculate and visualize cumulative returns.
- Analyze sector-wise stock performance.
- Calculate stock price correlations.
- Identify monthly top gainers and losers.
- Develop interactive dashboards using Streamlit and Power BI.

---

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning Library | Scikit-learn |
| Data Format | YAML, CSV |
| Database | MySQL |
| Database Connectivity | SQLAlchemy, PyMySQL |
| Interactive Dashboard | Streamlit |
| Business Intelligence | Power BI |
| Version Control | Git, GitHub |

---

## Dataset

The project uses historical NIFTY 50 stock market data for 50 stocks.

### Data Period

**November 2023 to November 2024**

### Dataset Fields

| Field | Description |
|---|---|
| Date | Stock trading date |
| Ticker | Stock symbol |
| Open | Opening price |
| High | Highest price |
| Low | Lowest price |
| Close | Closing price |
| Volume | Trading volume |
| Month | Month of trading |

The raw data is stored in YAML format and processed into structured CSV datasets for analysis and visualization.

---

## Project Workflow

```text
Raw YAML Data
      |
      v
Data Extraction
      |
      v
Data Cleaning and Transformation
      |
      v
CSV Datasets
      |
      v
MySQL Database
      |
      v
Exploratory Data Analysis
      |
      v
Statistical and Financial Analysis
      |
      +---------------------------+
      |                           |
      v                           v
Streamlit Dashboard          Power BI Dashboard
      |                           |
      v                           v
Interactive Analysis         Interactive Visualizations
```

---

## Key Analysis

### 1. Top 10 Gainers

Identifies the top 10 NIFTY 50 stocks based on yearly returns.

### 2. Top 10 Losers

Identifies the 10 stocks with the lowest yearly returns during the analysis period.

### 3. Market Summary

Provides an overview of the market using the following metrics:

- Total number of stocks
- Number of green stocks
- Number of red stocks
- Average closing price
- Average trading volume

### 4. Stock Volatility Analysis

Calculates daily stock returns and standard deviation to identify stocks with greater price fluctuations.

Daily Return:

```text
Daily Return = (Current Close - Previous Close) / Previous Close
```

Volatility is used to understand historical price variation and market risk.

### 5. Cumulative Returns

Calculates cumulative returns over time to analyze stock performance and visualize the top-performing stocks.

### 6. Sector-wise Performance

Maps NIFTY 50 stocks to their respective sectors and calculates average yearly returns for each sector.

### 7. Stock Price Correlation

Calculates correlations between stock prices using Pandas and visualizes relationships through a correlation heatmap and correlation matrix.

### 8. Monthly Gainers and Losers

Identifies the top 5 gainers and top 5 losers for each month during the analysis period.

---

## Project Structure

```text
Data-Driven-Stock-Analysis/
│
├── app.py
├── query
├── .gitignore
├── README.md
│
├── data/
│   └── csv_files/
│       ├── nifty_50/
│       ├── monthly_charts/
│       ├── market_summary.csv
│       ├── monthly_gainers_losers.csv
│       ├── sector_performance.csv
│       ├── stock_correlation.csv
│       ├── stock_return.csv
│       ├── stock_returns.csv
│       ├── stock_volatility.csv
│       ├── top_10_gainers.csv
│       ├── top_10_losers.csv
│       ├── top_10_volatility.csv
│       └── top_5_cumulative_returns.csv
│
├── scripts/
│   ├── 01_read_companies.py
│   ├── 01_yaml_to_csv.py
│   ├── 02_read_csv.py
│   ├── 02_store_to_sql.py
│   ├── 03_calculate_returns.py
│   ├── 03_market_analytics.py
│   ├── 04_moving_average.py
│   ├── 05_volatility.py
│   ├── 06_stock_summary.py
│   ├── 07_read_nifty.py
│   ├── 07_top_stocks.py
│   ├── 08_top_gainers_losers.py
│   ├── 09_market_summary.py
│   ├── 10_top_volatility.py
│   ├── 11_cumulative_return.py
│   ├── 12_sector_performance.py
│   ├── 13_stock_correlation.py
│   ├── 14_market_visualization.py
│   ├── 15_monthly_gainers_losers.py
│   ├── 16_monthly_gainers_losers_visualization.py
│   ├── 16_split_by_symbol.py
│   ├── 17_volatility_standard.py
│   └── 18_stock_return.py
│
├── yaml_files/
│   └── Monthly stock data
│
├── dashboard.png
├── cumulative_returns.png
├── monthly_gainers_losers.png
├── sector_performance.png
├── stock_correlation.png
├── stock_volatility.png
│
└── Streamlit Dashboard Screenshots
    ├── streamlit_dashboard.png
    ├── streamlit_volatility_chart.png
    ├── streamlit_volatility_table.png
    ├── streamlit_cumulative_returns_chart.png
    ├── streamlit_cumulative_returns_table.png
    ├── streamlit_sector_performance_chart.png
    ├── streamlit_sector_performance_table.png
    ├── streamlit_stock_correlation_heatmap.png
    ├── streamlit_stock_correlation_matrix.png
    ├── streamlit_monthly_gainers_losers_chart.png
    ├── streamlit_monthly_data.png
    ├── streamlit_market_overview_monthly_data.png
    └── streamlit_market_overview_sector_table.png
```

---

## Database

The processed stock market data is stored in MySQL.

| Database Property | Value |
|---|---|
| Database | `stock_analysis` |
| Main Table | `stocks` |
| Database System | MySQL |

SQLAlchemy and PyMySQL are used for database connectivity.

SQL is used to store, query, and retrieve processed stock market data for analysis and dashboard development.

---

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- MySQL Server
- Git
- Power BI Desktop (for viewing or editing the Power BI dashboard)

### Step 1: Clone the Repository

```bash
git clone https://github.com/arthi-564219/Data-Driven-Stock-Analysis.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Data-Driven-Stock-Analysis
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn pyyaml streamlit sqlalchemy pymysql
```

### Step 4: Configure MySQL

Create a MySQL database named:

```sql
CREATE DATABASE stock_analysis;
```

Configure the database connection settings in the application according to your local MySQL username, password, and database configuration.

Ensure that the required stock data is available in the database before running the dashboard.

Do not upload database passwords or other sensitive credentials to GitHub.

### Step 5: Run the Streamlit Application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

Default local address:

```text
http://localhost:8501
```

---

## Dashboard Screenshots

This project includes interactive dashboards developed using Streamlit and Power BI.

### 1. Streamlit Dashboard

The Streamlit dashboard provides interactive analysis of NIFTY 50 stock market data using Python, Pandas, and MySQL.

#### Market Overview

![Streamlit Market Overview](streamlit_dashboard.png)

#### Stock Volatility

![Streamlit Stock Volatility Chart](streamlit_volatility_chart.png)

![Streamlit Stock Volatility Table](streamlit_volatility_table.png)

#### Cumulative Returns

![Streamlit Cumulative Returns Chart](streamlit_cumulative_returns_chart.png)

![Streamlit Cumulative Returns Table](streamlit_cumulative_returns_table.png)

#### Sector Performance

![Streamlit Sector Performance Chart](streamlit_sector_performance_chart.png)

![Streamlit Sector Performance Table](streamlit_sector_performance_table.png)

#### Stock Correlation

![Streamlit Stock Correlation Heatmap](streamlit_stock_correlation_heatmap.png)

![Streamlit Stock Correlation Matrix](streamlit_stock_correlation_matrix.png)

#### Monthly Gainers and Losers

![Streamlit Monthly Gainers and Losers Chart](streamlit_monthly_gainers_losers_chart.png)

#### Monthly Data

![Streamlit Monthly Data](streamlit_monthly_data.png)

#### Market Overview - Monthly Data

![Streamlit Market Overview Monthly Data](streamlit_market_overview_monthly_data.png)

#### Market Overview - Sector Table

![Streamlit Market Overview Sector Table](streamlit_market_overview_sector_table.png)

---

### 2. Power BI Dashboard

Power BI is used to create interactive visualizations for exploring stock market performance, returns, volatility, and sector-wise trends.

#### Market Overview

![Power BI Market Overview](dashboard.png)

#### Cumulative Returns

![Power BI Cumulative Returns](cumulative_returns.png)

#### Monthly Gainers and Losers

![Power BI Monthly Gainers and Losers](monthly_gainers_losers.png)

#### Sector Performance

![Power BI Sector Performance](sector_performance.png)

#### Stock Correlation

![Power BI Stock Correlation](stock_correlation.png)

#### Stock Volatility

![Power BI Stock Volatility](stock_volatility.png)

---

## Key Project Outputs

The project generates datasets and visualizations for:

- Top 10 Gainers
- Top 10 Losers
- Market Summary
- Top 10 Volatility
- Cumulative Returns
- Sector Performance
- Stock Correlation
- Monthly Gainers and Losers
- Stock Returns
- Stock Volatility

---

## Project Results

The analysis provides insights into NIFTY 50 stock market performance during the selected period.

### Market Summary

| Metric | Result |
|---|---:|
| Total Stocks | 50 |
| Green Stocks | 38 |
| Red Stocks | 12 |
| Green Stocks Percentage | 76% |
| Red Stocks Percentage | 24% |
| Average Closing Price | 2230.16 |
| Average Trading Volume | 7,250,021.43 |

### Top Performing Stocks

The top-performing stocks based on yearly returns include:

| Rank | Stock | Yearly Return |
|---|---|---:|
| 1 | ADANIPORTS | 50.42% |
| 2 | BPCL | 41.67% |
| 3 | ONGC | 40.40% |
| 4 | TRENT | 36.84% |
| 5 | ADANIENT | 34.11% |

### Volatility Analysis

The volatility analysis identifies stocks with higher variation in daily returns and helps understand historical market risk and price movement.

The project also provides sector-wise performance, cumulative returns, and stock correlation analysis to support further exploration of historical market trends.

---

## Skills Demonstrated

- Data Collection and Extraction
- Data Cleaning and Transformation
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Financial Data Analysis
- Python Programming
- Pandas and NumPy
- Data Visualization
- SQL and MySQL Database Management
- Streamlit Dashboard Development
- Power BI Dashboard Development
- Git and GitHub Version Control

---

## Author

Aarthi R

B.Sc. Computer Science

GitHub: [arthi-564219](https://github.com/arthi-564219)

---

## GitHub Repository

[Data-Driven-Stock-Analysis](https://github.com/arthi-564219/Data-Driven-Stock-Analysis)
