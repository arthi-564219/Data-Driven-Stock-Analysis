import streamlit as st
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Nifty 50 Analytics Hub", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- Dynamic Data Processing Pipeline ---
@st.cache_data
def ingest_and_compile_metrics(csv_directory):
    """Scan localized directories, calculate statistics, and compress tables."""
    all_records = []
    if not os.path.exists(csv_directory):
        return pd.DataFrame(), pd.DataFrame()
        
    for file_name in os.listdir(csv_directory):
        if file_name.endswith('.csv'):
            ticker = file_name.replace('.csv', '')
            temp_df = pd.read_csv(os.path.join(csv_directory, file_name))
            temp_df['Symbol'] = ticker
            all_records.append(temp_df)
            
    if not all_records:
        return pd.DataFrame(), pd.DataFrame()
        
    master_df = pd.concat(all_records, ignore_index=True)
    master_df['Date'] = pd.to_datetime(master_df['Date'])
    master_df = master_df.sort_values(['Symbol', 'Date']).reset_index(drop=True)
    
    # Mathematical transformations
    master_df['Daily_Return'] = master_df.groupby('Symbol')['Close'].pct_change()
    
    # Extract structural return bounds
    returns_registry = []
    for ticker, group in master_df.groupby('Symbol'):
        sorted_grp = group.sort_values('Date')
        vola = sorted_grp['Daily_Return'].std()
        
        init_val = sorted_grp['Close'].iloc[0]
        final_val = sorted_grp['Close'].iloc[-1]
        net_change = (final_val - init_val) / init_val
        
        returns_registry.append({
            'Symbol': ticker, 
            'Total_Return': net_change, 
            'Volatility': vola
        })
        
    return master_df, pd.DataFrame(returns_registry)

# Run extraction (points to default workspace folder)
DATA_PATH = 'data/processed_csv'
timeseries_df, metrics_df = ingest_and_compile_metrics(DATA_PATH)

# Fallback block to spin mock data if folder path is unprovisioned
if metrics_df.empty:
    tickers = [f"STOCK_{i:02d}" for i in range(1, 51)]
    metrics_df = pd.DataFrame({
        'Symbol': tickers,
        'Total_Return': np.random.uniform(-0.35, 0.55, 50),
        'Volatility': np.random.uniform(0.012, 0.038, 50)
    })
    # Fabricate timeseries structural bounds
    date_rng = pd.date_range(start="2025-01-01", end="2025-12-31", freq="B")
    ts_list = []
    for t in tickers:
        base_p = np.random.uniform(100, 2000)
        p_seq = base_p * (1 + np.random.uniform(-0.02, 0.02, len(date_rng))).cumsum()
        vol_seq = np.random.randint(50000, 2000000, len(date_rng))
        ts_list.append(pd.DataFrame({'Date': date_rng, 'Symbol': t, 'Close': p_seq, 'Volume': vol_seq}))
    timeseries_df = pd.concat(ts_list)
    timeseries_df['Daily_Return'] = timeseries_df.groupby('Symbol')['Close'].pct_change()

# --- Dashboard Layout Presentation ---
st.title("📈 Stock Analytics Pipeline Visualizer")
st.markdown("---")

# Navigation Sidebar
st.sidebar.header("📁 Navigation & Filters")
app_mode = st.sidebar.selectbox("Choose View", ["Market Overview", "Volatility & Returns Matrix", "Correlation Analysis"])

if app_mode == "Market Overview":
    # Top KPI Metrics Cards
    advancing = (metrics_df['Total_Return'] >= 0).sum()
    declining = (metrics_df['Total_Return'] < 0).sum()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🟢 Green Stocks Count", f"{advancing} Assets", delta=f"{(advancing/50)*100:.1f}% Market Share")
    with col2:
        st.metric("🔴 Red Stocks Count", f"{declining} Assets", delta=f"-{(declining/50)*100:.1f}% Market Share", delta_color="inverse")
    with col3:
        st.metric("📊 Mean Transaction Volume", f"{int(timeseries_df['Volume'].mean()):,}")
    with col4:
        st.metric("💰 Average Asset Settlement", f"₹ {timeseries_df['Close'].mean():.2f}")
        
    st.markdown("### Top Performers vs Asset Liabilities")
    p1, p2 = st.columns(2)
    
    with p1:
        top_10 = metrics_df.sort_values('Total_Return', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.barplot(data=top_10, x='Total_Return', y='Symbol', palette='viridis', ax=ax)
        ax.set_title("Top 10 Green Performers (Yearly Return)")
        st.pyplot(fig)
        
    with p2:
        bottom_10 = metrics_df.sort_values('Total_Return', ascending=True).head(10)
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.barplot(data=bottom_10, x='Total_Return', y='Symbol', palette='flare', ax=ax)
        ax.set_title("Top 10 Loss Accumulators (Red)")
        st.pyplot(fig)

elif app_mode == "Volatility & Returns Matrix":
    st.markdown("### Volatility Risk Matrix Profiler")
    
    v1, v2 = st.columns([1, 2])
    with v1:
        high_vol = metrics_df.sort_values('Volatility', ascending=False).head(10)
        st.dataframe(high_vol[['Symbol', 'Volatility']].style.background_gradient(cmap='Oranges'))
        
    with v2:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(data=metrics_df, x='Volatility', y='Total_Return', size='Volatility', hue='Total_Return', palette='coolwarm', ax=ax)
        ax.axhline(0, color='grey', linestyle='--', linewidth=0.8)
        ax.set_title("Risk vs Reward Distribution Metric Mapping")
        st.pyplot(fig)

elif app_mode == "Correlation Analysis":
    st.markdown("### Close Price Correlation Vector Mapping")
    
    # Pivot datasets to construct narrow closing array for heatmaps
    pivot_df = timeseries_df.pivot(index='Date', columns='Symbol', values='Close').iloc[:, :12]
    corr_matrix = pivot_df.corr()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='mako', fmt=".2f", linewidths=.5, ax=ax)
    st.pyplot(fig)

