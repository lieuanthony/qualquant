from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting, BacktestingBroker
from lumibot.traders import Trader
from strategy import MyStrategy

def main() -> None:
    backtesting_start = datetime(2019, 8, 15)
    backtesting_end = datetime(2024, 8, 15)

    data_source = YahooDataBacktesting(
        datetime_start=backtesting_start,
        datetime_end=backtesting_end
    )
    broker = BacktestingBroker(data_source)
    strategy = MyStrategy(broker=broker)
    trader = Trader(backtest=True)
    trader.add_strategy(strategy)
    trader.run_all()

if __name__ == "__main__":
    main()