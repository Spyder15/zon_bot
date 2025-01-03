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
MIN_PRICE_THRESHOLD = Decimal("0.0015")

HIGH_PRICE_THRESHOLD = Decimal("0.008")
RETRY_DELAY = 5  # Delay in seconds between cycles
RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold

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
    if amount < Decimal("0.0001"):
        print("Amount too small, skipping order.")
        return
    try:
        if order_type == "buy":
            bitrue.create_market_buy_order(pair, float(amount))
            print(f"Market buy order executed for {amount} ZON.")
        elif order_type == "sell":
            bitrue.create_market_sell_order(pair, float(amount))
            print(f"Market sell order executed for {amount} ZON.")
    except Exception as e:
        print(f"Error placing market {order_type} order: {e}")

def identify_sell_wall(pair, current_price, threshold_percentage):
    """Identify if a sell wall exists within a threshold percentage of the current price."""
    order_book = bitrue.fetch_order_book(pair)
    for sell_price, quantity in order_book['asks']:
        sell_price = Decimal(str(sell_price))
        if abs(sell_price - current_price) <= current_price * Decimal(threshold_percentage):
            print(f"Sell wall detected at {sell_price} with quantity {quantity}.")
            return sell_price
    return None

def execute_cycle(cycle, current_price, usdt_balance):
    """Execute a trading cycle."""
    print(f"Executing Cycle {cycle}")

    # Calculate dynamic trade size (30% of available reserve)
    trade_size = usdt_balance * Decimal("0.30")
    print(f"Dynamic trade size: {trade_size:.2f} USDT")

    # Step 1: Check for sell wall within 3% of the current price
    sell_wall_price = identify_sell_wall(PAIR_USDT, current_price, 0.03)

    if sell_wall_price:
        print(f"Adjusting strategy due to sell wall at {sell_wall_price}.")

        # Place sell order 2% below market price
        sell_price = current_price * (1 - Decimal("0.02"))
        sell_amount = trade_size / sell_price
        place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

        # Place buy order 2% below market price
        buy_price = current_price * (1 - Decimal("0.02"))
        buy_amount = trade_size / buy_price
        place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)
    else:
        print("No sell wall detected within 3% of the current price. Proceeding with normal logic.")

        # Place sell orders 0.5% and 1% above the current price
        for spread in SELL_SPREAD:
            sell_price = current_price * (1 + spread)
            sell_amount = trade_size / sell_price
            place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

        # Place only one market buy order (matching the first sell order's quantity)
        first_sell_price = current_price * (1 + SELL_SPREAD[0])  # First sell price (0.5% above market)
        first_sell_amount = trade_size / first_sell_price
        place_market_order("buy", PAIR_USDT, first_sell_amount)

        # Place buy order 1% below market price
        buy_price = current_price * (1 - Decimal("0.01"))
        buy_amount = trade_size / buy_price
        place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

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
