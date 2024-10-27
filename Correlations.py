from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yfinance as yf

START = datetime(2017, 1, 1)
END = datetime(2024, 9, 9)
PORTFOLIO = ['FFIDX', 'FFRHX', 'FPHAX', 'FSENX', 'FSPSX', 'FSPTX', 'FTQGX',
             'FWWFX', 'IVV']


def make_array(tickers):
    symbols = []
    for ticker in tickers:
        data = yf.download(ticker, START, END)
        data['Symbol'] = ticker
        symbols.append(data)
    df = pd.concat(symbols)
    df = df.reset_index()
    df = df[['Date', 'Close', 'Symbol']]
    df.head()
    return df


def pivot_table(df):
    df_pivot = df.pivot('Date', 'Symbol', 'Close').reset_index()
    df_pivot.head()
    return df_pivot


def correlate(pivot):
    corr_df = pivot.corr(method='pearson')
    corr_df.head().reset_index()
    corr_df.head(10)
    return corr_df


def plot_correlations(corr):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('ROTH Correlations')
    plt.show()


if __name__ == '__main__':
    array = make_array(PORTFOLIO)
    pivot_array = pivot_table(array)
    corr = correlate(pivot_array)
    plot_correlations(corr)