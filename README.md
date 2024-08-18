# AlgoTrader-v2

This Python-based `AlgoTrader-v2` is designed to fetch market data and execute paper trades using the Alpaca Markets API. The trading strategy, which is proprietary and hidden from public view, is designed to automatically run each day when the market opens. The project also utilizes the LumiBot API for backtesting, allowing for thorough evaluation of the strategy before deployment.

## Features

- **Automated Trading**: The bot is set to execute trades automatically at market open, using GitHub Actions to schedule the start and stop times.
- **Market Data Fetching**: Integrates with Alpaca Markets API to fetch real-time market data and execute trades based on predefined criteria.
- **Backtesting**: Utilizes the LumiBot API to backtest the strategy, ensuring it performs well under various market conditions.
- **Dockerized Deployment**: The entire project is containerized using Docker, ensuring a consistent and reliable runtime environment.

## Project Structure

- **`Dockerfile`**: Contains the instructions to build the Docker image for the project.
- **`strategy.py`**: The main script that fetches data and executes trades. The trading strategy is implemented here but is not exposed to the public.
- **`.github/workflows/start-algotrader-v2.yml`**: GitHub Actions workflow to start the bot before market open (9:25 AM EST).
- **`.github/workflows/stop-algotrader-v2.yml`**: GitHub Actions workflow to stop the bot after trades are executed (9:35 AM EST).

## Dependencies

The following key dependencies are used in this project:

- **Alpaca Markets API**: For fetching market data and executing trades.
- **LumiBot API**: For backtesting the trading strategy.
- **Docker**: To containerize the application, ensuring consistency across different environments.

## How It Works

1. **Market Data Fetching**: The bot uses the Alpaca Markets API to fetch real-time market data.
2. **Trading Execution**: Based on the proprietary strategy, the bot decides which trades to execute during market hours.
3. **Automated Scheduling**: The bot starts automatically at 9:25 AM EST and stops at 9:35 AM EST, thanks to GitHub Actions.
4. **Backtesting**: The LumiBot API allows for comprehensive backtesting of the strategy, using historical data to validate its effectiveness.

## Security

The trading strategy implemented in `strategy.py` is proprietary and hidden from the public. The repository does not expose any sensitive information or strategy details.
