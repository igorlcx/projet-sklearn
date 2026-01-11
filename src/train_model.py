import pandas as pd
import yfinance as yf

nasdaq = yf.download('^IXIC', start='2020-01-01', end='2025-01-01')
nasdaq.head()
print(nasdaq.head())