from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from config import ALPACA_API_KEY, ALPACA_API_SECRET, STOCK_SYMBOL, TRADE_QUANTITY

class TradeExecutor:
    def __init__(self):
        self.client = TradingClient(ALPACA_API_KEY, ALPACA_API_SECRET, paper=True)
    
    def place_order(self, action):
        order_data = MarketOrderRequest(
            symbol=STOCK_SYMBOL,
            qty=TRADE_QUANTITY,
            side=OrderSide(action.lower()),
            time_in_force=TimeInForce.GTC
        )
        try:
            order = self.client.submit_order(order_data)
            print(f"Order placed: {TRADE_QUANTITY} shares of {STOCK_SYMBOL} - {action}")
        except Exception as e:
            print(f"Error placing order: {e}")
