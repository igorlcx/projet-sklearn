import pandas as pd
import yfinance as yf

nasdaq = yf.download('^IXIC', start='2020-01-01', end='2025-01-01')
nasdaq.head()
print(nasdaq.head())

nasdaq['Close'].plot(figsize=(12, 6))
plt.title('NASDAQ Index (2020-2025)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()