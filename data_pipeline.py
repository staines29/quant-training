import numpy as np
import pandas as pd
df = pd.read_csv('aapl_dirty.csv')
print(df.info())
df_clean = df.ffill()
print(df_clean.info())
print(df_clean.head(7))
df_clean['Daily_Return'] = df_clean['Close'].pct_change()
print(df_clean[['Date', 'Close', 'Daily_Return']].head(7))