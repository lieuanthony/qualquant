from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.data import StockHistoricalDataClient, StocksTradeRequest
from datetime import datetime
import config

def main() -> None:
    client: TradingClient = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)


if __name__ == "__main__":
    main()