# import time
# import ccxt
# from decimal import Decimal

# # Configuration
# API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# EXCHANGE = "bitrue"
# PAIR_USDT = "ZON/USDT"
# BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# MIN_PRICE_THRESHOLD = Decimal("0.005")
# HIGH_PRICE_THRESHOLD = Decimal("0.008")
# RETRY_DELAY = 5  # Delay in seconds between cycles
# RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
# TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON

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

# def cancel_all_orders(pair):
#     """Cancel all open orders for the pair."""
#     open_orders = bitrue.fetch_open_orders(pair)
#     for order in open_orders:
#         bitrue.cancel_order(order["id"], pair)
#     print(f"All open orders for {pair} canceled.")

# def place_limit_order(order_type, pair, price, amount):
#     """Place a limit order (buy or sell)."""
#     if amount < Decimal("0.0001"):
#         print("Amount too small, skipping order.")
#         return
#     try:
#         if order_type == "buy":
#             bitrue.create_limit_buy_order(pair, float(amount), float(price))
#             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
#         elif order_type == "sell":
#             bitrue.create_limit_sell_order(pair, float(amount), float(price))
#             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
#     except Exception as e:
#         print(f"Error placing {order_type} order: {e}")

# def place_market_order(order_type, pair, amount):
#     """Place a market order (buy or sell)."""
#     try:
#         if order_type == "buy":
#             bitrue.create_market_buy_order(pair, float(amount))
#             print(f"Market buy order executed: {amount} ZON")
#         elif order_type == "sell":
#             bitrue.create_market_sell_order(pair, float(amount))
#             print(f"Market sell order executed: {amount} ZON")
#     except Exception as e:
#         print(f"Error placing market {order_type} order: {e}")

# def execute_cycle(cycle, current_price, usdt_balance):
#     """Execute a trading cycle."""
#     print(f"Executing Cycle {cycle}")

#     # Calculate trade amount based on available balance
#     trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

#     # Step 1: Place sell orders 0.5% and 1% above the current price
#     for spread in SELL_SPREAD:
#         sell_price = current_price * (1 + spread)
#         sell_amount = TRADE_LIMIT / sell_price
#         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#     # Step 2: Market Sell based on calculated trade amount
#     place_market_order("sell", PAIR_USDT, trade_amount)

#     # Step 3: Place buy orders 1% and 2% below the current price
#     for spread in BUY_SPREAD:
#         buy_price = current_price * (1 - spread)
#         buy_amount = TRADE_LIMIT / buy_price
#         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#     # Step 4: Market Buy based on calculated trade amount
#     place_market_order("buy", PAIR_USDT, trade_amount)

# def main():
#     """Main bot loop."""
#     while True:
#         try:
#             # Fetch balances
#             usdt_balance = fetch_balance("USDT")
#             zon_balance = fetch_balance("ZON")
#             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

#             # Check reserve threshold
#             if usdt_balance < RESERVE_THRESHOLD:
#                 print("Reserve balance too low! Pausing the bot.")
#                 break

#             # Fetch current price
#             current_price = fetch_price(PAIR_USDT)
#             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

#             # Cancel all previous orders
#             cancel_all_orders(PAIR_USDT)

#             # Determine action based on price
#             if current_price >= HIGH_PRICE_THRESHOLD:
#                 print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
#                 execute_cycle(1, current_price, usdt_balance)
#             elif current_price >= MIN_PRICE_THRESHOLD:
#                 print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
#                 execute_cycle(2, current_price, usdt_balance)
#             else:
#                 print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

#             # Delay before the next iteration
#             time.sleep(RETRY_DELAY)

#         except Exception as e:
#             print(f"Error: {e}")
#             time.sleep(RETRY_DELAY)

# if __name__ == "__main__":
#     main()

































# import time
# from decimal import Decimal
# import ccxt

# # Configuration
# API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # Trading parameters
# PAIR_USDT = "ZON/USDT"  # Trading pair
# TRADE_LIMIT = Decimal("10.0")  # Max USDT to trade per order
# HIGH_PRICE_THRESHOLD = Decimal("0.5")
# MIN_PRICE_THRESHOLD = Decimal("0.2")
# RESERVE_THRESHOLD = Decimal("20.0")  # Minimum USDT reserve
# RETRY_DELAY = 60  # Delay between retries in seconds

