from lumibot.brokers import Alpaca
from lumibot.traders import Trader
from strategy import ALPACA_CONFIG, MyStrategy

def main() -> None:
    broker = Alpaca(ALPACA_CONFIG)
    strategy = MyStrategy(broker=broker)
    trader = Trader()
    trader.add_strategy(strategy)
    trader.run_all()

if __name__ == "__main__":
    main()