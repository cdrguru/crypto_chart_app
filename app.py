# app.py
"""
This is the main script to run the Crypto Chart Visualization with Interpretation App.

The app performs the following tasks:
1. Retrieves historical financial data using the data_retrieval module.
2. Visualizes the retrieved data using the visualization module.
3. Simulates trades based on the data using the trading module.
4. Starts real-time updates using the real_time_updates module.
5. Analyzes the simulated trades using the gpt_analysis module.

The main function orchestrates these tasks and prints the results of the GPT-4o analysis.
"""

import logging
import os
from dotenv import load_dotenv
from data_retrieval import get_historical_data
from visualization import plot_data
from trading import simulate_trades
from real_time_updates import start_updates
from gpt_analysis import analyze_trades

# Load environment variables
load_dotenv()

def main():
    """
    The main function of the crypto chart app.

    This function retrieves historical data for a given symbol and timeframe,
    visualizes the data, simulates trades, starts real-time updates, analyzes
    the simulated trades using GPT-4o, and prints the analysis result.

    Raises:
        Exception: If an error occurs during the execution of any step.
    """
    try:
        # Step 1: Retrieve historical data
        symbol = 'BTC-USD'  # Example symbol for Bitcoin
        timeframe = 'D'  # Daily timeframe
        data = get_historical_data(symbol, timeframe)
        logging.info("Historical data retrieved successfully.")

        # Step 2: Visualize the retrieved data
        plot_data(data)
        logging.info("Data visualization completed.")

        # Step 3: Simulate trades
        trades = simulate_trades(data)
        logging.info("Trades simulated successfully.")

        # Step 4: Start real-time updates (placeholder)
        start_updates()
        logging.info("Real-time updates started.")

        # Step 5: Analyze the simulated trades using GPT-4o
        analysis_result = analyze_trades(trades)
        logging.info("Trades analyzed successfully.")

        # Print the results of the analysis
        print("GPT-4o Analysis Result:")
        print(analysis_result)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
