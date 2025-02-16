import time
import ccxt
from decimal import Decimal

# Configuration
API_KEY = "00907e9d4ece06857597fcae91d54b833fd0238a8bbf56207b47f67876606629"
API_SECRET = "50fc7a48ba34cca68972de37bc45ac892b3abba97e34c74b4e2167fd45b70f8f"
EXCHANGE = "bitrue"
PAIR_USDT = "ZON/USDT"
PAIR_XDC = "ZON/XDC"
BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]
SELL_SPREAD = [Decimal("0.03"), Decimal("0.02")]
MIN_PRICE_THRESHOLD = Decimal("0.005")
HIGH_PRICE_THRESHOLD = Decimal("0.008")
SELL_WALL_THRESHOLD = 0.03
RESERVE_THRESHOLD = Decimal("1.00")
TRADE_LIMIT = Decimal("1.00")  # Trade limit set to 1 USDT per trade
MIN_TRADE_VALUE = Decimal("1.00")
RETRY_DELAY = 5  

# Initialize exchange
bitrue = ccxt.bitrue({
    "apiKey": API_KEY,
    "secret": API_SECRET,
})

def fetch_price(pair):
    """Fetch the current price of a trading pair with error handling."""
    try:
        ticker = bitrue.fetch_ticker(pair)
        return Decimal(str(ticker["last"]))
    except Exception as e:
        print(f"❌ Error fetching price for {pair}: {e}")
        return None

def fetch_balance(currency):
    """Fetch balance of a specific currency with retry mechanism."""
    try:
        balance = bitrue.fetch_balance()
        return Decimal(str(balance["free"].get(currency, 0)))
    except Exception as e:
        print(f"❌ Error fetching balance for {currency}: {e}")
        return Decimal("0")

def cancel_all_orders():
    """Cancel all open orders to free up USDT balance."""
    try:
        open_orders = bitrue.fetch_open_orders(PAIR_USDT)
        for order in open_orders:
            order_id = order["id"]
            bitrue.cancel_order(order_id, PAIR_USDT)
            print(f"🚀 Canceled Order ID: {order_id}")
    except Exception as e:
        print(f"❌ Error canceling orders: {e}")

def place_limit_order(order_type, pair, price, amount):
    """Place a limit buy or sell order, ensuring it meets the minimum order value."""
    order_value = amount * price
    if order_value < MIN_TRADE_VALUE:
        print(f"⚠️ Skipping {order_type.upper()} order at {price:.6f} USDT, value {order_value:.6f} is below {MIN_TRADE_VALUE} USDT.")
        return
    
    try:
        if order_type == "buy":
            bitrue.create_limit_buy_order(pair, float(amount), float(price))
            print(f"✅ Buy order placed: {amount} ZON at {price:.6f} USDT")
        elif order_type == "sell":
            bitrue.create_limit_sell_order(pair, float(amount), float(price))
            print(f"✅ Sell order placed: {amount} ZON at {price:.6f} USDT")
    except Exception as e:
        print(f"❌ Error placing {order_type.upper()} order at {price:.6f} USDT: {e}")

def execute_trades(current_price, usdt_balance, zon_balance):
    """Execute buy and sell trades based on strategy."""
    print("🚀 Executing trading strategy...")

    if usdt_balance < RESERVE_THRESHOLD:
        print("⚠️ USDT balance below reserve threshold. Stopping buys.")
        return

    # Sell Strategy
    for spread in SELL_SPREAD:
        sell_price = current_price * (1 + spread)
        sell_amount = min(TRADE_LIMIT / sell_price, zon_balance)
        place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

    # Buy Strategy
    for spread in BUY_SPREAD:
        buy_price = current_price * (1 - spread)
        buy_amount = TRADE_LIMIT / buy_price
        if (usdt_balance - buy_amount * buy_price) > RESERVE_THRESHOLD:
            place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)
        else:
            print(f"⚠️ Skipping buy order at {buy_price:.6f} USDT to maintain USDT reserve.")

def main():
    """Main bot execution loop."""
    print("🔄 Cancelling all open orders before starting...")
    cancel_all_orders()  # Cancel all orders before proceeding

    while True:
        try:
            usdt_balance = fetch_balance("USDT")
            zon_balance = fetch_balance("ZON")
            print(f"💰 USDT Balance: {usdt_balance}, ZON Balance: {zon_balance}")

            if usdt_balance < RESERVE_THRESHOLD:
                print("❌ Low USDT balance, stopping bot to preserve reserve.")
                break

            current_price = fetch_price(PAIR_USDT)
            if not current_price:
                time.sleep(RETRY_DELAY)
                continue

            print(f"📈 Current price of {PAIR_USDT}: {current_price}")
            execute_trades(current_price, usdt_balance, zon_balance)
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
