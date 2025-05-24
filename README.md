# TSLA-dashboard
📈 TSLA Stock Analysis Dashboard

This project is a Streamlit-based interactive dashboard for visualizing and analyzing Tesla (TSLA) stock market data using OHLCV (Open, High, Low, Close, Volume) format. It includes features for charting support and resistance levels, identifying market directions (LONG/SHORT), and integrates with Google’s Gemini Pro API for natural language querying and AI-assisted insights.

⸻

🔍 Features
 • 📊 Candlestick Chart with support and resistance overlays
 • 🔎 Date Filtering to focus on specific time ranges
 • 🚦 Market Sentiment Highlighting: Bullish (LONG), Bearish (SHORT), and Neutral zones
 • 🤖 Gemini Chatbot Integration: Ask questions like
 • “How many bullish days in 2023?”
 • “When was the close price above resistance?”


💡 Technologies Used
 • Python
 • Streamlit
 • Pandas
 • TradingView Lightweight Charts (via streamlit-lightweight-charts)
 • Google Gemini Pro API
 • dotenv for environment variable management
 
🚀 How to Run
 1. Clone the repository:
git clone https://github.com/prashanthvamshi/TSLA-dashboard
cd TSLA-dashboard

2. Install dependencies:
pip install -r requirements.txt

3.Add your .env file:
GEMINI_API_KEY = your_google_api_key_here

4.Run the app:
streamlit run app1.py

🧠 Sample Questions You Can Ask Gemini
 • “Show me days in 2024 when volume was above average.”
 • “How many SHORT signals were detected between Jan–June 2023?”
 • “Was there a bullish breakout in July 2022?”
