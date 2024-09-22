from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from config import ALPACA_API_KEY, ALPACA_API_SECRET, STOCK_SYMBOL

class DataFetcher:
    def __init__(self):
        self.client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_API_SECRET)
        self.symbol = STOCK_SYMBOL
    
    def fetch_stock_data(self):
        request_params = StockBarsRequest(
            symbol_or_symbols=self.symbol,
            timeframe=TimeFrame.Minute,
            start=datetime.now()
        )
        bars = self.client.get_stock_bars(request_params)
        latest_bar = bars[self.symbol][0]

        return {
            "price": latest_bar.close,
            "time": latest_bar.timestamp
        }
