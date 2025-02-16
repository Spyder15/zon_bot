import time
import ccxt
from decimal import Decimal

# Configuration
API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
EXCHANGE = "bitrue"
PAIR_USDT = "ZON/USDT"
TRADE_SIZE_USDT = Decimal("100.00")  # $100 per trade
RETRY_DELAY = 2  # 2-second delay between trades

# Initialize exchange
bitrue = ccxt.bitrue({
    "apiKey": API_KEY,
    "secret": API_SECRET,
})

def fetch_price():
    """Fetch current market price of ZON/USDT."""
    try:
        ticker = bitrue.fetch_ticker(PAIR_USDT)
        return Decimal(str(ticker["last"]))
    except Exception as e:
        print(f"❌ Error fetching price: {e}")
        return None

def fetch_balance(currency):
    """Fetch balance of a specific currency with error handling."""
    try:
        balance = bitrue.fetch_balance()
        return Decimal(str(balance["free"].get(currency, 0)))
    except Exception as e:
        print(f"❌ Error fetching balance for {currency}: {e}")
        return Decimal("0")

def cancel_all_orders():
    """Cancel all open orders before trading."""
    try:
        open_orders = bitrue.fetch_open_orders(PAIR_USDT)
        for order in open_orders:
            order_id = order["id"]
            bitrue.cancel_order(order_id, PAIR_USDT)
            print(f"🚀 Canceled Order ID: {order_id}")
    except Exception as e:
        print(f"❌ Error canceling orders: {e}")

def place_market_buy():
    """Place a market buy order for $100 worth of ZON."""
    usdt_balance = fetch_balance("USDT")
    if usdt_balance < TRADE_SIZE_USDT:
        print(f"❌ Insufficient USDT balance ({usdt_balance}), stopping bot.")
        return False

    current_price = fetch_price()
    if not current_price:
        print("❌ Unable to fetch price, retrying...")
        return False

    # Calculate ZON quantity to buy
    quantity_to_buy = TRADE_SIZE_USDT / current_price
    if quantity_to_buy < Decimal("1.00"):  # Bitrue min order restriction
        print(f"⚠️ Order size is too small ({quantity_to_buy} ZON), increasing to 1 ZON minimum.")
        quantity_to_buy = Decimal("1.00")

    try:
        order = bitrue.create_market_buy_order(PAIR_USDT, float(quantity_to_buy))
        print(f"✅ Bought {quantity_to_buy:.2f} ZON at market price.")
        return True
    except Exception as e:
        print(f"❌ Error placing market buy order: {e}")
        return False

def main():
    """Main execution loop."""
    print("🔄 Cancelling all open orders before starting...")
    cancel_all_orders()  # Cancel all orders before starting

    while True:
        success = place_market_buy()
        if not success:
            break
        time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
