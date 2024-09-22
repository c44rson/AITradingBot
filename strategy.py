class Strategy:
    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window
        self.prices = []

    def add_price(self, price):
        self.prices.append(price)
        if len(self.prices) > self.long_window:
            self.prices.pop(0)
    
    def generate_signal(self):
        if len(self.prices) < self.long_window:
            return None 

        short_ma = sum(self.prices[-self.short_window:]) / self.short_window
        long_ma = sum(self.prices[-self.long_window:]) / self.long_window

        if short_ma > long_ma:
            return "BUY"
        elif short_ma < long_ma:
            return "SELL"
        return None
