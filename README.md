# 📊 Data-Driven Stock Analysis

### Organizing, Cleaning, and Visualizing Market Trends

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/arthi-564219/Data-Driven-Stock-Analysis)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Power BI](https://img.shields.io/badge/Dashboard-Power%20BI-yellow)](https://powerbi.microsoft.com/)

---

## 📌 Project Overview

Data-Driven Stock Analysis is a data analytics project that analyzes historical NIFTY 50 stock market data from November 2023 to November 2024.

The project uses Python, Pandas, NumPy, MySQL, Streamlit, and Power BI to extract, clean, process, analyze, and visualize stock market data.

### Key Features

- Top 10 stock gainers and losers
- Market overview and summary statistics
- Stock volatility analysis
- Cumulative returns analysis
- Sector-wise performance
- Stock correlation heatmap
- Monthly top 5 gainers and losers
- Interactive Streamlit and Power BI dashboards

## 🖥️ Dashboard Previews

### 1. Streamlit Dashboard

An interactive dashboard built using Python, Pandas, MySQL, and Streamlit.

#### 🏠 Market Overview

![Streamlit Dashboard](streamlit_dashboard/streamlit_dashboard.png)

![Market Overview - Monthly Data](streamlit_dashboard/streamlit_market_overview_monthly_data.png)

![Market Overview - Sector Table](streamlit_dashboard/streamlit_market_overview_sector_table.png)

#### 📉 Stock Volatility

![Stock Volatility Chart](streamlit_dashboard/streamlit_volatility_chart.png)

![Stock Volatility Table](streamlit_dashboard/streamlit_volatility_table.png)

#### 📈 Cumulative Returns

![Cumulative Returns Chart](streamlit_dashboard/streamlit_cumulative_returns_chart.png)

![Cumulative Returns Table](streamlit_dashboard/streamlit_cumulative_returns_table.png)

#### 🏢 Sector Performance

![Sector Performance Chart](streamlit_dashboard/streamlit_sector_performance_chart.png)

![Sector Performance Table](streamlit_dashboard/streamlit_sector_performance_table.png)

#### 🔗 Stock Correlation

![Stock Correlation Heatmap](streamlit_dashboard/streamlit_stock_correlation_heatmap.png)

![Stock Correlation Matrix](streamlit_dashboard/streamlit_stock_correlation_matrix.png)

#### 📅 Monthly Gainers and Losers

![Monthly Gainers and Losers](streamlit_dashboard/streamlit_monthly_gainers_losers_chart.png)

![Monthly Analysis Data](streamlit_dashboard/streamlit_monthly_data.png)

---

### 2. Power BI Dashboard

Interactive Power BI reports for stock market performance, returns, volatility, sector analysis, and stock correlations.

#### 📅 Monthly Gainers and Losers

![Power BI Monthly Gainers and Losers](powerbi_dashboard.png/monthly_gainers_losers.png)

#### 🏢 Sector Performance

![Power BI Sector Performance](powerbi_dashboard.png/sector_performance.png)

#### 📉 Stock Volatility

![Power BI Stock Volatility](powerbi_dashboard.png/stock_volatility.png)

#### 📈 Cumulative Returns

![Power BI Cumulative Returns](powerbi_dashboard.png/cumulative_returns.png)

#### 🔗 Stock Correlation

![Power BI Stock Correlation](powerbi_dashboard.png/stock_correlation.png)

---

## 🎯 Project Objectives

- Extract stock market data from YAML files.
- Clean and transform the extracted data.
- Convert YAML data into structured CSV files.
- Organize data for 50 NIFTY 50 stocks.
- Store processed data in a MySQL database.
- Calculate stock returns and market summary statistics.
- Identify top-performing and underperforming stocks.
- Analyze volatility, cumulative returns, and sector performance.
- Calculate stock correlations.
- Identify monthly gainers and losers.
- Build interactive dashboards using Streamlit and Power BI.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning Library | Scikit-learn |
| Data Extraction | PyYAML |
| Database | MySQL |
| Database Connectivity | SQLAlchemy, PyMySQL |
| Interactive Dashboard | Streamlit |
| Business Intelligence | Power BI |
| Version Control | Git, GitHub |

## 📂 Dataset

- **Market:** NIFTY 50
- **Number of stocks:** 50
- **Analysis period:** November 2023 – November 2024
- **Source:** [Project Dataset Folder](https://drive.google.com/drive/folders/1JH7DBYk1uSvkYCxoMA11EI5KM8uXJAI6?usp=sharing)

### Data Fields

- Date
- Ticker
- Open
- High
- Low
- Close
- Volume
- Month

## 🔄 Project Workflow

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
CSV Datasets for 50 Stocks
      |
      v
MySQL Database
      |
      v
Stock Market Analysis
      |
      +--------------------------+
      |                          |
      v                          v
Streamlit Dashboard         Power BI Dashboard
      |                          |
      v                          v
Interactive Analysis        Business Intelligence
```

## 📊 Key Analysis

### 1. Top 10 Gainers and Losers

Ranks stocks by yearly return to identify the strongest and weakest performers.

### 2. Market Summary

Summarizes the market using the total number of stocks, green and red stock counts, average closing price, and trading volume.

### 3. Stock Volatility

Uses daily returns and standard deviation to measure fluctuations in stock performance.

Daily return:

`(Current Close - Previous Close) / Previous Close`

### 4. Cumulative Returns

Analyzes stock performance over time and identifies the top-performing stocks across the selected period.

### 5. Sector-wise Performance

Maps stocks to their respective sectors and compares average yearly returns across sectors.

### 6. Stock Correlation

Uses Pandas correlation calculations to examine relationships between stock price movements and presents the results in a heatmap.

### 7. Monthly Gainers and Losers

Identifies the top five gainers and top five losers for each month in the dataset.

## 🗄️ Database

The project uses MySQL to store and retrieve processed stock market data.

| Component | Details |
|---|---|
| Database | `stock_analysis` |
| Main table | `stocks` |
| Connectivity | SQLAlchemy, PyMySQL |

MySQL must be installed and configured for database-connected features of the application to work.

## 📁 Project Structure

```text
Data-Driven-Stock-Analysis/
├── app.py
├── query
├── requirements.txt
├── README.md
├── .gitignore
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
│       ├── stock_sectors.csv
│       ├── stock_summary.csv
│       ├── stock_volatility.csv
│       ├── top_10_gainers.csv
│       ├── top_10_losers.csv
│       ├── top_10_volatility.csv
│       └── top_5_cumulative_returns.csv
├── powerbi_dashboard.png/
│   ├── cumulative_returns.png
│   ├── monthly_gainers_losers.png
│   ├── sector_performance.png
│   ├── stock_correlation.png
│   └── stock_volatility.png
├── streamlit_dashboard/
│   ├── streamlit_dashboard.png
│   ├── streamlit_market_overview_monthly_data.png
│   ├── streamlit_market_overview_sector_table.png
│   ├── streamlit_volatility_chart.png
│   ├── streamlit_volatility_table.png
│   ├── streamlit_cumulative_returns_chart.png
│   ├── streamlit_cumulative_returns_table.png
│   ├── streamlit_sector_performance_chart.png
│   ├── streamlit_sector_performance_table.png
│   ├── streamlit_stock_correlation_heatmap.png
│   ├── streamlit_stock_correlation_matrix.png
│   ├── streamlit_monthly_gainers_losers_chart.png
│   └── streamlit_monthly_data.png
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
└── yaml_files/
    └── Monthly stock data
```

*Note: This structure summarizes the project. Keep the README file paths aligned with the actual files in your repository.*

## ⚙️ Installation and Setup

### Prerequisites

- Python installed
- MySQL installed and configured
- Git installed

### Step 1: Clone the Repository

```bash
git clone https://github.com/arthi-564219/Data-Driven-Stock-Analysis.git
```

### Step 2: Open the Project Folder

```bash
cd Data-Driven-Stock-Analysis
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal. It is usually:

`http://localhost:8501`

**Note:** Configure the MySQL connection settings required by `app.py` before running database-dependent features.

## 📦 Key Project Outputs

- Stock-wise CSV datasets
- Market summary
- Top 10 gainers and losers
- Stock volatility results
- Cumulative returns
- Sector performance
- Stock correlation matrix and heatmap
- Monthly gainers and losers
- Streamlit dashboard
- Power BI dashboard screenshots

## 🎓 Skills Demonstrated

- Python programming
- Data extraction and cleaning
- Data transformation
- Exploratory data analysis
- Financial data analysis
- Statistical analysis
- Data visualization
- SQL and MySQL database management
- Dashboard development
- Streamlit
- Power BI
- Git and GitHub

## 📌 Project Deliverables

- Processed stock market datasets
- Python analysis scripts
- MySQL database integration
- Streamlit dashboard
- Power BI dashboard
- Project documentation
- Public GitHub repository

## 💼 Business Use Cases

- Compare stock performance over a selected period.
- Review market-level statistics.
- Identify high-volatility stocks.
- Compare sector performance.
- Explore relationships between stock movements.
- Review monthly gainers and losers.

## 👤 Author

**Aarthi R**

B.Sc. Computer Science

[GitHub Repository](https://github.com/arthi-564219/Data-Driven-Stock-Analysis)

## ⚠️ Disclaimer

This project is developed for educational and data analytics purposes. Historical stock market analysis is not financial or investment advice.

