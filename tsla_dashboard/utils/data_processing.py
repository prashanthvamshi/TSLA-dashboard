import pandas as pd
import numpy as np
import ast

def process_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['support_min'] = df['Support'].apply(lambda x: min(ast.literal_eval(x)) if pd.notna(x) and x != '[]' else np.nan)
    df['support_max'] = df['Support'].apply(lambda x: max(ast.literal_eval(x)) if pd.notna(x) and x != '[]' else np.nan)
    df['resistance_min'] = df['Resistance'].apply(lambda x: min(ast.literal_eval(x)) if pd.notna(x) and x != '[]' else np.nan)
    df['resistance_max'] = df['Resistance'].apply(lambda x: max(ast.literal_eval(x)) if pd.notna(x) and x != '[]' else np.nan)
    df['direction'] = df['direction'].str.upper().replace({'': None})
    return df