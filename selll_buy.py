import time
import ccxt
from decimal import Decimal

# Configuration
API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
EXCHANGE = "bitrue"
PAIR_USDT = "ZON/USDT"
BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
RETRY_DELAY = 5  # Delay in seconds between cycles
RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
MAX_TRADE_AMOUNT = Decimal("30.00")  # Max trade size in USDT (for sell orders)
TRADE_LIMIT = Decimal("30.00")  # Max trade size in USDT

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
            print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
        elif order_type == "sell":
            bitrue.create_limit_sell_order(pair, float(amount), float(price))
            print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
    except Exception as e:
        print(f"Error placing {order_type} order: {e}")

def execute_sell_cycle(current_price):
    """Execute a selling cycle for $30 worth of ZON."""
    print("Executing sell cycle")

    # Place multiple sell orders at different price levels (based on the spread)
    for spread in SELL_SPREAD:
        sell_price = current_price * (1 + spread)
        sell_amount = MAX_TRADE_AMOUNT / sell_price
        place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

def execute_buy_cycle(current_price, usdt_balance):
    """Execute a buying cycle."""
    print("Executing buy cycle")

    # Calculate trade amount based on available balance
    trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

    # Step 1: Place limit buy orders 1% and 2% below the current price
    for spread in BUY_SPREAD:
        buy_price = current_price * (1 - spread)
        buy_amount = TRADE_LIMIT / buy_price
        place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

    # Step 2: Place a market buy order
    place_market_order("buy", PAIR_USDT, trade_amount)

def place_market_order(order_type, pair, amount):
    """Place a market order (buy or sell)."""
    try:
        if order_type == "buy":
            bitrue.create_market_buy_order(pair, float(amount))
            print(f"Market buy order executed: {amount} ZON")
        elif order_type == "sell":
            bitrue.create_market_sell_order(pair, float(amount))
            print(f"Market sell order executed: {amount} ZON")
    except Exception as e:
        print(f"Error placing market {order_type} order: {e}")

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
                print("Reserve balance too low! Pausing the bot.")
                break

            # Fetch current price
            current_price = fetch_price(PAIR_USDT)
            print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

            # Cancel all previous orders
            cancel_all_orders(PAIR_USDT)

            # Execute sell cycle for placing $30 worth of ZON sell orders
            execute_sell_cycle(current_price)

            # Execute buy cycle
            execute_buy_cycle(current_price, usdt_balance)

            # Delay before the next iteration
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