# # Initialize exchange
# bitrue = ccxt.bitrue({
#     'apiKey': API_KEY,
#     'secret': API_SECRET,
#     'enableRateLimit': True,  # Enables rate limiting
# })

# # Function to validate if the trading pair exists
# def validate_pair(pair):
#     markets = bitrue.load_markets()
#     if pair not in markets:
#         raise ValueError(f"Error: Pair '{pair}' not available on Bitrue.")
#     print(f"Validated pair: {pair}")

# # Function to fetch balance safely
# def fetch_balance(currency):
#     try:
#         balance = bitrue.fetch_balance()
#         free_balance = balance['free'].get(currency, Decimal("0"))
#         print(f"{currency} Balance: {free_balance:.4f}")
#         return Decimal(free_balance)
#     except Exception as e:
#         print(f"Error fetching balance: {e}")
#         return Decimal("0")

# # Function to fetch current market price
# def fetch_price(pair):
#     try:
#         ticker = bitrue.fetch_ticker(pair)
#         price = Decimal(ticker['last'])
#         print(f"Current Price of {pair}: {price:.4f}")
#         return price
#     except Exception as e:
#         print(f"Error fetching price: {e}")
#         return None

# # Function to fetch order book
# def fetch_order_book(pair):
#     try:
#         order_book = bitrue.fetch_order_book(pair)
#         return order_book
#     except Exception as e:
#         print(f"Error fetching order book: {e}")
#         return None

# # Function to place limit orders
# def place_limit_order(order_type, pair, price, amount):
#     try:
#         if order_type == "buy":
#             bitrue.create_limit_buy_order(pair, float(amount), float(price))
#         elif order_type == "sell":
#             bitrue.create_limit_sell_order(pair, float(amount), float(price))
#         print(f"{order_type.capitalize()} Order Placed: {amount:.4f} {pair.split('/')[0]} at {price:.4f} USDT")
#     except Exception as e:
#         print(f"Error placing {order_type} order: {e}")

# # Function to cancel all open orders
# def cancel_all_orders(pair):
#     try:
#         orders = bitrue.fetch_open_orders(pair)
#         for order in orders:
#             bitrue.cancel_order(order['id'])
#         print(f"Cancelled all open orders for {pair}")
#     except Exception as e:
#         print(f"Error cancelling orders: {e}")

# # Trading strategies
# def execute_strategy(strategy, current_price):
#     if strategy == 1:  # High price strategy
#         sell_price = current_price * Decimal("1.02")
#         sell_amount = TRADE_LIMIT / sell_price
#         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         buy_price = current_price * Decimal("0.98")
#         buy_amount = TRADE_LIMIT / buy_price
#         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)
#     elif strategy == 2:  # Low price strategy
#         buy_price = current_price * Decimal("0.99")
#         buy_amount = TRADE_LIMIT / buy_price
#         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#         sell_price = current_price * Decimal("1.01")
#         sell_amount = TRADE_LIMIT / sell_price
#         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

# # Main bot loop
# def main():
#     try:
#         validate_pair(PAIR_USDT)  # Validate pair before starting the bot
#         while True:
#             try:
#                 # Fetch balances
#                 usdt_balance = fetch_balance("USDT")
#                 zon_balance = fetch_balance("ZON")

#                 # Check if reserve balance is sufficient
#                 if usdt_balance < RESERVE_THRESHOLD:
#                     print("USDT balance below reserve threshold! Pausing trading.")
#                     break

#                 # Fetch current price
#                 current_price = fetch_price(PAIR_USDT)
#                 if current_price is None:
#                     print("Unable to fetch current price. Retrying...")
#                     time.sleep(RETRY_DELAY)
#                     continue

#                 # Fetch and analyze order book
#                 order_book = fetch_order_book(PAIR_USDT)
#                 if order_book:
#                     threshold_percentage = Decimal("3")  # 3% threshold
#                     print("Checking for orders within threshold...")
#                     sell_orders = [
#                         order for order in order_book['asks']
#                         if current_price * Decimal("0.97") <= Decimal(order[0]) <= current_price * Decimal("1.03")
#                     ]

