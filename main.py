import time
from data_fetcher import DataFetcher
from strategy import Strategy
from trade_executor import TradeExecutor
from config import FETCH_INTERVAL
from account_info import get_parsed_account_info
def test_trade():
    trade_executor = TradeExecutor()

    trade_executor.place_order("BUY")

    get_parsed_account_info()

def run_trading_bot():
    data_fetcher = DataFetcher()
    strategy = Strategy()
    trade_executor = TradeExecutor()

    while True:
        stock_data = data_fetcher.fetch_stock_data()

        if stock_data:
            price = stock_data["price"]
            print(f"Latest price: {price}")
            
            strategy.add_price(price)

            signal = strategy.generate_signal()
            if signal == "BUY" or signal == "SELL":
                trade_executor.place_order(signal)

        time.sleep(FETCH_INTERVAL)

if __name__ == "__main__":
    test_trade()
