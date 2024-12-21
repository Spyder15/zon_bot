# # import requests
# # import hmac
# # import hashlib
# # import time

# # # API Credentials (replace with your real API key and secret)
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Base URL for the API
# # BASE_URL = "https://fapi.bitrue.com"

# # # Pair to trade
# # PAIR = "ZON/USDT"

# # # Threshold price for buying
# # BUY_THRESHOLD = 10

# # # Function to create an HMAC signature
# # def create_signature(params, secret):
# #     query_string = "&".join([f"{key}={params[key]}" for key in sorted(params)])
# #     return hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# # # Function to fetch the current price
# # def get_price():
# #     url = f"{BASE_URL}/market/ticker"
# #     params = {"pair": PAIR}
# #     try:
# #         response = requests.get(url, params=params)
# #         response.raise_for_status()
# #         data = response.json()
# #         print(f"API Response: {data}")  # Debugging line to inspect response
# #         # Adjust key path based on actual API response
# #         last_price = data.get("last_price")
# #         if not last_price:
# #             print(f"Key 'last_price' not found. Response structure: {data}")
# #             return None
# #         return float(last_price)
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error fetching price: {e}")
# #         return None
# #     except ValueError as e:
# #         print(f"Error parsing price data: {e}. Response data: {data}")
# #         return None

# # # Function to place a buy order
# # def place_order(price, quantity):
# #     url = f"{BASE_URL}/order"
# #     timestamp = int(time.time() * 1000)
# #     params = {
# #         "symbol": PAIR.replace("/", ""),
# #         "side": "BUY",
# #         "type": "LIMIT",
# #         "price": price,
# #         "quantity": quantity,
# #         "timestamp": timestamp,
# #         "recvWindow": 5000,
# #     }
# #     params["signature"] = create_signature(params, API_SECRET)
# #     headers = {"X-MBX-APIKEY": API_KEY}

# #     try:
# #         response = requests.post(url, params=params, headers=headers)
# #         response.raise_for_status()
# #         data = response.json()
# #         print(f"Order placed successfully: {data}")
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error placing order: {e}")

# # # Main trading logic
# # def trade_bot():
# #     print("Starting trading bot...")
# #     current_price = get_price()

# #     if current_price is None:
# #         print("Could not fetch the price. Exiting...")
# #         return

# #     print(f"Current price of {PAIR}: {current_price}")

# #     if current_price <= BUY_THRESHOLD:
# #         print(f"Price is below or equal to the threshold (${BUY_THRESHOLD}). Placing a buy order...")
# #         quantity = round(10 / current_price, 8)  # Calculate quantity to spend $10
# #         place_order(current_price, quantity)
# #     else:
# #         print(f"Price is above the threshold (${BUY_THRESHOLD}). No action taken.")

# # # Run the bot
# # if __name__ == "__main__":
# #     trade_bot()




# import time
# import ccxt
# from decimal import Decimal

# # Configuration
# API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# EXCHANGE = "bitrue"
# PAIR_USDT = "ZON/USDT"
# BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# RETRY_DELAY = 5  # Delay in seconds between cycles
# RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT

# # Initialize exchange
# bitrue = ccxt.bitrue({
#     "apiKey": API_KEY,
#     "secret": API_SECRET,
# })

# def fetch_price(pair):
#     """Fetch the current price of the pair."""
#     ticker = bitrue.fetch_ticker(pair)
#     return Decimal(str(ticker["last"]))

# def fetch_balance(currency):
#     """Fetch the balance of the specified currency."""
#     balance = bitrue.fetch_balance()
#     return Decimal(str(balance["free"][currency]))

# def place_limit_order(order_type, pair, price, amount):
#     """Place a limit order (buy only)."""
#     if amount < Decimal("0.0001"):
#         print("Amount too small, skipping order.")
#         return
#     try:
#         if order_type == "buy":
#             bitrue.create_limit_buy_order(pair, float(amount), float(price))
#             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
#     except Exception as e:
#         print(f"Error placing {order_type} order: {e}")

# def place_market_order(order_type, pair, amount):
#     """Place a market order (buy only)."""
#     try:
#         if order_type == "buy":
#             bitrue.create_market_buy_order(pair, float(amount))
#             print(f"Market buy order executed: {amount} ZON")
#     except Exception as e:
#         print(f"Error placing market {order_type} order: {e}")

# def execute_buy_strategy(current_price, usdt_balance):
#     """Execute the buy strategy to push the price up."""
#     print("Executing Buy Strategy")

#     # Calculate trade amount based on available balance
#     trade_amount = min(MAX_TRADE_AMOUNT / current_price, usdt_balance / current_price)

#     # Place buy orders 1% and 2% below the current price
#     for spread in BUY_SPREAD:
#         buy_price = current_price * (1 - spread)
#         buy_amount = MAX_TRADE_AMOUNT / buy_price
#         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#     # Market Buy
#     place_market_order("buy", PAIR_USDT, trade_amount)

# def main():
#     """Main bot loop."""
#     while True:
#         try:
#             # Fetch balances
#             usdt_balance = fetch_balance("USDT")
#             print(f"USDT Balance: {usdt_balance:.2f}")

#             # Check reserve threshold
#             if usdt_balance < RESERVE_THRESHOLD:
#                 print("Reserve balance too low! Pausing the bot.")
#                 break

#             # Fetch current price
#             current_price = fetch_price(PAIR_USDT)
#             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

#             # Execute buy strategy
#             execute_buy_strategy(current_price, usdt_balance)

#             # Delay before the next iteration
#             time.sleep(RETRY_DELAY)

#         except Exception as e:
#             print(f"Error: {e}")
#             time.sleep(RETRY_DELAY)

# if __name__ == "__main__":  
#     main()









import time
import ccxt
from decimal import Decimal

# Configuration
API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
EXCHANGE = "bitrue"
PAIR_USDT = "ZON/USDT"
BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
TRADE_AMOUNT_USDT = Decimal("10.00")  # Fixed trade size of $10
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

def place_limit_order(order_type, pair, price, amount):
    """Place a limit order (buy)."""
    if amount < Decimal("0.0001"):
        print("Amount too small, skipping order.")
        return
    try:
        if order_type == "buy":
            bitrue.create_limit_buy_order(pair, float(amount), float(price))
            print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
    except Exception as e:
        print(f"Error placing {order_type} order: {e}")

def main():
    """Main bot loop."""
    while True:
        try:
            # Fetch balances
            usdt_balance = fetch_balance("USDT")
            print(f"USDT Balance: {usdt_balance:.2f}")

            # Ensure sufficient USDT balance
            if usdt_balance < TRADE_AMOUNT_USDT:
                print("Insufficient USDT balance. Pausing the bot.")
                break

            # Fetch current price
            current_price = fetch_price(PAIR_USDT)
            print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

            # Place buy orders with spread
            for spread in BUY_SPREAD:
                buy_price = current_price * (1 - spread)
                buy_amount = TRADE_AMOUNT_USDT / buy_price
                place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

            # Delay before the next iteration
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