#                     if sell_orders:
#                         print(f"Detected {len(sell_orders)} sell orders within 3% of market price.")
#                         execute_strategy(1, current_price)
#                     else:
#                         print("No significant sell orders detected. Running low price strategy.")
#                         cancel_all_orders(PAIR_USDT)
#                         execute_strategy(2, current_price)

#                 time.sleep(RETRY_DELAY)

#             except Exception as e:
#                 print(f"Runtime Error: {e}")
#                 time.sleep(RETRY_DELAY)

#     except Exception as e:
#         print(f"Fatal Error: {e}")

# if __name__ == "__main__":
#     main()






































# import time
# import ccxt
# from decimal import Decimal

# # Configuration
# API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# EXCHANGE = "bitrue"
# PAIR_USDT = "ZON/USDT"
# BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# MIN_PRICE_THRESHOLD = Decimal("0.005")
# HIGH_PRICE_THRESHOLD = Decimal("0.008")
# RETRY_DELAY = 5  # Delay in seconds between cycles
# RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
# TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON

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

# def cancel_all_orders(pair):
#     """Cancel all open orders for the pair."""
#     open_orders = bitrue.fetch_open_orders(pair)
#     for order in open_orders:
#         bitrue.cancel_order(order["id"], pair)
#     print(f"All open orders for {pair} canceled.")

# def place_limit_order(order_type, pair, price, amount):
#     """Place a limit order (buy or sell)."""
#     if amount < Decimal("0.0001"):
#         print("Amount too small, skipping order.")
#         return
#     try:
#         if order_type == "buy":
#             bitrue.create_limit_buy_order(pair, float(amount), float(price))
#             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
#         elif order_type == "sell":
#             bitrue.create_limit_sell_order(pair, float(amount), float(price))
#             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
#     except Exception as e:
#         print(f"Error placing {order_type} order: {e}")

# def place_market_order(order_type, pair, amount):
#     """Place a market order (buy or sell)."""
#     try:
#         if order_type == "buy":
#             bitrue.create_market_buy_order(pair, float(amount))
#             print(f"Market buy order executed: {amount} ZON")
#         elif order_type == "sell":
#             bitrue.create_market_sell_order(pair, float(amount))
#             print(f"Market sell order executed: {amount} ZON")
#     except Exception as e:
#         print(f"Error placing market {order_type} order: {e}")

# def check_sell_orders_within_3_percent(pair, current_price):
#     """Check if there are sell orders within 3% of the current price."""
#     open_orders = bitrue.fetch_open_orders(pair)
#     for order in open_orders:
#         if order['side'] == 'sell':
#             order_price = Decimal(str(order['price']))
#             if order_price >= current_price * 0.97 and order_price <= current_price * 1.03:
#                 print(f"Sell order detected within 3% of current price at {order_price:.4f} USDT")
#                 return True
#     return False

# def execute_cycle(cycle, current_price, usdt_balance, sell_order_detected):
#     """Execute a trading cycle."""
#     print(f"Executing Cycle {cycle}")

#     # Calculate trade amount based on available balance
#     trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

#     if sell_order_detected:
#         # Step 1: Place sell orders 2% below the current price
#         sell_price = current_price * (1 - Decimal("0.02"))
#         sell_amount = TRADE_LIMIT / sell_price
#         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         # Step 2: Place buy orders 2% below the current price
#         buy_price = current_price * (1 - Decimal("0.02"))
#         buy_amount = TRADE_LIMIT / buy_price
#         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)
#     else:
#         # Place sell orders 0.5% and 1% above the current price
#         for spread in SELL_SPREAD:
#             sell_price = current_price * (1 + spread)
#             sell_amount = TRADE_LIMIT / sell_price
#             place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         # Place buy orders 1% and 2% below the current price
#         for spread in BUY_SPREAD:
#             buy_price = current_price * (1 - spread)
#             buy_amount = TRADE_LIMIT / buy_price
#             place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#     # Step 3: Market Buy/Sell based on calculated trade amount
#     place_market_order("sell", PAIR_USDT, trade_amount)
#     place_market_order("buy", PAIR_USDT, trade_amount)

# def main():
#     """Main bot loop."""
#     while True:
#         try:
#             # Fetch balances
#             usdt_balance = fetch_balance("USDT")
#             zon_balance = fetch_balance("ZON")
#             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

