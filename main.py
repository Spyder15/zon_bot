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
MIN_PRICE_THRESHOLD = Decimal("0.005")
HIGH_PRICE_THRESHOLD = Decimal("0.008")
RETRY_DELAY = 5  # Delay in seconds between cycles
RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON

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

def execute_cycle(cycle, current_price, usdt_balance):
    """Execute a trading cycle."""
    print(f"Executing Cycle {cycle}")

    # Calculate trade amount based on available balance
    trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

    # Step 1: Place sell orders 0.5% and 1% above the current price
    for spread in SELL_SPREAD:
        sell_price = current_price * (1 + spread)
        sell_amount = TRADE_LIMIT / sell_price
        place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

    # Step 2: Market Sell based on calculated trade amount
    place_market_order("sell", PAIR_USDT, trade_amount)

    # Step 3: Place buy orders 1% and 2% below the current price
    for spread in BUY_SPREAD:
        buy_price = current_price * (1 - spread)
        buy_amount = TRADE_LIMIT / buy_price
        place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

    # Step 4: Market Buy based on calculated trade amount
    place_market_order("buy", PAIR_USDT, trade_amount)

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

            # Determine action based on price
            if current_price >= HIGH_PRICE_THRESHOLD:
                print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
                execute_cycle(1, current_price, usdt_balance)
            elif current_price >= MIN_PRICE_THRESHOLD:
                print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
                execute_cycle(2, current_price, usdt_balance)
            else:
                print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

            # Delay before the next iteration
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
