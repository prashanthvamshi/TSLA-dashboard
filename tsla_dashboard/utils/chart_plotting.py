import plotly.graph_objects as go
import pandas as pd

def create_candlestick_chart(df, animate=False):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df['timestamp'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Price'
    ))

    # Support Band
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['support_min'],
        mode='lines',
        line=dict(width=0),
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['support_max'],
        mode='lines',
        fill='tonexty',
        fillcolor='rgba(0,255,0,0.2)',
        line=dict(width=0),
        name='Support Band'
    ))

    # Resistance Band
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['resistance_min'],
        mode='lines',
        line=dict(width=0),
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['resistance_max'],
        mode='lines',
        fill='tonexty',
        fillcolor='rgba(255,0,0,0.2)',
        line=dict(width=0),
        name='Resistance Band'
    ))

    # Direction Markers
    for _, row in df.iterrows():
        if row['direction'] == 'LONG':
            fig.add_annotation(x=row['timestamp'], y=row['low'] * 0.98, text="🡅", font=dict(color="green", size=15), showarrow=False)
        elif row['direction'] == 'SHORT':
            fig.add_annotation(x=row['timestamp'], y=row['high'] * 1.02, text="🡇", font=dict(color="red", size=15), showarrow=False)
        elif pd.isna(row['direction']):
            fig.add_annotation(x=row['timestamp'], y=row['close'], text="●", font=dict(color="yellow", size=10), showarrow=False)

    fig.update_layout(
        title='TSLA Stock Price with Support/Resistance Bands',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        height=700
    )

    return fig
