# Data-Driven Stock Analysis 
 
## Project Overview 
 
**Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends** is a data analytics project focused on analyzing historical NIFTY 50 stock market data. 
 
The project uses Python, Pandas, SQL, Streamlit, and Power BI to clean, transform, analyze, and visualize stock market trends. 
 
The analysis covers stock returns, market performance, volatility, cumulative returns, sector performance, stock correlations, and monthly gainers and losers. 
 
--- 
 
## Objectives 
 
- Analyze historical NIFTY 50 stock data 
- Clean and organize raw YAML data 
- Convert YAML data into structured CSV datasets 
- Store processed stock data in a MySQL database 
- Identify top 10 performing stocks 
- Identify top 10 underperforming stocks 
- Calculate market summary statistics 
- Analyze stock volatility 
- Analyze cumulative returns 
- Analyze sector-wise performance 
- Analyze stock price correlations 
- Identify monthly top gainers and losers 
- Build interactive dashboards using Streamlit and Power BI 
 
--- 
 
## Technologies Used 
 
- Python 
- Pandas 
- NumPy 
- Matplotlib 
- Seaborn 
- Scikit-learn 
- PyYAML 
- MySQL 
- SQLAlchemy 
- PyMySQL 
- Streamlit 
- Power BI 
- Git 
- GitHub 
 
--- 
 
## Dataset 
 
The project uses historical NIFTY 50 stock market data. 
 
### Data Fields 
 
- Date 
- Ticker 
- Open 
- High 
- Low 
- Close 
- Volume 
- Month 
 
### Data Period 
 
**November 2023 to November 2024** 
 
The dataset contains historical data for **50 NIFTY 50 stocks**. 
 
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
Data Analysis 
      | 
      +----------------------+ 
      |                      | 
      v                      v 
Streamlit Dashboard     Power BI Dashboard


Key Analysis
1. Top 10 Gainers

Identifies the top 10 NIFTY 50 stocks based on yearly return.

2. Top 10 Losers

Identifies the 10 stocks with the lowest yearly returns.

3. Market Summary

Provides an overview of the market using:

Total number of stocks
Number of green stocks
Number of red stocks
Average closing price
Average trading volume
4. Volatility Analysis

Calculates daily returns and standard deviation to identify the most volatile stocks.

Daily return is calculated using:

Daily Return = (Current Close - Previous Close) / Previous Close
5. Cumulative Returns

Calculates cumulative returns to analyze stock performance over time and visualize the top-performing stocks.

6. Sector-wise Performance

Maps NIFTY 50 stocks to their respective sectors and calculates average yearly returns for each sector.

7. Stock Correlation

Calculates correlations between stock prices using Pandas and visualizes the relationships using a correlation heatmap.

8. Monthly Gainers and Losers

Identifies the top 5 gainers and top 5 losers for each month during the analysis period.

Project Structure
Data_Driven_Stock_Analysis/
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
└── yaml_files/
    └── monthly stock data
Database

The processed stock data is stored in MySQL.

Database
stock_analysis
Main Table
stocks

SQL is used to store, query, and retrieve processed stock market data for analysis and dashboard development.

Installation

Install the required Python libraries:

pip install pandas numpy matplotlib seaborn scikit-learn pyyaml streamlit sqlalchemy pymysql
Running the Project
Step 1: Clone the Repository
git clone https://github.com/arthi-564219/Data-Driven-Stock-Analysis.git
Step 2: Navigate to the Project
cd Data-Driven-Stock-Analysis
Step 3: Run the Streamlit Application
streamlit run app.py

The Streamlit application will open in the browser.

Dashboard
Streamlit Dashboard

The Streamlit dashboard provides interactive analysis of:

Market summary
Stock performance
Top gainers and losers
Volatility
Cumulative returns
Sector performance
Stock correlation
Monthly performance
Power BI Dashboard

Power BI is used to create interactive visualizations for:

Market overview
Stock performance
Gainers and losers
Volatility
Sector performance
Market trends
Key Project Outputs

The project generates datasets and visualizations for:

Top 10 Gainers
Top 10 Losers
Market Summary
Top 10 Volatility
Cumulative Returns
Sector Performance
Stock Correlation
Monthly Gainers and Losers
Stock Returns
Stock Volatility
Project Results

The analysis provides insights into NIFTY 50 market performance during the selected period.

Market Summary
Total Stocks: 50
Green Stocks: 38
Red Stocks: 12
Green Stocks Percentage: 76%
Red Stocks Percentage: 24%
Average Closing Price: 2230.16
Average Trading Volume: 7,250,021.43
Top Gainers

The top-performing stocks based on yearly return include:

ADANIPORTS
BPCL
ONGC
TRENT
ADANIENT
Volatility

The volatility analysis identifies stocks with higher variation in daily returns and helps understand market risk and price movement.

Skills Demonstrated
Data Collection
Data Cleaning
Data Transformation
Exploratory Data Analysis
Statistical Analysis
Financial Data Analysis
Data Visualization
SQL Database Management
Python Programming
Dashboard Development
Streamlit
Power BI
Git and GitHub

Author
arthi

B.Sc. Computer Science

GitHub Repository

https://github.com/arthi-564219/Data-Driven-Stock-Analysis
