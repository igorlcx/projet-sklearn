import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

nasdaq = yf.download('^IXIC', start='2020-01-01', end='2025-01-01')
nasdaq.head()
print(nasdaq.head())

# Télécharger les données pour Apple, Google, Meta et Nvidia
stocks_data = yf.download(['AAPL', 'GOOGL', 'META'], start='2020-01-01', end='2025-01-01')

# Extraire les données de clôture
stocks = stocks_data['Close']
stocks.columns = ['Apple', 'Google', 'Meta']

# Ajouter le NASDAQ
stocks['NASDAQ'] = nasdaq['Close']
norme = stocks.iloc[0]  # Première ligne 
stocks_normalized = stocks / norme
print(stocks_normalized.head())

# Tracer tous les stocks sur le même graphe
stocks_normalized.plot(figsize=(12, 6))
plt.title('Stocks + NASDAQ (2020-2025)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

