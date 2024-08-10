import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.stream import TradingStream
import config

def create_tickers() -> dict[yf.Ticker]:
    tickers: dict[yf.Ticker] = dict()

    with open("tickers.txt") as file:
        for line in file:
            ticker: yf.Ticker = yf.Ticker(line)
            tickers[line] = ticker

    return tickers

def main() -> None:
    client: TradingClient = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
    account = dict(client.get_account())

if __name__ == "__main__":
    main()