#             # Check reserve threshold
#             if usdt_balance < RESERVE_THRESHOLD:
#                 print("Reserve balance too low! Pausing the bot.")
#                 break

#             # Fetch current price
#             current_price = fetch_price(PAIR_USDT)
#             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

#             # Cancel all previous orders
#             cancel_all_orders(PAIR_USDT)

#             # Check for sell orders within 3% of current price
#             sell_order_detected = check_sell_orders_within_3_percent(PAIR_USDT, current_price)

#             # Execute logic based on whether a sell order was detected within 3%
#             execute_cycle(1, current_price, usdt_balance, sell_order_detected)

#             # Delay before the next iteration
#             time.sleep(RETRY_DELAY)

#         except Exception as e:
#             print(f"Error: {e}")
#             time.sleep(RETRY_DELAY)

# if __name__ == "__main__":
#     main()


























# import time
# import ccxt
# from decimal import Decimal

# # Configuration
# API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# EXCHANGE = "bitrue"
# PAIR_USDT = "ZON/USDT"
# BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# MIN_PRICE_THRESHOLD = Decimal("0.005")
# HIGH_PRICE_THRESHOLD = Decimal("0.008")
# RETRY_DELAY = 5  # Delay in seconds between cycles
# RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
# TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON

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

# def cancel_all_orders(pair):
#     """Cancel all open orders for the pair."""
#     open_orders = bitrue.fetch_open_orders(pair)
#     for order in open_orders:
#         bitrue.cancel_order(order["id"], pair)
#     print(f"All open orders for {pair} canceled.")

# def place_limit_order(order_type, pair, price, amount):
#     """Place a limit order (buy or sell)."""
#     if amount < Decimal("0.0001"):
#         print("Amount too small, skipping order.")
#         return
#     try:
#         if order_type == "buy":
#             bitrue.create_limit_buy_order(pair, float(amount), float(price))
#             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
#         elif order_type == "sell":
#             bitrue.create_limit_sell_order(pair, float(amount), float(price))
#             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
#     except Exception as e:
#         print(f"Error placing {order_type} order: {e}")

# def place_market_order(order_type, pair, amount):
#     """Place a market order (buy or sell)."""
#     try:
#         if order_type == "buy":
#             bitrue.create_market_buy_order(pair, float(amount))
#             print(f"Market buy order executed: {amount} ZON")
#         elif order_type == "sell":
#             bitrue.create_market_sell_order(pair, float(amount))
#             print(f"Market sell order executed: {amount} ZON")
#     except Exception as e:
#         print(f"Error placing market {order_type} order: {e}")

# def identify_sell_orders_within_range(pair, current_price, threshold_percentage):
#     """Check if any sell orders are within the specified threshold percentage of the current price."""
#     open_orders = bitrue.fetch_open_orders(pair)
#     for order in open_orders:
#         if order['side'] == 'sell':
#             order_price = Decimal(str(order['price']))
#             price_diff = abs(current_price - order_price) / current_price
#             if price_diff <= threshold_percentage:
#                 print(f"Sell order found within {threshold_percentage * 100}%: {order_price:.4f} USDT")
#                 return True
#     return False

# def execute_cycle(cycle, current_price, usdt_balance):
#     """Execute a trading cycle."""
#     print(f"Executing Cycle {cycle}")

#     # Step 1: Check if there are any sell orders within 3% of the current price
#     if identify_sell_orders_within_range(PAIR_USDT, current_price, 0.03):
#         print(f"Sell order detected within 3% of current price. Placing orders.")
        
#         # Place sell order 2% below the market price
#         for spread in [Decimal("0.02")]:  # 2% below market price
#             sell_price = current_price * (1 - spread)
#             sell_amount = TRADE_LIMIT / sell_price
#             place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         # Place buy order 2% below market price
#         for spread in [Decimal("0.02")]:  # 2% below market price
#             buy_price = current_price * (1 - spread)
#             buy_amount = TRADE_LIMIT / buy_price
#             place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#     else:
#         print("No sell order detected within 3% of the current price. Continuing with current logic.")
#         # Continue with the previous logic (the rest of your execute_cycle code)
#         # Place regular orders and market trades as previously defined

#         # Calculate trade amount based on available balance
#         trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

