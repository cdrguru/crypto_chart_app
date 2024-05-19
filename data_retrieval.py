"""
This module retrieves historical financial data using the yfinance library.

Functions:
- get_historical_data(symbol: str, timeframe: str) -> pd.DataFrame:
    Retrieves historical data for a given stock symbol and timeframe.
    Supported timeframes: '5' (5 minutes), '15' (15 minutes), '60' (60 minutes), 'D' (daily).

    Args:
    - symbol (str): The stock symbol to retrieve data for (e.g., 'AAPL').
    - timeframe (str): The timeframe for the data (e.g., 'D' for daily).

    Returns:
    - pd.DataFrame: A DataFrame containing the historical data with date as the index.
"""

import yfinance as yf
import pandas as pd
import logging

def get_historical_data(symbol: str, timeframe: str) -> pd.DataFrame:
    """
    Retrieves historical data for a given stock symbol and timeframe.

    Args:
    - symbol (str): The stock symbol to retrieve data for (e.g., 'AAPL').
    - timeframe (str): The timeframe for the data (e.g., 'D' for daily).

    Returns:
    - pd.DataFrame: A DataFrame containing the historical data with date as the index.
    """
    # Map the timeframe to the yfinance interval parameter
    interval_map = {
        '5': '5m',
        '15': '15m',
        '60': '60m',
        'D': '1d'
    }
    
    if timeframe not in interval_map:
        raise ValueError("Unsupported timeframe. Use '5', '15', '60', or 'D'.")
    
    interval = interval_map[timeframe]
    
    try:
        # Download historical data using yfinance
        data = yf.download(tickers=symbol, interval=interval)
        logging.info(f"Data for {symbol} with {timeframe} timeframe retrieved successfully.")
        
        return data
    
    except Exception as e:
        logging.error(f"Error retrieving data for {symbol}: {e}")
        raise

# Example usage (for testing purposes)
if __name__ == "__main__":
    symbol = 'BTC-USD'
    timeframe = 'D'
    data = get_historical_data(symbol, timeframe)
    print(data.head())
