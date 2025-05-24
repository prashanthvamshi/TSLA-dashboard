import google.generativeai as genai
import os
import pandas as pd

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def query_gemini(question, df):
    # Convert 'timestamp' to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Optional: Filter only relevant year
    df_filtered = df[df['timestamp'].dt.year == 2023]

    # Optional: Drop unused columns to keep prompt size small
    df_small = df_filtered[['timestamp', 'close', 'Support', 'Resistance', 'direction']].copy()

    # Convert to text Gemini can understand
    sample_data = df_small.head(50).to_csv(index=False)
    df = pd.read_csv('Data\TSLA_data.csv')
    csv_text = df.to_string()

    # Build prompt
    context = f"""Analyze this data:
    {csv_text}


Now answer this question:
{question}
"""

    # Send to Gemini
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(context)
    return response.text