#         # Place sell orders 0.5% and 1% above the current price
#         for spread in SELL_SPREAD:
#             sell_price = current_price * (1 + spread)
#             sell_amount = TRADE_LIMIT / sell_price
#             place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         # Step 2: Market Sell based on calculated trade amount
#         place_market_order("sell", PAIR_USDT, trade_amount)

#         # Step 3: Place buy orders 1% and 2% below the current price
#         for spread in BUY_SPREAD:
#             buy_price = current_price * (1 - spread)
#             buy_amount = TRADE_LIMIT / buy_price
#             place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#         # Step 4: Market Buy based on calculated trade amount
#         place_market_order("buy", PAIR_USDT, trade_amount)

# def main():
#     """Main bot loop."""
#     while True:
#         try:
#             # Fetch balances
#             usdt_balance = fetch_balance("USDT")
#             zon_balance = fetch_balance("ZON")
#             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

#             # Check reserve threshold
#             if usdt_balance < RESERVE_THRESHOLD:
#                 print("Reserve balance too low! Pausing the bot.")
#                 break

#             # Fetch current price
#             current_price = fetch_price(PAIR_USDT)
#             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

#             # Cancel all previous orders
#             cancel_all_orders(PAIR_USDT)

#             # Determine action based on price
#             if current_price >= HIGH_PRICE_THRESHOLD:
#                 print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
#                 execute_cycle(1, current_price, usdt_balance)
#             elif current_price >= MIN_PRICE_THRESHOLD:
#                 print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
#                 execute_cycle(2, current_price, usdt_balance)
#             else:
#                 print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

#             # Delay before the next iteration
#             time.sleep(RETRY_DELAY)

#         except Exception as e:
#             print(f"Error: {e}")
#             time.sleep(RETRY_DELAY)

# if __name__ == "__main__":
#     main()








## working perfectly fine 



# import time
# import ccxt
# from decimal import Decimal

# # Configuration
# API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# EXCHANGE = "bitrue"
# PAIR_USDT = "ZON/USDT"
# BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# MIN_PRICE_THRESHOLD = Decimal("0.005")
# HIGH_PRICE_THRESHOLD = Decimal("0.008")
# RETRY_DELAY = 5  # Delay in seconds between cycles
# RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
# TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON

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

# def cancel_all_orders(pair):
#     """Cancel all open orders for the pair."""
#     open_orders = bitrue.fetch_open_orders(pair)
#     for order in open_orders:
#         bitrue.cancel_order(order["id"], pair)
#     print(f"All open orders for {pair} canceled.")

# def place_limit_order(order_type, pair, price, amount):
#     """Place a limit order (buy or sell)."""
#     if amount < Decimal("0.0001"):
#         print("Amount too small, skipping order.")
#         return
#     try:
#         if order_type == "buy":
#             bitrue.create_limit_buy_order(pair, float(amount), float(price))
#             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
#         elif order_type == "sell":
#             bitrue.create_limit_sell_order(pair, float(amount), float(price))
#             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
#     except Exception as e:
#         print(f"Error placing {order_type} order: {e}")

# def place_market_order(order_type, pair, amount):
#     """Place a market order (buy or sell)."""
#     try:
#         if order_type == "buy":
#             bitrue.create_market_buy_order(pair, float(amount))
#             print(f"Market buy order executed: {amount} ZON")
#         elif order_type == "sell":
#             bitrue.create_market_sell_order(pair, float(amount))
#             print(f"Market sell order executed: {amount} ZON")
#     except Exception as e:
#         print(f"Error placing market {order_type} order: {e}")

# def identify_sell_orders_within_range(pair, current_price, threshold_percentage):
#     """Check if any sell orders are within the specified threshold percentage of the current price."""
#     order_book = bitrue.fetch_order_book(pair)
#     for sell_price, quantity in order_book['asks']:
#         sell_price = Decimal(str(sell_price))
#         if abs(sell_price - current_price) <= current_price * Decimal(threshold_percentage):
#             print(f"Sell order detected at {sell_price} within {threshold_percentage * 100}% range.")
#             return True
#     return False

# def execute_cycle(cycle, current_price, usdt_balance):
#     """Execute a trading cycle."""
#     print(f"Executing Cycle {cycle}")

