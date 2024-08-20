from dotenv import load_dotenv
from lumibot.strategies import Strategy
import math
import numpy as np
import os
import pandas as pd

load_dotenv()
ALPACA_CONFIG = {
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
    "PAPER": True 
}

def round_up_or_down(value: float) -> int:
    result: int = math.floor(value)
    
    if value - math.floor(value) >= 0.5:
        result = math.ceil(value)

    return result

class StrategyA(Strategy):

    def initialize(self):
        signal = None
        self.signal = signal
        self.sleeptime = "1D"

    def on_trading_iteration(self):
        with open("file_a.txt", "r") as file:
            line_count: int = sum(1 for _ in file)
            for line in file:
                symbol: str = line.strip()
                price: float = self.get_last_price(symbol)

                bars = self.get_historical_prices(symbol, 22, "day")
                df = bars.df

                df["9-day"] = df["close"].rolling(9).mean()
                df["21-day"] = df["close"].rolling(21).mean()
                df["Signal"] = np.where(np.logical_and(df["9-day"] > df["21-day"],
                                                        df["9-day"].shift(1) < df["21-day"].shift(1)),
                                                        "BUY", None)
                df["Signal"] = np.where(np.logical_and(df["9-day"] < df["21-day"],
                                                        df["9-day"].shift(1) > df["21-day"].shift(1)),
                                                        "SELL", df["Signal"])
                self.signal = df.iloc[-1]["Signal"]

                buying_power: float = (self.get_portfolio_value() + self.get_cash()) * 0.75
                dollar_risk_per_trade: float = (buying_power / line_count) * 0.01
                dollar_risk_per_share: float = price * 0.01
                quantity: int = round_up_or_down(dollar_risk_per_trade / dollar_risk_per_share)

                if self.signal == "BUY":
                    position = self.get_position(symbol)

                    if position is not None:
                        order = self.get_selling_order(position)
                        self.submit_order(order)

                    order = self.create_order(symbol, quantity, "buy")
                    self.submit_order(order)

                elif self.signal == "SELL":
                    position = self.get_position(symbol)

                    if position is not None:
                        order = self.get_selling_order(position)
                        self.submit_order(order)

                    order = self.create_order(symbol, quantity, "sell_short")
                    self.submit_order(order)

        with open("file_b.txt", "r") as file:
            line_count: int = sum(1 for _ in file)
            for line in file:
                symbol: str = line.strip()
                price: float = self.get_last_price(symbol)

                bars = self.get_historical_prices(symbol, 201, "day")
                df = bars.df

                df["50-day"] = df["close"].rolling(50).mean()
                df["200-day"] = df["close"].rolling(200).mean()
                df["Signal"] = np.where(np.logical_and(df["50-day"] > df["200-day"],
                                                        df["50-day"].shift(1) < df["200-day"].shift(1)),
                                                        "BUY", None)
                df["Signal"] = np.where(np.logical_and(df["50-day"] < df["200-day"],
                                                        df["50-day"].shift(1) > df["200-day"].shift(1)),
                                                        "SELL", df["Signal"])
                self.signal = df.iloc[-1]["Signal"]

                buying_power: float = (self.get_portfolio_value() + self.get_cash()) * 0.25
                dollar_risk_per_trade: float = (buying_power / line_count) * 0.01
                dollar_risk_per_share: float = price * 0.01
                quantity: int = round_up_or_down(dollar_risk_per_trade / dollar_risk_per_share)

                if self.signal == "BUY":
                    position = self.get_position(symbol)

                    if position is not None:
                        order = self.get_selling_order(position)
                        self.submit_order(order)

                    order = self.create_order(symbol, quantity, "buy")
                    self.submit_order(order)

                elif self.signal == "SELL":
                    position = self.get_position(symbol)

                    if position is not None:
                        order = self.get_selling_order(position)
                        self.submit_order(order)
