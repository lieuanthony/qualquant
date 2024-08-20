from lumibot.brokers import Alpaca
from lumibot.traders import Trader
from strategy import ALPACA_CONFIG, StrategyA

def main() -> None:
    broker = Alpaca(ALPACA_CONFIG)
    strategy_a = StrategyA(broker=broker)
    trader = Trader(strategies=[strategy_a])
    trader.run_all()

if __name__ == "__main__":
    main()