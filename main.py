from dotenv import load_dotenv
from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting, BacktestingBroker
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader
import os

load_dotenv()
ALPACA_CONFIG = {
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
    "PAPER": True 
}

class BuyHold(Strategy):

    def initialize(self):
        self.sleeptime = "1D"

    def on_trading_iteration(self):
        if self.first_iteration:
            symbol = "GOOG"
            price = self.get_last_price(symbol)
            quantity = self.cash // price
            order = self.create_order(symbol, quantity, "buy")
            self.submit_order(order)

backtesting_start = datetime(2020, 11, 1)
backtesting_end = datetime(2020, 12, 31)

if __name__ == "__main__":
    trade = False
    if trade:
        broker = Alpaca(ALPACA_CONFIG)
        strategy = BuyHold(broker=broker)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()
    else:
        trader = Trader(backtest=True)
        data_source = YahooDataBacktesting(
        datetime_start=backtesting_start,
        datetime_end=backtesting_end,
        )
        broker = BacktestingBroker(data_source)
        strat = BuyHold(
        broker=broker,
        )
trader.add_strategy(strat)
trader.run_all()