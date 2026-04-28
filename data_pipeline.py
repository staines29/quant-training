import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = yf.download('AAPL', start='2014-01-01', end='2024-01-01') # the new data source 
#df = pd.read_csv('aapl_dirty.csv') # This was thre primary data source we used for the project.

#print(df.info())
df_clean = pd.DataFrame()
df_clean['Close'] = df['Close']
#df_clean = df.ffill()  #older data source
#print(df_clean.info())
#print(df_clean.head(7))
df_clean['Daily_Return'] = df_clean['Close'].pct_change()
#print(df_clean[['Date', 'Close', 'Daily_Return']].head(7))
df_clean['Fast_SMA'] = df_clean['Close'].rolling(window=50).mean()
#print(df_clean[['Date', 'Close', 'Fast_SMA']].head(7))
df_clean['Slow_SMA'] = df_clean['Close'].rolling(window=200).mean()
#print(df_clean[['Date', 'Close', 'Slow_SMA']].head(7)) 
df_clean['Signal'] = np.where(df_clean['Fast_SMA'] > df_clean['Slow_SMA'], 1, -1)
#print(df_clean[['Date', 'Fast_SMA', 'Slow_SMA', 'Signal']].head(7))
df_clean['Strategy_Return'] = df_clean['Daily_Return'] * df_clean['Signal'].shift(1)
#print(df_clean[['Date', 'Daily_Return', 'Signal', 'Strategy_Return']].head(7))
df_clean['Market_Growth'] = (1 + df_clean['Daily_Return']).cumprod()
df_clean['Strategy_Growth'] = (1 + df_clean['Strategy_Return']).cumprod()
#print(df_clean[['Date', 'Market_Growth', 'Strategy_Growth']].tail(5))
#df_clean.set_index('Date', inplace=True) # for the old data set which had a date column
# Market Metrics
market_return = df_clean['Daily_Return'].mean() * 252
market_volatility = df_clean['Daily_Return'].std() * np.sqrt(252)
market_sharpe = market_return / market_volatility
# Strategy Metrics
strategy_return = df_clean['Strategy_Return'].mean() * 252
strategy_volatility = df_clean['Strategy_Return'].std() * np.sqrt(252)
strategy_sharpe = strategy_return / strategy_volatility
#print 
print(f"Market Sharpe: {market_sharpe:.2f}")
print(f"Strategy Sharpe: {strategy_sharpe:.2f}")

df_clean[['Market_Growth', 'Strategy_Growth']].plot(figsize=(10, 6))
plt.title('Market Growth vs Strategy Growth')
plt.xlabel('Date')
plt.ylabel('Growth')
plt.show()