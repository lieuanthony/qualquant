from lumibot.brokers import Alpaca
from lumibot.traders import Trader
from strategies import ALPACA_CONFIG, StrategyA, StrategyB

def main() -> None:
    broker = Alpaca(ALPACA_CONFIG)
    strategy_a = StrategyA(broker=broker)
    strategy_b = StrategyB(broker=broker)
    trader = Trader(strategies=[strategy_a, strategy_b])
    trader.run_all()

if __name__ == "__main__":
    main()