#     # Step 1: Check for sell orders within 3% of the current price
#     if identify_sell_orders_within_range(PAIR_USDT, current_price, 0.03):
#         print(f"Sell order detected within 3% of current price. Adjusting strategy.")

#         # Place sell orders 2% below the market price
#         for spread in [Decimal("0.02")]:
#             sell_price = current_price * (1 - spread)
#             sell_amount = TRADE_LIMIT / sell_price
#             place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         # Place buy orders 2% below the market price
#         for spread in [Decimal("0.02")]:
#             buy_price = current_price * (1 - spread)
#             buy_amount = TRADE_LIMIT / buy_price
#             place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#     else:
#         print("No sell order detected within 3% of the current price. Proceeding with normal logic.")

#         # Calculate trade amount based on available balance
#         trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

#         # Place sell orders 0.5% and 1% above the current price
#         for spread in SELL_SPREAD:
#             sell_price = current_price * (1 + spread)
#             sell_amount = TRADE_LIMIT / sell_price
#             place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

#         # Step 2: Market Sell
#         place_market_order("sell", PAIR_USDT, trade_amount)

#         # Step 3: Place buy orders 1% and 2% below the current price
#         for spread in BUY_SPREAD:
#             buy_price = current_price * (1 - spread)
#             buy_amount = TRADE_LIMIT / buy_price
#             place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

#         # Step 4: Market Buy
#         place_market_order("buy", PAIR_USDT, trade_amount)

# def main():
#     """Main bot loop."""
#     while True:
#         try:
#             # Fetch balances
#             usdt_balance = fetch_balance("USDT")
#             zon_balance = fetch_balance("ZON")
#             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

#             # Check reserve threshold
#             if usdt_balance < RESERVE_THRESHOLD:
#                 print("Reserve balance too low! Pausing the bot.")
#                 break

#             # Fetch current price
#             current_price = fetch_price(PAIR_USDT)
#             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

#             # Cancel all previous orders
#             cancel_all_orders(PAIR_USDT)

#             # Determine action based on price
#             if current_price >= HIGH_PRICE_THRESHOLD:
#                 print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
#                 execute_cycle(1, current_price, usdt_balance)
#             elif current_price >= MIN_PRICE_THRESHOLD:
#                 print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
#                 execute_cycle(2, current_price, usdt_balance)
#             else:
#                 print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

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

def identify_sell_orders_within_range(pair, current_price, threshold_percentage):
    """Check if any sell orders are within the specified threshold percentage of the current price."""
    order_book = bitrue.fetch_order_book(pair)
    for sell_price, quantity in order_book['asks']:
        sell_price = Decimal(str(sell_price))
        if abs(sell_price - current_price) <= current_price * Decimal(threshold_percentage):
            print(f"Sell order detected at {sell_price} within {threshold_percentage * 100}% range.")
            return True
    return False

def execute_cycle(cycle, current_price, usdt_balance):
    """Execute a trading cycle."""
    print(f"Executing Cycle {cycle}")

    # Step 1: Check for sell orders within 3% of the current price
    if identify_sell_orders_within_range(PAIR_USDT, current_price, 0.03):
        print(f"Sell order detected within 3% of current price. Adjusting strategy.")

        # Place sell orders 2% below the market price
        for spread in [Decimal("0.02")]:
            sell_price = current_price * (1 - spread)
            sell_amount = TRADE_LIMIT / sell_price
            place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

        # Place buy orders 2% below the market price
        for spread in [Decimal("0.02")]:
            buy_price = current_price * (1 - spread)
            buy_amount = TRADE_LIMIT / buy_price
            place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

    else:
        print("No sell order detected within 3% of the current price. Proceeding with normal logic.")

        # Calculate trade amount based on available balance
        trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

        # Place sell orders 0.5% and 1% above the current price
        for spread in SELL_SPREAD:
            sell_price = current_price * (1 + spread)
            sell_amount = TRADE_LIMIT / sell_price
            place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

        # Step 2: Market Sell
        place_market_order("sell", PAIR_USDT, trade_amount)

        # Step 3: Place buy orders 1% and 2% below the current price
        for spread in BUY_SPREAD:
            buy_price = current_price * (1 - spread)
            buy_amount = TRADE_LIMIT / buy_price
            place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

        # Step 4: Market Buy
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

