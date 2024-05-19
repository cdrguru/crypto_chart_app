"""
This module visualizes financial data using the matplotlib library.

Functions:
- plot_data(data: pd.DataFrame) -> None:
    Plots the closing prices of the financial data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the historical financial data with date as the index.
- plot_candlestick(data: pd.DataFrame) -> None:
    Plots a candlestick chart of the financial data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the historical financial data with date as the index.
"""

import matplotlib.pyplot as plt
import pandas as pd
import logging
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

def plot_data(data: pd.DataFrame) -> None:
    """
    Plots the closing prices of the financial data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the historical financial data with date as the index.
    """
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data['Close'], label='Closing Price')
        plt.title('Closing Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
        logging.info("Data visualization completed successfully.")
    except Exception as e:
        logging.error(f"Error during data visualization: {e}")
        raise

def plot_candlestick(data: pd.DataFrame) -> None:
    """
    Plots a candlestick chart of the financial data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the historical financial data with date as the index.
    """
    try:
        data = data[['Open', 'High', 'Low', 'Close']]
        data.reset_index(inplace=True)
        data['Date'] = data['Date'].map(mdates.date2num)

        fig, ax = plt.subplots(figsize=(10, 5))
        candlestick_ohlc(ax, data.values, width=0.6, colorup='g', colordown='r', alpha=0.8)

        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.title('Candlestick Chart')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True)
        plt.show()
        logging.info("Candlestick chart visualization completed successfully.")
    except Exception as e:
        logging.error(f"Error during candlestick chart visualization: {e}")
        raise

# Example usage (for testing purposes)
if __name__ == "__main__":
    import yfinance as yf
    symbol = 'BTC-USD'
    timeframe = '1d'
    data = yf.download(symbol, interval=timeframe)
    
    plot_data(data)
    plot_candlestick(data)
