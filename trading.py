"""
This module simulates trading strategies based on historical financial data.

Functions:
- simulate_trades(data: pd.DataFrame) -> list:
    Simulates trades based on the provided data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the historical financial data with date as the index.

    Returns:
    - list: A list of dictionaries representing the simulated trades.
"""

import pandas as pd
import logging

def simulate_trades(data: pd.DataFrame) -> list:
    """
    Simulates trades based on the provided data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the historical financial data with date as the index.

    Returns:
    - list: A list of dictionaries representing the simulated trades.
    """
    trades = []
    position = None  # None means no position, 'long' means holding the asset
    buy_price = 0.0

    try:
        for i in range(1, len(data)):
            # Example simple strategy: Buy when price increases by 1% from the previous day's close, sell when it decreases by 1%
            previous_close = data['Close'].iloc[i - 1]
            current_close = data['Close'].iloc[i]

            # Buy signal
            if position is None and current_close > previous_close * 1.01:
                position = 'long'
                buy_price = current_close
                trades.append({
                    'type': 'buy',
                    'price': current_close,
                    'date': data.index[i]
                })
                logging.info(f"Buy at {current_close} on {data.index[i]}")

            # Sell signal
            elif position == 'long' and current_close < previous_close * 0.99:
                position = None
                trades.append({
                    'type': 'sell',
                    'price': current_close,
                    'date': data.index[i],
                    'profit': current_close - buy_price
                })
                logging.info(f"Sell at {current_close} on {data.index[i]}, Profit: {current_close - buy_price}")

        logging.info("Trade simulation completed successfully.")
    except Exception as e:
        logging.error(f"Error during trade simulation: {e}")
        raise

    return trades

# Example usage (for testing purposes)
if __name__ == "__main__":
    import yfinance as yf
    symbol = 'BTC-USD'
    timeframe = '1d'
    data = yf.download(symbol, interval=timeframe)
    trades = simulate_trades(data)
    for trade in trades:
        print(trade)
