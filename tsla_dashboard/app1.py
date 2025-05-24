import streamlit as st
import pandas as pd
from utils.data_processing import process_data
from utils.chart_plotting import create_candlestick_chart
from utils.gemini_query import query_gemini

# Page setup
st.set_page_config(layout="wide", page_title="TSLA Stock Analysis Dashboard")

# Load data
df = pd.read_csv("tsla_dashboard/Data/TSLA_data.csv")
df = process_data(df)

# Tabs
tab1, tab2 = st.tabs(["📊 Visualization", "🤖 Chat with Gemini"])

with tab1:
    st.title("TSLA Stock Price Analysis")
    st.write("- please select a date range to load the chart")
    st.write("-⚠️ Higher the range you select Longer the system will take to load the chart")  

    # Date filter
    min_date = df['timestamp'].min().date()
    max_date = df['timestamp'].max().date()
    start_date, end_date = st.date_input("Select date range:", (min_date, max_date), min_value=min_date, max_value=max_date)

    filtered_df = df[(df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)]

    # Plot chart
    st.plotly_chart(create_candlestick_chart(filtered_df, animate=False), use_container_width=True)

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Days", len(filtered_df))
    col1.metric("Bullish Days", len(filtered_df[filtered_df['direction'] == 'LONG']))
    col2.metric("Bearish Days", len(filtered_df[filtered_df['direction'] == 'SHORT']))
    col2.metric("Neutral Days", len(filtered_df[filtered_df['direction'].isna()]))
    col3.metric("Average Volume", f"{filtered_df['volume'].mean():.2f}")
    col3.metric("Price Range", f"{filtered_df['low'].min():.2f} - {filtered_df['high'].max():.2f}")

with tab2:
    st.title("Ask Gemini About TSLA 📈")
    st.write("Try these example questions:")
    st.write("- How many days in 2023 was TSLA bullish ?")
    st.write("- what was the highest resistance level in Q1 2024 ?")
    st.write("- Show me days when the close price was above the resistance band.")
    st.write("- What percentage of days had a LONG direction ?")
    question = st.text_input("Ask your question about TSLA stock data:")
    if question:
        with st.spinner("Gemini is thinking..."):
            try:
                response = query_gemini(question, df)
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
