import time
import ccxt
from decimal import Decimal

# Configuration
API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
EXCHANGE = "bitrue"
PAIR_USDT = "ZON/USDT"
SELL_WALL_THRESHOLD_MULTIPLIER = Decimal("2")  # Sell wall threshold multiplier
ADJUSTMENT_PERCENTAGE = Decimal("0.005")  # 0.5% below sell wall
RESERVE_THRESHOLD = Decimal("30.00")  # Minimum USDT reserve
TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON
RETRY_DELAY = 5  # Delay in seconds between cycles

# Initialize exchange
bitrue = ccxt.bitrue({
    "apiKey": API_KEY,
    "secret": API_SECRET,
})

def fetch_price(pair):
    """Fetch the current price of the pair."""
    ticker = bitrue.fetch_ticker(pair)
    return Decimal(str(ticker["last"]))

def fetch_balance(currency):
    """Fetch the balance of the specified currency."""
    balance = bitrue.fetch_balance()
    return Decimal(str(balance["free"][currency]))

def fetch_order_book(pair, depth=10):
    """Fetch the order book for the specified pair."""
    order_book = bitrue.fetch_order_book(pair, depth)
    return order_book["asks"]

def detect_sell_wall(order_book, threshold_multiplier=2):
    """
    Detects a sell wall in the order book.

    Args:
        order_book: The order book data (list of sell orders as price/quantity pairs).
        threshold_multiplier: Multiplier to define a sell wall.

    Returns:
        Sell wall price if detected, None otherwise.
    """
    average_order_size = sum([order[1] for order in order_book]) / len(order_book)
    for sell_order in order_book:
        price, quantity = sell_order
        if Decimal(quantity) > Decimal(average_order_size) * Decimal(threshold_multiplier):
            return Decimal(price)
    return None

def adjust_buy_price(current_price, sell_wall_price, adjustment_percentage=0.005):
    """
    Adjusts the buy price to avoid a sell wall.

    Args:
        current_price: Current market price.
        sell_wall_price: Price of the detected sell wall.
        adjustment_percentage: Percentage to lower the price.

    Returns:
        Adjusted buy price.
    """
    if sell_wall_price and sell_wall_price <= current_price:
        return sell_wall_price * (1 - adjustment_percentage)
    return current_price

def place_limit_order(order_type, pair, price, amount):
    """Place a limit order (buy or sell)."""
    if amount < Decimal("0.0001"):
        print("Amount too small, skipping order.")
        return
    try:
        if order_type == "buy":
            bitrue.create_limit_buy_order(pair, float(amount), float(price))
            print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
        elif order_type == "sell":
            bitrue.create_limit_sell_order(pair, float(amount), float(price))
            print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
    except Exception as e:
        print(f"Error placing {order_type} order: {e}")

def cancel_open_orders(pair):
    """Cancel all open orders for the pair."""
    try:
        open_orders = bitrue.fetch_open_orders(pair)
        for order in open_orders:
            bitrue.cancel_order(order['id'], pair)
            print(f"Canceled order {order['id']}")
    except Exception as e:
        print(f"Error canceling open orders: {e}")

def main():
    """Main bot loop."""
    while True:
        try:
            # Fetch balances
            usdt_balance = fetch_balance("USDT")
            zon_balance = fetch_balance("ZON")
            print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

            # Check reserve threshold
            if usdt_balance < RESERVE_THRESHOLD:
                print("USDT balance below reserve threshold! Stopping buy orders.")
                time.sleep(RETRY_DELAY)
                continue

            # Fetch current price
            current_price = fetch_price(PAIR_USDT)
            print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

            # Fetch order book and detect sell wall
            order_book = fetch_order_book(PAIR_USDT)
            sell_wall_price = detect_sell_wall(order_book, SELL_WALL_THRESHOLD_MULTIPLIER)
            if sell_wall_price:
                print(f"Detected sell wall at {sell_wall_price:.4f} USDT")

            # Adjust buy price
            adjusted_buy_price = adjust_buy_price(current_price, sell_wall_price, ADJUSTMENT_PERCENTAGE)
            print(f"Adjusted buy price: {adjusted_buy_price:.4f} USDT")

            # Fetch current open orders and cancel them
            cancel_open_orders(PAIR_USDT)

            # Calculate trade amount based on available balance
            trade_amount = min(TRADE_LIMIT / adjusted_buy_price, usdt_balance / adjusted_buy_price)

            # Place buy order below sell wall
            place_limit_order("buy", PAIR_USDT, adjusted_buy_price, trade_amount)

            # Delay before the next iteration
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
