from alpaca.trading.client import TradingClient
from config import ALPACA_API_KEY, ALPACA_API_SECRET

def get_parsed_account_info():
    client = TradingClient(ALPACA_API_KEY, ALPACA_API_SECRET, paper=True)

    account = client.get_account()

    print(f"Account Number: {account.account_number}")
    print(f"Status: {account.status}")
    print(f"Currency: {account.currency}")
    print(f"Cash Balance: {account.cash}")
    print(f"Buying Power: {account.buying_power}")
    print(f"Day Trading Buying Power: {account.daytrading_buying_power}")
    print(f"Portfolio Value: {account.portfolio_value}")
    print(f"Equity: {account.equity}")
    print(f"Shorting Enabled: {account.shorting_enabled}")
    print(f"Pattern Day Trader: {account.pattern_day_trader}")
    print(f"Trading Blocked: {account.trading_blocked}")
    print(f"Transfers Blocked: {account.transfers_blocked}")
    print(f"Options Trading Level: {account.options_trading_level}")
    print(f"Account Created At: {account.created_at}")

if __name__ == "__main__":
    get_parsed_account_info()
