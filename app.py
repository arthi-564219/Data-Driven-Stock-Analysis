import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine, URL

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Nifty 50 Stock Analysis",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# MYSQL CONNECTION
# =========================================================
@st.cache_resource
def init_connection():

    connection_url = URL.create(
        "mysql+pymysql",
        username="root",
        password="Arthi@12465_mysql",   
        host="localhost",
        port=3306,
        database="stock_analysis"
    )

    return create_engine(connection_url)


# Test MySQL connection
try:

    engine = init_connection()

    with engine.connect():
        pass

except Exception as e:

    st.error("❌ MySQL Connection Failed")
    st.error(e)
    st.stop()


# =========================================================
# HELPER FUNCTION
# =========================================================
def load_table(table_name):

    try:

        return pd.read_sql(
            f"SELECT * FROM `{table_name}`",
            engine
        )

    except Exception as e:

        st.error(f"❌ Error loading {table_name}")
        st.error(e)

        return pd.DataFrame()


# =========================================================
# TITLE
# =========================================================
st.title("📊 Nifty 50 Stock Analysis Dashboard")

st.success("✅ MySQL Database Connected Successfully")

st.markdown(
    "Data-Driven Stock Analysis using Python, MySQL, Pandas and Streamlit."
)

st.markdown("---")


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("📌 Analysis")

option = st.sidebar.radio(
    "Select Analysis",
    [
        "📊 Market Overview",
        "📈 Stock Volatility",
        "📉 Cumulative Returns",
        "🏢 Sector Performance",
        "🔗 Stock Correlation",
        "📅 Monthly Gainers & Losers"
    ]
)


# =========================================================
# 1. MARKET OVERVIEW
# =========================================================
if option == "📊 Market Overview":

    st.header("📊 Market Overview")

    volatility_df = load_table("stock_volatility")
    sector_df = load_table("sector_performance")
    monthly_df = load_table("monthly_gainers_losers")

    # KPI calculations
    total_stocks = volatility_df["Stock"].nunique()

    avg_close = volatility_df["Close"].mean()

    total_volume = volatility_df["Volume"].sum()

    total_records = len(volatility_df)

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Stocks",
        total_stocks
    )

    col2.metric(
        "Average Close",
        f"{avg_close:,.2f}"
    )

    col3.metric(
        "Total Records",
        f"{total_records:,}"
    )

    col4.metric(
        "Total Volume",
        f"{total_volume:,.0f}"
    )

    st.markdown("---")

    # Sector summary
    st.subheader("🏢 Sector Performance")

    if not sector_df.empty:

        st.dataframe(
            sector_df,
            use_container_width=True
        )

    # Monthly summary
    st.subheader("📅 Monthly Gainers & Losers")

    if not monthly_df.empty:

        st.dataframe(
            monthly_df,
            use_container_width=True
        )


# =========================================================
# 2. STOCK VOLATILITY
# =========================================================
elif option == "📈 Stock Volatility":

    st.header("📈 Top 10 Most Volatile Stocks")

    df = load_table("stock_volatility")

    if not df.empty:

        # Find maximum volatility for each stock
        volatility = (
            df.groupby("Stock")["Volatility"]
            .max()
            .reset_index()
        )

        volatility = volatility.sort_values(
            "Volatility",
            ascending=False
        ).head(10)

        # Chart
        fig = px.bar(
            volatility,
            x="Stock",
            y="Volatility",
            title="Top 10 Most Volatile Nifty 50 Stocks",
            labels={
                "Stock": "Stock Ticker",
                "Volatility": "Volatility"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("📋 Volatility Data")

        st.dataframe(
            volatility,
            use_container_width=True
        )


# =========================================================
# 3. CUMULATIVE RETURNS
# =========================================================
elif option == "📉 Cumulative Returns":

    st.header("📉 Top 5 Performing Stocks")

    df = load_table("top_5_cumulative_returns")

    if not df.empty:

        df["Date"] = pd.to_datetime(df["Date"])

        # Find the 5 stocks having highest final cumulative return
        latest = (
            df.sort_values("Date")
            .groupby("Stock")
            .tail(1)
            .sort_values(
                "Cumulative_Return_%",
                ascending=False
            )
            .head(5)
        )

        top_stocks = latest["Stock"].tolist()

        chart_df = df[
            df["Stock"].isin(top_stocks)
        ]

        # Line chart
        fig = px.line(
            chart_df,
            x="Date",
            y="Cumulative_Return_%",
            color="Stock",
            title="Cumulative Return of Top 5 Performing Stocks",
            labels={
                "Date": "Date",
                "Cumulative_Return_%": "Cumulative Return (%)",
                "Stock": "Stock"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("📋 Top 5 Final Returns")

        st.dataframe(
            latest,
            use_container_width=True
        )


# =========================================================
# 4. SECTOR PERFORMANCE
# =========================================================
elif option == "🏢 Sector Performance":

    st.header("🏢 Sector-wise Performance")

    df = load_table("sector_performance")

    if not df.empty:

        fig = px.bar(
            df,
            x="Sector",
            y="Average_Yearly_Return",
            title="Average Yearly Return by Sector",
            labels={
                "Sector": "Sector",
                "Average_Yearly_Return": "Average Yearly Return (%)"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("📋 Sector Performance Data")

        st.dataframe(
            df,
            use_container_width=True
        )


# =========================================================
# 5. STOCK CORRELATION
# =========================================================
elif option == "🔗 Stock Correlation":

    st.header("🔗 Stock Price Correlation")

    df = load_table("stock_correlation")

    if not df.empty:

        # First column contains stock names
        correlation_matrix = df.set_index("Stock")

        fig = px.imshow(
            correlation_matrix,
            title="Nifty 50 Stock Correlation Heatmap",
            labels={
                "color": "Correlation"
            },
            aspect="auto"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("📋 Correlation Matrix")

        st.dataframe(
            correlation_matrix,
            use_container_width=True
        )


# =========================================================
# 6. MONTHLY GAINERS & LOSERS
# =========================================================
elif option == "📅 Monthly Gainers & Losers":

    st.header("📅 Monthly Top Gainers & Losers")

    df = load_table("monthly_gainers_losers")

    if not df.empty:

        # Show available months
        months = df["Month"].unique()

        selected_month = st.selectbox(
            "Select Month",
            months
        )

        filtered = df[
            df["Month"] == selected_month
        ]

        # Sort by return
        filtered = filtered.sort_values(
            "Monthly_Return",
            ascending=False
        )

        # Chart
        fig = px.bar(
            filtered,
            x="Stock",
            y="Monthly_Return",
            title=f"Top Gainers & Losers - {selected_month}",
            labels={
                "Stock": "Stock",
                "Monthly_Return": "Monthly Return (%)"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("📋 Monthly Data")

        st.dataframe(
            filtered,
            use_container_width=True
        )


# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.caption(
    "Data-Driven Stock Analysis • Python • Pandas • MySQL • Streamlit"
)