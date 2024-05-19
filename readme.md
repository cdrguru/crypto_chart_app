# Crypto Chart Visualization with Interpretation App

This application provides real-time cryptocurrency chart visualization with simulated trading and GPT-4o analysis.

## Directory Structure

crypto_chart_app/ ├── app.py ├── data_retrieval.py ├── visualization.py ├── trading.py ├── real_time_updates.py ├── gpt_analysis.py ├── utils.py ├── requirements.txt ├── .env └── README.md

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-repo/crypto_chart_app.git
    cd crypto_chart_app
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Rename the `.env.example` file to `.env`:

        ```bash
        mv .env.example .env
        ```

    - Fill in your OpenAI API key and organization ID in the `.env` file.

5. **Run the application**:

    ```bash
    python app.py
    ```

## Files Description

- `app.py`: Main script to run the application.
- `data_retrieval.py`: Module to retrieve historical data from TradingView.
- `visualization.py`: Module to visualize data.
- `trading.py`: Module to simulate trades.
- `real_time_updates.py`: Module for real-time data updates.
- `gpt_analysis.py`: Module for screenshot and GPT analysis.
- `utils.py`: Utility functions for GPT-4o analysis.
- `requirements.txt`: List of dependencies.
- `.env`: Environment variables file (you need to provide your OpenAI API key and organization ID).
- `README.md`: This file.

## Notes

- Ensure you have valid API keys and required permissions for data access and GPT analysis.
- This application is for educational purposes and simulates trading actions. Do not use it for actual trading without proper modifications and risk assessments.