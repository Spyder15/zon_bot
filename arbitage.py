
import time
import ccxt
from decimal import Decimal

# Configuration
API_KEY = "00907e9d4ece06857597fcae91d54b833fd0238a8bbf56207b47f67876606629"
API_SECRET = "50fc7a48ba34cca68972de37bc45ac892b3abba97e34c74b4e2167fd45b70f8f"
EXCHANGE = "bitrue"
PAIR_XDC = "ZON/XDC"
BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
MIN_PRICE_THRESHOLD = Decimal("0.005")
HIGH_PRICE_THRESHOLD = Decimal("0.008")
SELL_WALL_THRESHOLD = 0.03  # Sell wall detection within 3%
RESERVE_THRESHOLD = Decimal("3.00")  # Minimum reserve in XDC
TRADE_LIMIT = Decimal("400.00")  # Max trade size
RETRY_DELAY = 5  # Seconds between retries

# Initialize exchange
bitrue = ccxt.bitrue({
    "apiKey": API_KEY,
    "secret": API_SECRET,
})

def fetch_price(pair):
    """Fetch the current price of the trading pair."""
    ticker = bitrue.fetch_ticker(pair)
    return Decimal(str(ticker["last"]))

def fetch_balance(currency):
    """Fetch the balance of a specific currency."""
    balance = bitrue.fetch_balance()
    return Decimal(str(balance["free"].get(currency, 0)))

def cancel_all_orders(pair):
    """Cancel all open orders for the pair."""
    open_orders = bitrue.fetch_open_orders(pair)
    for order in open_orders:
        bitrue.cancel_order(order["id"], pair)
    print(f"All open orders for {pair} canceled.")

def place_limit_order(order_type, pair, price, amount):
    """Place a limit order (buy or sell)."""
    if amount < Decimal("0.0001"):
        print("Amount too small, skipping order.")
        return
    try:
        if order_type == "buy":
            bitrue.create_limit_buy_order(pair, float(amount), float(price))
            print(f"Buy order placed: {amount} at {price:.4f} XDC")
        elif order_type == "sell":
            bitrue.create_limit_sell_order(pair, float(amount), float(price))
            print(f"Sell order placed: {amount} at {price:.4f} XDC")
    except Exception as e:
        print(f"Error placing {order_type} order: {e}")

def identify_sell_wall(pair, current_price, threshold_percentage):
    """Identify a sell wall within the threshold percentage."""
    order_book = bitrue.fetch_order_book(pair)
    for sell_price, quantity in order_book['asks']:
        sell_price = Decimal(str(sell_price))
        if abs(sell_price - current_price) <= current_price * Decimal(threshold_percentage):
            print(f"Sell wall detected at {sell_price} with quantity {quantity}.")
            return sell_price
    return None

def execute_cycle(cycle, current_price, xdc_balance):
    """Execute a trading cycle based on the strategy."""
    print(f"Executing cycle {cycle}")

    # Check for sell wall
    sell_wall_price = identify_sell_wall(PAIR_XDC, current_price, SELL_WALL_THRESHOLD)

    if sell_wall_price:
        print(f"Adjusting strategy due to sell wall at {sell_wall_price}.")
        sell_price = sell_wall_price * Decimal("0.98")  # Adjust sell price
        sell_amount = TRADE_LIMIT / sell_price
        place_limit_order("sell", PAIR_XDC, sell_price, sell_amount)

    # Normal strategy
    for spread in SELL_SPREAD:
        sell_price = current_price * (1 + spread)
        sell_amount = TRADE_LIMIT / sell_price
        place_limit_order("sell", PAIR_XDC, sell_price, sell_amount)

    buy_price = current_price * (1 - Decimal("0.01"))
    buy_amount = TRADE_LIMIT / buy_price
    place_limit_order("buy", PAIR_XDC, buy_price, buy_amount)

def main():
    """Main bot logic."""
    while True:
        try:
            xdc_balance = fetch_balance("XDC")
            zon_balance = fetch_balance("ZON")
            print(f"XDC Balance: {xdc_balance}, ZON Balance: {zon_balance}")

            if xdc_balance < RESERVE_THRESHOLD:
                print("Low XDC balance, pausing bot.")
                break

            current_price = fetch_price(PAIR_XDC)
            print(f"Current price of {PAIR_XDC}: {current_price}")

            cancel_all_orders(PAIR_XDC)
            execute_cycle(1, current_price, xdc_balance)

            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
