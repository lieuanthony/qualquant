from dotenv import load_dotenv
from lumibot.strategies import Strategy
import numpy as np
import os
import pandas as pd

load_dotenv()
ALPACA_CONFIG = {
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
    "PAPER": True 
}

class MyStrategy(Strategy):

    def initialize(self):
        signal = None
        self.signal = signal
        self.sleeptime = "1D"

    def on_trading_iteration(self):
        with open("file.txt") as file:
            for line in file:
                symbol: str = line.strip()

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

                quantity: int = self.get_cash() // (self.get_last_price(symbol) * 5)

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