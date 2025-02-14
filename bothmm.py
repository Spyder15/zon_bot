import time
import ccxt
from decimal import Decimal

# Account 1 API credentials
API_KEY_1 = "00907e9d4ece06857597fcae91d54b833fd0238a8bbf56207b47f67876606629"
API_SECRET_1 = "50fc7a48ba34cca68972de37bc45ac892b3abba97e34c74b4e2167fd45b70f8f"

# Account 2 API credentials
API_KEY_2 = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
API_SECRET_2 = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

EXCHANGE = "bitrue"
PAIR = "ZON/USDT"
TRADE_AMOUNT = Decimal("5.00")  # Adjust trade size as needed
MIN_TRADE_VALUE = Decimal("1.0000")  # Bitrue's minimum order value in USDT
SLEEP_TIME = 2  # Delay between order cycles

# Initialize both exchange clients
account_1 = ccxt.bitrue({"apiKey": API_KEY_1, "secret": API_SECRET_1})
account_2 = ccxt.bitrue({"apiKey": API_KEY_2, "secret": API_SECRET_2})

def fetch_price():
    """Fetch the current market price of the asset."""
    ticker = account_1.fetch_ticker(PAIR)
    return Decimal(str(ticker["last"]))

def cancel_orders(account):
    """Cancel all open orders for the pair on the given account."""
    orders = account.fetch_open_orders(PAIR)
    for order in orders:
        account.cancel_order(order["id"], PAIR)
    print(f"All open orders for {PAIR} canceled.")

def place_limit_order(account, order_type, price, amount):
    """Place a limit order (buy/sell) ensuring minimum order size."""
    order_value = price * amount
    if order_value < MIN_TRADE_VALUE:
        print(f"Order value {order_value:.2f} USDT is below minimum. Skipping.")
        return
    try:
        if order_type == "buy":
            account.create_limit_buy_order(PAIR, float(amount), float(price))
            print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
        elif order_type == "sell":
            account.create_limit_sell_order(PAIR, float(amount), float(price))
            print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
    except Exception as e:
        print(f"Error placing {order_type} order: {e}")

def execute_cycle():
    """Execute a cycle where one account buys and the other sells, then swap roles."""
    while True:
        try:
            # Fetch the latest price
            price = fetch_price()

            # Ensure minimum trade amount in ZON
            trade_amount_zon = TRADE_AMOUNT / price
            print(f"Trading {trade_amount_zon:.4f} ZON at {price:.4f} USDT")

            # Cancel any open orders before placing new ones
            cancel_orders(account_1)
            cancel_orders(account_2)

            # Cycle 1: Account 1 Buys, Account 2 Sells
            place_limit_order(account_1, "buy", price, trade_amount_zon)
            place_limit_order(account_2, "sell", price, trade_amount_zon)

            # Wait before swapping roles
            time.sleep(SLEEP_TIME)

            # Cycle 2: Account 2 Buys, Account 1 Sells
            cancel_orders(account_1)
            cancel_orders(account_2)

            place_limit_order(account_2, "buy", price, trade_amount_zon)
            place_limit_order(account_1, "sell", price, trade_amount_zon)

            # Sleep before the next cycle
            time.sleep(SLEEP_TIME)

        except Exception as e:
            print(f"Error in cycle execution: {e}")
            time.sleep(5)  # Retry delay

if __name__ == "__main__":
    execute_cycle()