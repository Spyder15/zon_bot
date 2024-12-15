# # import ccxt
# # import time

# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # secret_key = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': secret_key
# # })

# # # Synchronize time
# # def sync_time():
# #     server_time = bitrue.fetch_time()
# #     local_time = int(time.time() * 1000)
# #     offset = server_time - local_time
# #     print(f"Time offset: {offset} ms")
# #     return offset

# # # Adjust your nonce function
# # time_offset = sync_time()

# # def nonce():
# #     return int(time.time() * 1000) + time_offset

# # bitrue.nonce = nonce  # Overwrite CCXT's default nonce

# # pair = "ZON/USDT"

# # def main():
# #     print("Starting bot...")
# #     markets = bitrue.load_markets()
# #     if pair not in markets:
# #         print(f"Trading pair {pair} is not available.")
# #         return

# #     print(f"Trading pair {pair} is valid.")

# #     while True:
# #         try:
# #             # Fetch order book
# #             order_book = bitrue.fetch_order_book(pair)
# #             print("Order book fetched.")

# #             # Cancel existing orders
# #             open_orders = bitrue.fetch_open_orders(pair)
# #             for order in open_orders:
# #                 bitrue.cancel_order(order['id'], pair)
# #                 print(f"Cancelled order: {order['id']}")

# #             # Example logic for placing orders
# #             print("Placing new orders...")

# #             time.sleep(5)  # Delay for throttling
# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(5)  # Retry delay

# # if __name__ == "__main__":
# #     main()




# # import ccxt
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants
# # PAIR = "ZON/USDT"
# # TRADE_SIZE_USDT = 5  # $5 per trade
# # ORDER_REFRESH_INTERVAL = 180  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = 0.005  # 0.5% below the current price
# # SELL_SPREAD = 0.005  # 0.5% above the current price
# # MAX_ORDERS = 5  # Max buy/sell orders at any given time


# # def place_spread_orders(current_price):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     """
# #     try:
# #         # Cancel all existing orders
# #         bitrue.cancel_all_orders(PAIR)
# #         print("Canceled all open orders.")

# #         # Place buy orders
# #         for i in range(MAX_ORDERS):
# #             buy_price = current_price * (1 - (BUY_SPREAD * (i + 1)))
# #             buy_amount = TRADE_SIZE_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR, buy_amount, buy_price)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_ORDERS):
# #             sell_price = current_price * (1 + (SELL_SPREAD * (i + 1)))
# #             sell_amount = TRADE_SIZE_USDT / current_price
# #             bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")


# # def simulate_trades(current_price):
# #     """
# #     Execute small buy/sell trades to inflate volume.
# #     """
# #     try:
# #         # Small buy trade
# #         buy_amount = TRADE_SIZE_USDT / current_price
# #         bitrue.create_market_buy_order(PAIR, buy_amount)
# #         print(f"Simulated buy: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# #         # Small delay
# #         time.sleep(2)

# #         # Small sell trade
# #         sell_amount = TRADE_SIZE_USDT / current_price
# #         sell_price = current_price * 1.01  # Sell at 1% higher price
# #         bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #         print(f"Simulated sell: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error simulating trades: {e}")


# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price
# #             ticker = bitrue.fetch_ticker(PAIR)
# #             current_price = ticker['last']
# #             print(f"Current price of {PAIR}: {current_price:.4f} USDT")

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price)
# #                 last_refresh_time = time.time()

# #             # Simulate small alternating trades
# #             simulate_trades(current_price)

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(10)  # Retry after a short delay


# # if __name__ == "__main__":
# #     main()













# # import ccxt
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants
# # PAIR = "ZON/USDT"
# # TRADE_SIZE_USDT = 5  # $5 per trade
# # ORDER_REFRESH_INTERVAL = 180  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = 0.005  # 0.5% below the current price
# # SELL_SPREAD = 0.003  # Adjusted to 0.3% above the current price
# # MAX_ORDERS = 5  # Max buy/sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds


# # def cancel_all_orders():
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(PAIR)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], PAIR)
# #         print("Canceled all open orders.")
# #     except Exception as e:
# #         print(f"Error canceling orders: {e}")
# #         time.sleep(RETRY_DELAY)


# # def place_spread_orders(current_price):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     """
# #     try:
# #         # Cancel all existing orders
# #         cancel_all_orders()

# #         # Place buy orders
# #         for i in range(MAX_ORDERS):
# #             buy_price = current_price * (1 - (BUY_SPREAD * (i + 1)))
# #             buy_amount = TRADE_SIZE_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR, buy_amount, buy_price)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_ORDERS):
# #             sell_price = current_price * (1 + (SELL_SPREAD * (i + 1)))
# #             sell_amount = TRADE_SIZE_USDT / current_price
# #             bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)


# # def simulate_trades(current_price):
# #     """
# #     Execute small buy/sell trades to inflate volume.
# #     """
# #     try:
# #         # Small buy trade
# #         buy_amount = TRADE_SIZE_USDT / current_price
# #         bitrue.create_market_buy_order(PAIR, buy_amount)
# #         print(f"Simulated buy: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# #         # Small delay
# #         time.sleep(2)

# #         # Small sell trade
# #         sell_amount = TRADE_SIZE_USDT / current_price
# #         sell_price = current_price * 1.01  # Sell at 1% higher price
# #         bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #         print(f"Simulated sell: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error simulating trades: {e}")
# #         time.sleep(RETRY_DELAY)


# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price
# #             ticker = bitrue.fetch_ticker(PAIR)
# #             current_price = ticker['last']
# #             print(f"Current price of {PAIR}: {current_price:.4f} USDT")

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price)
# #                 last_refresh_time = time.time()

# #             # Simulate small alternating trades
# #             simulate_trades(current_price)

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay


# # if __name__ == "__main__":
# #     main()











# # import ccxt 
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants
# # PAIR = "ZON/USDT"
# # TRADE_SIZE_USDT = 5  # $5 per trade
# # ORDER_REFRESH_INTERVAL = 180  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = 0.005  # 0.5% below the current price
# # SELL_SPREAD = 0.005  # 0.5% above the current price
# # MAX_ORDERS = 5  # Max buy/sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds


# # def cancel_all_orders():
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(PAIR)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], PAIR)
# #         print("Canceled all open orders.")
# #     except Exception as e:
# #         print(f"Error canceling orders: {e}")
# #         time.sleep(RETRY_DELAY)


# # def place_spread_orders(current_price):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     """
# #     try:
# #         # Cancel all existing orders
# #         cancel_all_orders()

# #         # Place buy orders
# #         for i in range(MAX_ORDERS):
# #             buy_price = current_price * (1 - (BUY_SPREAD * (i + 1)))
# #             buy_amount = TRADE_SIZE_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR, buy_amount, buy_price)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_ORDERS):
# #             sell_price = current_price * (1 + (SELL_SPREAD * (i + 1)))
# #             sell_amount = TRADE_SIZE_USDT / current_price
# #             bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)


# # def simulate_trades(current_price):
# #     """
# #     Execute small buy/sell trades to inflate volume.
# #     """
# #     try:
# #         # Small buy trade
# #         buy_amount = TRADE_SIZE_USDT / current_price
# #         bitrue.create_market_buy_order(PAIR, buy_amount)
# #         print(f"Simulated buy: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# #         # Small delay
# #         time.sleep(2)

# #         # Small sell trade
# #         sell_amount = TRADE_SIZE_USDT / current_price
# #         sell_price = current_price * 1.005  # Sell at 0.5% higher price
# #         bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #         print(f"Simulated sell: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error simulating trades: {e}")
# #         time.sleep(RETRY_DELAY)


# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price
# #             ticker = bitrue.fetch_ticker(PAIR)
# #             current_price = ticker['last']
# #             print(f"Current price of {PAIR}: {current_price:.4f} USDT")

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price)
# #                 last_refresh_time = time.time()

# #             # Simulate small alternating trades
# #             simulate_trades(current_price)

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay


# # if __name__ == "__main__":
# #     main()




















# # import ccxt 
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants
# # PAIR = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = 4  # $4 per buy trade
# # TRADE_SIZE_SELL_USDT = 5  # $5 per sell trade
# # ORDER_REFRESH_INTERVAL = 180  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = [0.02, 0.05]  # 2% to 5% below the current price
# # SELL_SPREAD = [0.02, 0.05]  # 2% to 5% above the current price
# # MAX_ORDERS = 5  # Max buy/sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds


# # def cancel_all_orders():
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(PAIR)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], PAIR)
# #         print("Canceled all open orders.")
# #     except Exception as e:
# #         print(f"Error canceling orders: {e}")
# #         time.sleep(RETRY_DELAY)


# # def place_spread_orders(current_price):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     """
# #     try:
# #         # Cancel all existing orders
# #         cancel_all_orders()

# #         # Place buy orders
# #         for i in range(MAX_ORDERS):
# #             buy_price = current_price * (1 - (BUY_SPREAD[0] + (BUY_SPREAD[1] - BUY_SPREAD[0]) * i / (MAX_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR, buy_amount, buy_price)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_ORDERS):
# #             sell_price = current_price * (1 + (SELL_SPREAD[0] + (SELL_SPREAD[1] - SELL_SPREAD[0]) * i / (MAX_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price
# #             bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)


# # def simulate_trades(current_price):
# #     """
# #     Execute small buy/sell trades to inflate volume.
# #     """
# #     try:
# #         # Small buy trade
# #         buy_amount = TRADE_SIZE_BUY_USDT / current_price
# #         bitrue.create_market_buy_order(PAIR, buy_amount)
# #         print(f"Simulated buy: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# #         # Small delay
# #         time.sleep(2)

# #         # Small sell trade
# #         sell_amount = TRADE_SIZE_SELL_USDT / current_price
# #         sell_price = current_price * 1.005  # Sell at 0.5% higher price
# #         bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #         print(f"Simulated sell: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error simulating trades: {e}")
# #         time.sleep(RETRY_DELAY)


# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price
# #             ticker = bitrue.fetch_ticker(PAIR)
# #             current_price = ticker['last']
# #             print(f"Current price of {PAIR}: {current_price:.4f} USDT")

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price)
# #                 last_refresh_time = time.time()

# #             # Simulate small alternating trades
# #             simulate_trades(current_price)

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay


# # if __name__ == "__main__":
# #     main()













# # import ccxt 
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants
# # PAIR = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = 4  # $4 per buy trade
# # TRADE_SIZE_SELL_USDT = 5  # $5 per sell trade
# # ORDER_REFRESH_INTERVAL = 180  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = [0.02, 0.05]  # 2% to 5% below the current price
# # SELL_SPREAD = [0.02, 0.05]  # 2% to 5% above the current price
# # MAX_BUY_ORDERS = 5  # Max buy orders at any given time
# # MAX_SELL_ORDERS = 10  # Max sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds
# # MIN_PRICE_THRESHOLD = 0.010  # Minimum price threshold to trigger orders

# # def cancel_all_orders():
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(PAIR)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], PAIR)
# #         print("Canceled all open orders.")
# #     except Exception as e:
# #         print(f"Error canceling orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def place_spread_orders(current_price):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     Maintain a 1:2 buy to sell ratio and ensure price exceeds threshold.
# #     """
# #     try:
# #         # Skip placing orders if the price is below the minimum threshold
# #         if current_price < MIN_PRICE_THRESHOLD:
# #             print(f"Price too low: {current_price:.4f} USDT. Skipping order placement.")
# #             return

# #         # Cancel all existing orders
# #         cancel_all_orders()

# #         # Place buy orders (1:2 ratio, 5 buy orders)
# #         for i in range(MAX_BUY_ORDERS):  # 5 buy orders
# #             buy_price = current_price * (1 - (BUY_SPREAD[0] + (BUY_SPREAD[1] - BUY_SPREAD[0]) * i / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR, buy_amount, buy_price)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders (2 times the buy orders: 10 sell orders)
# #         for i in range(MAX_SELL_ORDERS):  # 10 sell orders
# #             sell_price = current_price * (1 + (SELL_SPREAD[0] + (SELL_SPREAD[1] - SELL_SPREAD[0]) * i / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price
# #             bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def simulate_trades(current_price):
# #     """
# #     Execute small buy/sell trades to inflate volume.
# #     """
# #     try:
# #         # Small buy trade
# #         buy_amount = TRADE_SIZE_BUY_USDT / current_price
# #         bitrue.create_market_buy_order(PAIR, buy_amount)
# #         print(f"Simulated buy: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# #         # Small delay
# #         time.sleep(2)

# #         # Small sell trade
# #         sell_amount = TRADE_SIZE_SELL_USDT / current_price
# #         sell_price = current_price * 1.005  # Sell at 0.5% higher price
# #         bitrue.create_limit_sell_order(PAIR, sell_amount, sell_price)
# #         print(f"Simulated sell: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error simulating trades: {e}")
# #         time.sleep(RETRY_DELAY)

# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price
# #             ticker = bitrue.fetch_ticker(PAIR)
# #             current_price = ticker['last']
# #             print(f"Current price of {PAIR}: {current_price:.4f} USDT")

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price)
# #                 last_refresh_time = time.time()

# #             # Simulate small alternating trades
# #             simulate_trades(current_price)

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay

# # if __name__ == "__main__":
# #     main()


























# # import ccxt
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY = 4  # $4 worth of ZON per buy trade
# # TRADE_SIZE_SELL = 4  # $4 worth of ZON per sell trade
# # ORDER_REFRESH_INTERVAL = 60  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = [0.02, 0.05]  # 2% to 5% below the current price
# # SELL_SPREAD = [0.01, 0.03]  # 1% to 3% above the current price
# # MAX_BUY_ORDERS = 5  # Max buy orders at any given time
# # MAX_SELL_ORDERS = 10  # Max sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds
# # MIN_PRICE_THRESHOLD = 0.010  # Minimum price threshold to trigger orders
# # PAUSE_PRICE_THRESHOLD = 0.0112  # Price threshold to pause buy orders
# # INITIAL_USDT_BALANCE = 200  # Example initial USDT balance
# # USDT_LOSS_THRESHOLD = 50  # Amount of USDT drop to trigger focus on selling

# # # Function to fetch the current balance of USDT
# # def get_usdt_balance():
# #     balance = bitrue.fetch_balance()
# #     return balance['total']['USDT']

# # def fetch_price(pair):
# #     """Fetch the last price for a given trading pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return ticker['last']

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(pair)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], pair)
# #         print(f"Canceled all open orders for {pair}.")
# #     except Exception as e:
# #         print(f"Error canceling orders for {pair}: {e}")
# #         time.sleep(RETRY_DELAY)

# # def place_spread_orders(current_price, usdt_balance):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     Maintain a 1:2 buy to sell ratio and ensure price exceeds threshold.
# #     Adjust buy order sizes based on USDT reserves.
# #     """
# #     try:
# #         # Skip placing orders if the price is below the minimum threshold
# #         if current_price < MIN_PRICE_THRESHOLD:
# #             print(f"Price too low: {current_price:.4f}. Skipping order placement.")
# #             return

# #         # Pause buy orders if the price exceeds the threshold
# #         if current_price > PAUSE_PRICE_THRESHOLD:
# #             print(f"Price above {PAUSE_PRICE_THRESHOLD}. Pausing buy orders.")
# #             return

# #         # Cancel all existing orders
# #         cancel_all_orders(PAIR_USDT)

# #         # Adjust buy order size based on USDT balance
# #         if usdt_balance < (INITIAL_USDT_BALANCE - USDT_LOSS_THRESHOLD):
# #             # If USDT balance drops by more than the threshold, reduce buy order size
# #             trade_size_buy = 3  # Reduce buy order size to $3
# #             print("USDT balance dropped significantly. Reducing buy order size to $3.")
# #         else:
# #             trade_size_buy = TRADE_SIZE_BUY

# #         # Place buy orders (1:2 ratio, 5 buy orders)
# #         for i in range(MAX_BUY_ORDERS):  # 5 buy orders
# #             buy_price = current_price * (1 - (BUY_SPREAD[0] + (BUY_SPREAD[1] - BUY_SPREAD[0]) * i / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = trade_size_buy / buy_price
# #             bitrue.create_limit_buy_order(PAIR_USDT, buy_amount, buy_price)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders (2 times the buy orders: 10 sell orders)
# #         for i in range(MAX_SELL_ORDERS):  # 10 sell orders
# #             sell_price = current_price * (1 + (SELL_SPREAD[0] + (SELL_SPREAD[1] - SELL_SPREAD[0]) * i / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL / current_price
# #             bitrue.create_limit_sell_order(PAIR_USDT, sell_amount, sell_price)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def simulate_trades(current_price):
# #     """
# #     Execute small buy/sell trades to inflate volume.
# #     """
# #     try:
# #         # Small buy trade
# #         buy_amount = TRADE_SIZE_BUY / current_price
# #         bitrue.create_market_buy_order(PAIR_USDT, buy_amount)
# #         print(f"Simulated buy: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# #         # Small delay
# #         time.sleep(2)

# #         # Small sell trade
# #         sell_amount = TRADE_SIZE_SELL / current_price
# #         sell_price = current_price * 1.005  # Sell at 0.5% higher price
# #         bitrue.create_limit_sell_order(PAIR_USDT, sell_amount, sell_price)
# #         print(f"Simulated sell: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error simulating trades: {e}")
# #         time.sleep(RETRY_DELAY)

# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price for ZON/USDT
# #             current_price = fetch_price(PAIR_USDT)

# #             # Get the current USDT balance
# #             usdt_balance = get_usdt_balance()
            
# #             print(f"Current price of ZON/USDT: {current_price:.4f} USDT")
# #             print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price, usdt_balance)
# #                 last_refresh_time = time.time()

# #             # Simulate small alternating trades
# #             simulate_trades(current_price)

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay

# # if __name__ == "__main__":
# #     main()






# # # Constants for ZON/USDT trading pair
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = 4  # $4 worth of ZON for buy orders in USDT terms
# # TRADE_SIZE_SELL_USDT = 4  # $4 worth of ZON for sell orders in USDT terms
# # ORDER_REFRESH_INTERVAL = 180  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = [0.02, 0.05]  # 2% to 5% below the current price for buy orders
# # SELL_SPREAD = [0.01, 0.03]  # 1% to 3% above the current price for sell orders
# # MAX_BUY_ORDERS = 5  # Max buy orders at any given time
# # MAX_SELL_ORDERS = 10  # Max sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds
# # MIN_PRICE_THRESHOLD = 0.010  # Minimum price threshold to trigger orders
# # BUY_PAUSE_PRICE = 0.125  # Pause buy orders if ZON/USDT price exceeds this threshold

# # # Tracking profit variables
# # buy_orders = []  # List to store buy orders (buy price, amount)
# # sell_orders = []  # List to store sell orders (sell price, amount)

# # # Example function to track a completed buy order
# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})
# #     print(f"Buy order recorded: {amount} ZON at {price} USDT")

# # # Example function to track a completed sell order
# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})
# #     print(f"Sell order recorded: {amount} ZON at {price} USDT")

# # # Function to calculate profit
# # def calculate_profit():
# #     total_profit = 0
# #     for buy_order, sell_order in zip(buy_orders, sell_orders):
# #         buy_price = buy_order['price']
# #         sell_price = sell_order['price']
# #         amount = sell_order['amount']

# #         # Calculate profit before fees
# #         profit_before_fees = (sell_price - buy_price) * amount

# #         # Deduct trading fees (example fee of 0.1%)
# #         fee = 0.001  # 0.1% fee
# #         fee_deducted = (buy_price + sell_price) * fee * amount  # total fee for both buy and sell

# #         # Calculate net profit after fees
# #         net_profit = profit_before_fees - fee_deducted
# #         total_profit += net_profit

# #     print(f"Total profit: {total_profit:.4f} USDT")
# #     return total_profit

# # def fetch_price(pair):
# #     """Fetch the last price for a given trading pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return ticker['last']

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(pair)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], pair)
# #         print(f"Canceled all open orders for {pair}.")
# #     except Exception as e:
# #         print(f"Error canceling orders for {pair}: {e}")
# #         time.sleep(RETRY_DELAY)

# # def place_spread_orders(current_price_usdt):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     Maintain a 1:2 buy to sell ratio and ensure price exceeds threshold.
# #     """
# #     try:
# #         # Skip placing orders if the price is below the minimum threshold
# #         if current_price_usdt < MIN_PRICE_THRESHOLD:
# #             print(f"Price too low: {current_price_usdt:.4f} USDT. Skipping order placement.")
# #             return

# #         # Pause buy orders if the price exceeds the defined threshold
# #         if current_price_usdt > BUY_PAUSE_PRICE:
# #             print(f"Price exceeds threshold ({BUY_PAUSE_PRICE}). Pausing buy orders.")
# #             return

# #         # Cancel all existing orders
# #         cancel_all_orders(PAIR_USDT)

# #         # Place buy orders (1:2 ratio, 5 buy orders)
# #         for i in range(MAX_BUY_ORDERS):  # 5 buy orders
# #             buy_price = current_price_usdt * (1 - (BUY_SPREAD[0] + (BUY_SPREAD[1] - BUY_SPREAD[0]) * i / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR_USDT, buy_amount, buy_price)
# #             record_buy_order(buy_price, buy_amount)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders (2 times the buy orders: 10 sell orders)
# #         for i in range(MAX_SELL_ORDERS):  # 10 sell orders
# #             sell_price = current_price_usdt * (1 + (SELL_SPREAD[0] + (SELL_SPREAD[1] - SELL_SPREAD[0]) * i / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price_usdt
# #             bitrue.create_limit_sell_order(PAIR_USDT, sell_amount, sell_price)
# #             record_sell_order(sell_price, sell_amount)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def manage_usdt_balance():
# #     """
# #     Check the current USDT balance and adjust buy order size if reserves drop significantly.
# #     """
# #     balance = bitrue.fetch_balance()
# #     usdt_balance = balance.get('total', {}).get('USDT', 0)
# #     print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #     initial_balance = 200  # Set the initial balance as an example ($200)
# #     loss_threshold = 50  # If the loss is more than $50, adjust buy order size

# #     if usdt_balance < (initial_balance - loss_threshold):
# #         global TRADE_SIZE_BUY_USDT
# #         TRADE_SIZE_BUY_USDT = 3  # Reduce buy order size to $3 if USDT reserves drop significantly
# #         print("USDT reserves low. Reducing buy order size to $3.")

# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price for ZON/USDT
# #             current_price_usdt = fetch_price(PAIR_USDT)
            
# #             print(f"Current price of ZON/USDT: {current_price_usdt:.4f} USDT")

# #             # Manage USDT balance and adjust buy size if necessary
# #             manage_usdt_balance()

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price_usdt)
# #                 last_refresh_time = time.time()

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #             # Calculate and print profit
# #             total_profit = calculate_profit()

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay

# # if __name__ == "__main__":
# #     main()



















# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants for ZON/USDT trading pair
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = 4  # $4 worth of ZON for buy orders in USDT terms
# # TRADE_SIZE_SELL_USDT = 4  # $4 worth of ZON for sell orders in USDT terms
# # ORDER_REFRESH_INTERVAL = 60  # Cancel and recreate orders every 3 minutes
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = [0.02, 0.05]  # 2% to 5% below the current price for buy orders
# # SELL_SPREAD = [0.01, 0.03]  # 1% to 3% above the current price for sell orders
# # MAX_BUY_ORDERS = 5  # Max buy orders at any given time
# # MAX_SELL_ORDERS = 10  # Max sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds
# # MIN_PRICE_THRESHOLD = 0.010  # Minimum price threshold to trigger orders
# # BUY_PAUSE_PRICE = 0.125  # Pause buy orders if ZON/USDT price exceeds this threshold

# # # Tracking profit variables
# # buy_orders = []  # List to store buy orders (buy price, amount)
# # sell_orders = []  # List to store sell orders (sell price, amount)

# # # Example function to track a completed buy order
# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})
# #     print(f"Buy order recorded: {amount} ZON at {price} USDT")

# # # Example function to track a completed sell order
# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})
# #     print(f"Sell order recorded: {amount} ZON at {price} USDT")

# # # Function to calculate profit
# # def calculate_profit():
# #     total_profit = 0
# #     for buy_order, sell_order in zip(buy_orders, sell_orders):
# #         buy_price = buy_order['price']
# #         sell_price = sell_order['price']
# #         amount = sell_order['amount']

# #         # Calculate profit before fees
# #         profit_before_fees = (sell_price - buy_price) * amount

# #         # Deduct trading fees (example fee of 0.1%)
# #         fee = 0.001  # 0.1% fee
# #         fee_deducted = (buy_price + sell_price) * fee * amount  # total fee for both buy and sell

# #         # Calculate net profit after fees
# #         net_profit = profit_before_fees - fee_deducted
# #         total_profit += net_profit

# #     print(f"Total profit: {total_profit:.4f} USDT")
# #     return total_profit

# # def fetch_price(pair):
# #     """Fetch the last price for a given trading pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return ticker['last']

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(pair)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], pair)
# #         print(f"Canceled all open orders for {pair}.")
# #     except Exception as e:
# #         print(f"Error canceling orders for {pair}: {e}")
# #         time.sleep(RETRY_DELAY)

# # def place_spread_orders(current_price_usdt):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     Maintain a 1:2 buy to sell ratio and ensure price exceeds threshold.
# #     """
# #     try:
# #         # Skip placing orders if the price is below the minimum threshold
# #         if current_price_usdt < MIN_PRICE_THRESHOLD:
# #             print(f"Price too low: {current_price_usdt:.4f} USDT. Skipping order placement.")
# #             return

# #         # Pause buy orders if the price exceeds the defined threshold
# #         if current_price_usdt > BUY_PAUSE_PRICE:
# #             print(f"Price exceeds threshold ({BUY_PAUSE_PRICE}). Pausing buy orders.")
# #             return

# #         # Dynamically adjust buy and sell spreads based on market conditions
# #         buy_spread_dynamic = BUY_SPREAD[0] + (BUY_SPREAD[1] - BUY_SPREAD[0]) * (current_price_usdt / 0.02)
# #         sell_spread_dynamic = SELL_SPREAD[0] + (SELL_SPREAD[1] - SELL_SPREAD[0]) * (current_price_usdt / 0.02)

# #         print(f"Dynamic Buy Spread: {buy_spread_dynamic:.2f}, Dynamic Sell Spread: {sell_spread_dynamic:.2f}")

# #         # Cancel all existing orders
# #         cancel_all_orders(PAIR_USDT)

# #         # Place buy orders (1:2 ratio, 5 buy orders)
# #         for i in range(MAX_BUY_ORDERS):  # 5 buy orders
# #             buy_price = current_price_usdt * (1 - (buy_spread_dynamic * i / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR_USDT, buy_amount, buy_price)
# #             record_buy_order(buy_price, buy_amount)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders (2 times the buy orders: 10 sell orders)
# #         for i in range(MAX_SELL_ORDERS):  # 10 sell orders
# #             sell_price = current_price_usdt * (1 + (sell_spread_dynamic * i / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price_usdt
# #             bitrue.create_limit_sell_order(PAIR_USDT, sell_amount, sell_price)
# #             record_sell_order(sell_price, sell_amount)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def manage_usdt_balance():
# #     """
# #     Check the current USDT balance and adjust buy order size if reserves drop significantly.
# #     """
# #     balance = bitrue.fetch_balance()
# #     usdt_balance = balance.get('total', {}).get('USDT', 0)
# #     print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #     initial_balance = 200  # Set the initial balance as an example ($200)
# #     loss_threshold = 50  # If the loss is more than $50, adjust buy order size

# #     if usdt_balance < (initial_balance - loss_threshold):
# #         global TRADE_SIZE_BUY_USDT
# #         TRADE_SIZE_BUY_USDT = 3  # Reduce buy order size to $3 if USDT reserves drop significantly
# #         print("USDT reserves low. Reducing buy order size to $3.")

# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price for ZON/USDT
# #             current_price_usdt = fetch_price(PAIR_USDT)
            
# #             print(f"Current price of ZON/USDT: {current_price_usdt:.4f} USDT")

# #             # Manage USDT balance and adjust buy size if necessary
# #             manage_usdt_balance()

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price_usdt)
# #                 last_refresh_time = time.time()

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #             # Calculate and print profit
# #             total_profit = calculate_profit()

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay

# # if __name__ == "__main__":
# #     main()















# # import ccxt
# # import time

# # # Bitrue API credentials
# # api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # # Connect to Bitrue using ccxt
# # bitrue = ccxt.bitrue({
# #     'apiKey': api_key,
# #     'secret': api_secret,
# #     'enableRateLimit': True
# # })

# # # Constants for ZON/USDT trading pair
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = 4  # $4 worth of ZON for buy orders in USDT terms
# # TRADE_SIZE_SELL_USDT = 4  # $4 worth of ZON for sell orders in USDT terms
# # ORDER_REFRESH_INTERVAL = 60  # Cancel and recreate orders every 60 seconds
# # TRADE_INTERVAL = 60  # Execute trades every 60 seconds
# # BUY_SPREAD = [0.01, 0.02]  # Tightened spread for buy orders
# # SELL_SPREAD = [0.005, 0.01]  # Tightened spread for sell orders
# # MAX_BUY_ORDERS = 5  # Max buy orders at any given time
# # MAX_SELL_ORDERS = 10  # Max sell orders at any given time
# # RETRY_DELAY = 5  # Retry delay in seconds
# # MIN_PRICE_THRESHOLD = 0.010  # Minimum price threshold to trigger orders
# # BUY_PAUSE_PRICE = 0.125  # Pause buy orders if ZON/USDT price exceeds this threshold

# # # Tracking profit variables
# # buy_orders = []  # List to store buy orders (buy price, amount)
# # sell_orders = []  # List to store sell orders (sell price, amount)

# # # Example function to track a completed buy order
# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})
# #     print(f"Buy order recorded: {amount} ZON at {price} USDT")

# # # Example function to track a completed sell order
# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})
# #     print(f"Sell order recorded: {amount} ZON at {price} USDT")

# # # Function to calculate profit
# # def calculate_profit():
# #     total_profit = 0
# #     for buy_order, sell_order in zip(buy_orders, sell_orders):
# #         buy_price = buy_order['price']
# #         sell_price = sell_order['price']
# #         amount = sell_order['amount']

# #         # Calculate profit before fees
# #         profit_before_fees = (sell_price - buy_price) * amount

# #         # Deduct trading fees (example fee of 0.1%)
# #         fee = 0.001  # 0.1% fee
# #         fee_deducted = (buy_price + sell_price) * fee * amount  # total fee for both buy and sell

# #         # Calculate net profit after fees
# #         net_profit = profit_before_fees - fee_deducted
# #         total_profit += net_profit

# #     print(f"Total profit: {total_profit:.4f} USDT")
# #     return total_profit

# # def fetch_price(pair):
# #     """Fetch the last price for a given trading pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return ticker['last']

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the specified pair."""
# #     try:
# #         open_orders = bitrue.fetch_open_orders(pair)
# #         for order in open_orders:
# #             bitrue.cancel_order(order['id'], pair)
# #         print(f"Canceled all open orders for {pair}.")
# #     except Exception as e:
# #         print(f"Error canceling orders for {pair}: {e}")
# #         time.sleep(RETRY_DELAY)

# # def place_spread_orders(current_price_usdt):
# #     """
# #     Place staggered buy and sell orders around the current price.
# #     Maintain a 1:2 buy to sell ratio and ensure price exceeds threshold.
# #     """
# #     try:
# #         # Skip placing orders if the price is below the minimum threshold
# #         if current_price_usdt < MIN_PRICE_THRESHOLD:
# #             print(f"Price too low: {current_price_usdt:.4f} USDT. Skipping order placement.")
# #             return

# #         # Pause buy orders if the price exceeds the defined threshold
# #         if current_price_usdt > BUY_PAUSE_PRICE:
# #             print(f"Price exceeds threshold ({BUY_PAUSE_PRICE}). Pausing buy orders.")

# #         # Cancel all existing orders
# #         cancel_all_orders(PAIR_USDT)

# #         # Place buy orders
# #         for i in range(MAX_BUY_ORDERS):
# #             buy_price = current_price_usdt * (1 - (BUY_SPREAD[0] + i * (BUY_SPREAD[1] - BUY_SPREAD[0]) / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             bitrue.create_limit_buy_order(PAIR_USDT, buy_amount, buy_price)
# #             record_buy_order(buy_price, buy_amount)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_SELL_ORDERS):
# #             sell_price = current_price_usdt * (1 + (SELL_SPREAD[0] + i * (SELL_SPREAD[1] - SELL_SPREAD[0]) / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price_usdt
# #             bitrue.create_limit_sell_order(PAIR_USDT, sell_amount, sell_price)
# #             record_sell_order(sell_price, sell_amount)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def match_internal_orders():
# #     """Match buy and sell orders internally if they overlap."""
# #     matched_orders = []
# #     for buy_order in buy_orders:
# #         for sell_order in sell_orders:
# #             if buy_order['price'] >= sell_order['price']:
# #                 matched_amount = min(buy_order['amount'], sell_order['amount'])
# #                 profit = (sell_order['price'] - buy_order['price']) * matched_amount
# #                 print(f"Internally matched {matched_amount:.2f} ZON for profit: {profit:.4f} USDT")

# #                 # Update orders
# #                 buy_order['amount'] -= matched_amount
# #                 sell_order['amount'] -= matched_amount
# #                 matched_orders.append(profit)

# #     # Clean up fully matched orders
# #     buy_orders[:] = [order for order in buy_orders if order['amount'] > 0]
# #     sell_orders[:] = [order for order in sell_orders if order['amount'] > 0]
# #     return sum(matched_orders)

# # def manage_usdt_balance():
# #     """
# #     Check the current USDT balance and adjust buy order size if reserves drop significantly.
# #     """
# #     balance = bitrue.fetch_balance()
# #     usdt_balance = balance.get('total', {}).get('USDT', 0)
# #     print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #     initial_balance = 200  # Set the initial balance as an example ($200)
# #     loss_threshold = 50  # If the loss is more than $50, adjust buy order size

# #     if usdt_balance < (initial_balance - loss_threshold):
# #         global TRADE_SIZE_BUY_USDT
# #         TRADE_SIZE_BUY_USDT = 3  # Reduce buy order size to $3 if USDT reserves drop significantly
# #         print("USDT reserves low. Reducing buy order size to $3.")

# # def main():
# #     last_refresh_time = time.time()

# #     while True:
# #         try:
# #             # Fetch current price for ZON/USDT
# #             current_price_usdt = fetch_price(PAIR_USDT)
            
# #             print(f"Current price of ZON/USDT: {current_price_usdt:.4f} USDT")

# #             # Manage USDT balance and adjust buy size if necessary
# #             manage_usdt_balance()

# #             # Check if it's time to refresh orders
# #             if time.time() - last_refresh_time > ORDER_REFRESH_INTERVAL:
# #                 place_spread_orders(current_price_usdt)
# #                 last_refresh_time = time.time()

# #             # Match internal orders
# #             internal_profit = match_internal_orders()
# #             print(f"Profit from internal matching: {internal_profit:.4f} USDT")

# #             # Wait for the trade interval
# #             time.sleep(TRADE_INTERVAL)

# #             # Calculate and print profit
# #             total_profit = calculate_profit()

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)  # Retry after a short delay

# # if __name__ == "__main__":
# #     main()




         



# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = Decimal("10")
# # TRADE_SIZE_SELL_USDT = Decimal("10")
# # BUY_SPREAD = (Decimal("0.01"), Decimal("0.05"))  # 1% to 5% below current price
# # SELL_SPREAD = (Decimal("0.01"), Decimal("0.05"))  # 1% to 5% above current price
# # MAX_BUY_ORDERS = 3
# # MAX_SELL_ORDERS = 3
# # MIN_PRICE_THRESHOLD = Decimal("0.0001")  # Allow orders at very low prices
# # RETRY_DELAY = 5
# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     'apiKey': API_KEY,
# #     'secret': API_SECRET,
# # })

# # # Order tracking
# # buy_orders = []
# # sell_orders = []
# # profit_internal_matching = Decimal("0")

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker['last']))

# # def fetch_balance():
# #     """Fetch the USDT balance."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance['free']['USDT']))

# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})

# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order['id'], pair)  # Provide the symbol (pair) as an argument

# # def place_spread_orders(current_price_usdt):
# #     """Place staggered buy and sell orders around the current price."""
# #     global buy_orders, sell_orders
# #     buy_orders.clear()
# #     sell_orders.clear()

# #     try:
# #         cancel_all_orders(PAIR_USDT)

# #         # Place buy orders
# #         for i in range(MAX_BUY_ORDERS):
# #             buy_price = current_price_usdt * (1 - (BUY_SPREAD[0] + i * (BUY_SPREAD[1] - BUY_SPREAD[0]) / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             if buy_price < MIN_PRICE_THRESHOLD:
# #                 print(f"Buy price {buy_price:.4f} below minimum threshold. Skipping.")
# #                 continue
# #             bitrue.create_limit_buy_order(PAIR_USDT, float(buy_amount), float(buy_price))
# #             record_buy_order(buy_price, buy_amount)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_SELL_ORDERS):
# #             sell_price = current_price_usdt * (1 + (SELL_SPREAD[0] + i * (SELL_SPREAD[1] - SELL_SPREAD[0]) / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price_usdt
# #             bitrue.create_limit_sell_order(PAIR_USDT, float(sell_amount), float(sell_price))
# #             record_sell_order(sell_price, sell_amount)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def match_internal_orders():
# #     """Simulate internal matching of buy and sell orders for profit tracking."""
# #     global profit_internal_matching
# #     matched = []
# #     for buy_order in buy_orders:
# #         for sell_order in sell_orders:
# #             if sell_order['price'] > buy_order['price']:
# #                 profit_internal_matching += (sell_order['price'] - buy_order['price']) * min(buy_order['amount'], sell_order['amount'])
# #                 matched.append((buy_order, sell_order))

# #     for buy_order, sell_order in matched:
# #         buy_orders.remove(buy_order)
# #         sell_orders.remove(sell_order)

# # def main():
# #     global profit_internal_matching
# #     total_profit = Decimal("0")

# #     while True:
# #         try:
# #             current_price_usdt = fetch_price(PAIR_USDT)
# #             usdt_balance = fetch_balance()

# #             print(f"Current price of {PAIR_USDT}: {current_price_usdt:.4f} USDT")
# #             print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #             if current_price_usdt < MIN_PRICE_THRESHOLD:
# #                 print(f"Price too low: {current_price_usdt:.4f} USDT. Skipping order placement.")
# #             else:
# #                 place_spread_orders(current_price_usdt)
# #                 match_internal_orders()

# #             total_profit = profit_internal_matching
# #             print(f"Profit from internal matching: {profit_internal_matching:.4f} USDT")
# #             print(f"Total profit: {total_profit:.4f} USDT")

# #             time.sleep(10)
# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()













# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT = Decimal("10")
# # TRADE_SIZE_SELL_USDT = Decimal("10")
# # BUY_SPREAD = (Decimal("0.01"), Decimal("0.05"))  # 1% to 5% below current price
# # SELL_SPREAD = (Decimal("0.01"), Decimal("0.05"))  # 1% to 5% above current price
# # MAX_BUY_ORDERS = 3
# # MAX_SELL_ORDERS = 3
# # MIN_PRICE_THRESHOLD = Decimal("0.0001")  # Allow orders at very low prices
# # RETRY_DELAY = 5


# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     'apiKey': API_KEY,
# #     'secret': API_SECRET,
# # })

# # # Order tracking
# # buy_orders = []
# # sell_orders = []
# # profit_internal_matching = Decimal("0")

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker['last']))

# # def fetch_balance():
# #     """Fetch the USDT balance."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance['free']['USDT']))

# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})

# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order['id'], pair)  # Provide the symbol (pair) as an argument

# # def place_spread_orders(current_price_usdt):
# #     """Place staggered buy and sell orders around the current price."""
# #     global buy_orders, sell_orders
# #     buy_orders.clear()
# #     sell_orders.clear()

# #     try:
# #         cancel_all_orders(PAIR_USDT)

# #         # Place buy orders
# #         for i in range(MAX_BUY_ORDERS):
# #             buy_price = current_price_usdt * (1 - (BUY_SPREAD[0] + i * (BUY_SPREAD[1] - BUY_SPREAD[0]) / (MAX_BUY_ORDERS - 1)))
# #             buy_amount = TRADE_SIZE_BUY_USDT / buy_price
# #             if buy_price < MIN_PRICE_THRESHOLD:
# #                 print(f"Buy price {buy_price:.4f} below minimum threshold. Skipping.")
# #                 continue
# #             bitrue.create_limit_buy_order(PAIR_USDT, float(buy_amount), float(buy_price))
# #             record_buy_order(buy_price, buy_amount)
# #             print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# #         # Place sell orders
# #         for i in range(MAX_SELL_ORDERS):
# #             sell_price = current_price_usdt * (1 + (SELL_SPREAD[0] + i * (SELL_SPREAD[1] - SELL_SPREAD[0]) / (MAX_SELL_ORDERS - 1)))
# #             sell_amount = TRADE_SIZE_SELL_USDT / current_price_usdt
# #             bitrue.create_limit_sell_order(PAIR_USDT, float(sell_amount), float(sell_price))
# #             record_sell_order(sell_price, sell_amount)
# #             print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# #     except Exception as e:
# #         print(f"Error placing spread orders: {e}")
# #         time.sleep(RETRY_DELAY)

# # def match_internal_orders():
# #     """Simulate internal matching of buy and sell orders for profit tracking."""
# #     global profit_internal_matching
# #     matched = []
# #     # Create copies of the lists to safely iterate and modify them
# #     buy_orders_copy = buy_orders[:]
# #     sell_orders_copy = sell_orders[:]
    
# #     for buy_order in buy_orders_copy:
# #         for sell_order in sell_orders_copy:
# #             if sell_order['price'] > buy_order['price']:
# #                 profit_internal_matching += (sell_order['price'] - buy_order['price']) * min(buy_order['amount'], sell_order['amount'])
# #                 matched.append((buy_order, sell_order))

# #     # Remove matched orders only if they exist in the lists
# #     for buy_order, sell_order in matched:
# #         if buy_order in buy_orders:
# #             buy_orders.remove(buy_order)
# #         if sell_order in sell_orders:
# #             sell_orders.remove(sell_order)

# # def main():
# #     global profit_internal_matching
# #     total_profit = Decimal("0")

# #     while True:
# #         try:
# #             current_price_usdt = fetch_price(PAIR_USDT)
# #             usdt_balance = fetch_balance()

# #             print(f"Current price of {PAIR_USDT}: {current_price_usdt:.4f} USDT")
# #             print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #             if current_price_usdt < MIN_PRICE_THRESHOLD:
# #                 print(f"Price too low: {current_price_usdt:.4f} USDT. Skipping order placement.")
# #             else:
# #                 place_spread_orders(current_price_usdt)
# #                 match_internal_orders()

# #             total_profit = profit_internal_matching
# #             print(f"Profit from internal matching: {profit_internal_matching:.4f} USDT")
# #             print(f"Total profit: {total_profit:.4f} USDT")

# #             time.sleep(10)
# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # BUY_SPREAD = Decimal("0.01")  # 1% below current price
# # SELL_SPREAD = Decimal("0.005")  # 0.5% above current price
# # TRADE_SIZE_BUY_USDT_1 = Decimal("2.00")  # $2 for buy in first interval
# # TRADE_SIZE_SELL_USDT_1 = Decimal("1.70")  # $1.7 for sell in first interval
# # TRADE_SIZE_BUY_USDT_2 = Decimal("1.70")  # $1.7 for buy in second interval
# # TRADE_SIZE_SELL_USDT_2 = Decimal("2.00")  # $2 for sell in second interval
# # MIN_ORDER_VALUE = Decimal("1.00")  # Minimum order value in USDT (for Bitrue)
# # MAX_ORDERS = 1
# # RETRY_DELAY = 5

# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     'apiKey': API_KEY,
# #     'secret': API_SECRET,
# # })

# # # Order tracking
# # buy_orders = []
# # sell_orders = []

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker['last']))

# # def fetch_balance():
# #     """Fetch the USDT balance."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance['free']['USDT']))

# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})

# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order['id'], pair)  # Provide the symbol (pair) as an argument
# #     print("All orders cancelled.")

# # def place_buy_order(current_price_usdt, trade_size, spread):
# #     """Place a buy order at the current price minus spread."""
# #     buy_price = current_price_usdt * (1 - spread)
# #     # Ensure that the order value is at least the minimum required
# #     order_value = trade_size / buy_price
# #     if order_value < MIN_ORDER_VALUE:
# #         print(f"Buy order value too small. Adjusting trade size.")
# #         trade_size = MIN_ORDER_VALUE * buy_price

# #     buy_amount = trade_size / buy_price
# #     print(f"Placing buy order for {buy_amount:.2f} ZON at {buy_price:.4f} USDT")
# #     bitrue.create_limit_buy_order(PAIR_USDT, float(buy_amount), float(buy_price))
# #     record_buy_order(buy_price, buy_amount)
# #     print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# # def place_sell_order(current_price_usdt, trade_size, spread):
# #     """Place a sell order at the current price plus spread."""
# #     sell_price = current_price_usdt * (1 + spread)
# #     # Ensure that the order value is at least the minimum required
# #     order_value = trade_size / sell_price
# #     if order_value < MIN_ORDER_VALUE:
# #         print(f"Sell order value too small. Adjusting trade size.")
# #         trade_size = MIN_ORDER_VALUE * sell_price

# #     sell_amount = trade_size / sell_price
# #     print(f"Placing sell order for {sell_amount:.2f} ZON at {sell_price:.4f} USDT")
# #     bitrue.create_limit_sell_order(PAIR_USDT, float(sell_amount), float(sell_price))
# #     record_sell_order(sell_price, sell_amount)
# #     print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# # def main():
# #     buy_next = True  # Flag to alternate between buy and sell

# #     while True:
# #         try:
# #             current_price_usdt = fetch_price(PAIR_USDT)
# #             usdt_balance = fetch_balance()

# #             print(f"Current price of {PAIR_USDT}: {current_price_usdt:.4f} USDT")
# #             print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #             # Cancel previous orders to avoid conflicts
# #             cancel_all_orders(PAIR_USDT)

# #             # Alternate buy and sell actions
# #             if buy_next:
# #                 # First interval: Buy $2 and Sell $1.7
# #                 place_buy_order(current_price_usdt, TRADE_SIZE_BUY_USDT_1, BUY_SPREAD)
# #                 place_sell_order(current_price_usdt, TRADE_SIZE_SELL_USDT_1, SELL_SPREAD)
# #             else:
# #                 # Second interval: Reverse logic (Buy $1.7 and Sell $2)
# #                 place_buy_order(current_price_usdt, TRADE_SIZE_BUY_USDT_2, BUY_SPREAD)
# #                 place_sell_order(current_price_usdt, TRADE_SIZE_SELL_USDT_2, SELL_SPREAD)

# #             # Switch action for next interval
# #             buy_next = not buy_next

# #             time.sleep(60)  # Wait 1 minute (or adjust interval as needed)

# #         except Exception as e:
# #             print(f"Error in main loop: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()


















# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # TRADE_SIZE_BUY_USDT_1 = Decimal("2.00")  # Market buy $2 at current price
# # TRADE_SIZE_SELL_USDT_1 = Decimal("1.30")  # Market sell $1.3 at current price
# # TRADE_SIZE_BUY_USDT_2 = Decimal("1.70")  # Market buy $1.7 at current price
# # TRADE_SIZE_SELL_USDT_2 = Decimal("1.30")  # Market sell $1.3 at current price

# # BUY_SPREAD_1 = Decimal("0.01")  # 1% below current price for buy order
# # BUY_SPREAD_2 = Decimal("0.02")  # 2% below current price for buy order
# # SELL_SPREAD_1 = Decimal("0.005")  # 0.5% above current price for sell order
# # SELL_SPREAD_2 = Decimal("0.01")  # 1% above current price for sell order
# # MIN_ORDER_VALUE = Decimal("1.00")  # Minimum order value in USDT
# # RESERVE_THRESHOLD = Decimal("150.00")  # Reserve threshold to stop the bot (example 150 USDT)
# # RETRY_DELAY = 5
# # CANDLE_INTERVAL = '1m'  # 1-minute candles

# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     'apiKey': API_KEY,
# #     'secret': API_SECRET,
# # })

# # # Order tracking
# # buy_orders = []
# # sell_orders = []

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker['last']))

# # def fetch_balance():
# #     """Fetch the USDT balance."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance['free']['USDT']))

# # def record_buy_order(price, amount):
# #     buy_orders.append({'price': price, 'amount': amount})

# # def record_sell_order(price, amount):
# #     sell_orders.append({'price': price, 'amount': amount})

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order['id'], pair)

# # def place_buy_order(current_price_usdt, trade_size, spread):
# #     """Place a buy order at the current price adjusted with spread."""
# #     buy_price = current_price_usdt * (1 - spread)
# #     order_value = trade_size / buy_price

# #     if order_value < MIN_ORDER_VALUE:
# #         print(f"Buy order value too small. Adjusting trade size.")
# #         trade_size = MIN_ORDER_VALUE * buy_price

# #     buy_amount = trade_size / buy_price
# #     bitrue.create_limit_buy_order(PAIR_USDT, float(buy_amount), float(buy_price))
# #     record_buy_order(buy_price, buy_amount)
# #     print(f"Buy order placed: {buy_amount:.2f} ZON at {buy_price:.4f} USDT")

# # def place_sell_order(current_price_usdt, trade_size, spread):
# #     """Place a sell order at the current price adjusted with spread."""
# #     sell_price = current_price_usdt * (1 + spread)
# #     order_value = trade_size / sell_price

# #     if order_value < MIN_ORDER_VALUE:
# #         print(f"Sell order value too small. Adjusting trade size.")
# #         trade_size = MIN_ORDER_VALUE * sell_price

# #     sell_amount = trade_size / sell_price
# #     bitrue.create_limit_sell_order(PAIR_USDT, float(sell_amount), float(sell_price))
# #     record_sell_order(sell_price, sell_amount)
# #     print(f"Sell order placed: {sell_amount:.2f} ZON at {sell_price:.4f} USDT")

# # def place_market_buy_order(trade_size, current_price):
# #     """Execute a market buy order."""
# #     buy_amount = trade_size / current_price
# #     bitrue.create_market_buy_order(PAIR_USDT, float(buy_amount))
# #     print(f"Market buy order executed: {buy_amount:.2f} ZON at {current_price:.4f} USDT")

# # def place_market_sell_order(trade_size, current_price):
# #     """Execute a market sell order."""
# #     sell_amount = trade_size / current_price
# #     bitrue.create_market_sell_order(PAIR_USDT, float(sell_amount))
# #     print(f"Market sell order executed: {sell_amount:.2f} ZON at {current_price:.4f} USDT")

# # def fetch_latest_candle(pair):
# #     """Fetch the latest 1-minute candle for the pair."""
# #     ohlcv = bitrue.fetch_ohlcv(pair, timeframe=CANDLE_INTERVAL, limit=2)  # Fetch last 2 candles
# #     latest_candle = ohlcv[-1]  # Latest 1-minute candle
# #     close_price = Decimal(str(latest_candle[4]))  # Close price is the 5th element in OHLCV
# #     return close_price

# # def main():
# #     cycle = 1  # To alternate between cycles
# #     while True:
# #         try:
# #             # Fetch the latest 1-minute candle close price
# #             current_price_usdt = fetch_latest_candle(PAIR_USDT)
# #             usdt_balance = fetch_balance()

# #             print(f"Current price of {PAIR_USDT}: {current_price_usdt:.4f} USDT")
# #             print(f"Current USDT balance: {usdt_balance:.2f} USDT")

# #             # Check if the reserve balance is sufficient
# #             if usdt_balance < RESERVE_THRESHOLD:
# #                 print("Reserve balance too low! Pausing the bot.")
# #                 time.sleep(RETRY_DELAY)
# #                 continue  # Skip the trading logic and wait for a sufficient balance

# #             # Cancel previous orders before placing new ones
# #             cancel_all_orders(PAIR_USDT)

# #             if current_price_usdt >= Decimal("0.008"):
# #                 # Cycle 1 Logic (price >= 0.008):
# #                 place_buy_order(current_price_usdt, Decimal("2.00"), Decimal("0.01"))  # Buy order 1% below
# #                 place_buy_order(current_price_usdt, Decimal("2.00"), Decimal("0.02"))  # Buy order 2% below
# #                 place_market_buy_order(Decimal("2.00"), current_price_usdt)  # Market buy $2
# #                 place_sell_order(current_price_usdt, Decimal("1.30"), Decimal("0.005"))  # Sell order 0.5% above
# #                 place_sell_order(current_price_usdt, Decimal("1.30"), Decimal("0.01"))  # Sell order 1% above
# #                 place_market_sell_order(Decimal("1.30"), current_price_usdt)  # Market sell $1.30
# #                 cycle = 2  # Switch to Cycle 2 after this
# #             elif current_price_usdt >= Decimal("0.005"):
# #                 # Cycle 2 Logic (0.005 <= price < 0.008):
# #                 place_buy_order(current_price_usdt, Decimal("1.70"), Decimal("0.01"))  # Buy order 1% below
# #                 place_buy_order(current_price_usdt, Decimal("1.70"), Decimal("0.02"))  # Buy order 2% below
# #                 place_market_buy_order(Decimal("1.70"), current_price_usdt)  # Market buy $1.7
# #                 place_sell_order(current_price_usdt, Decimal("1.30"), Decimal("0.005"))  # Sell order 0.5% above
# #                 place_sell_order(current_price_usdt, Decimal("1.30"), Decimal("0.01"))  # Sell order 1% above
# #                 place_market_sell_order(Decimal("1.30"), current_price_usdt)  # Market sell $1.30
# #                 cycle = 1  # Switch to Cycle 1 after this

# #             time.sleep(RETRY_DELAY)  # Delay before the next cycle
# #         except Exception as e:
# #             print(f"Error: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()



































# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # TRADE_AMOUNT_CYCLE1 = {"buy": Decimal("2.00"), "sell": Decimal("1.30")}
# # TRADE_AMOUNT_CYCLE2 = {"buy": Decimal("1.70"), "sell": Decimal("1.30")}
# # BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# # SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# # MIN_PRICE_THRESHOLD = Decimal("0.005")
# # HIGH_PRICE_THRESHOLD = Decimal("0.008")
# # RETRY_DELAY = 5  # Delay in seconds between cycles
# # RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# # TRADE_LIMIT = Decimal("5.00")  # Max trade size in USDT or ZON

# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     "apiKey": API_KEY,
# #     "secret": API_SECRET,
# # })

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker["last"]))

# # def fetch_balance(currency):
# #     """Fetch the balance of the specified currency."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance["free"][currency]))

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order["id"], pair)
# #     print(f"All open orders for {pair} canceled.")

# # def place_limit_order(order_type, pair, price, amount):
# #     """Place a limit order (buy or sell)."""
# #     if amount < Decimal("0.0001"):
# #         print("Amount too small, skipping order.")
# #         return
# #     try:
# #         if order_type == "buy":
# #             bitrue.create_limit_buy_order(pair, float(amount), float(price))
# #             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
# #         elif order_type == "sell":
# #             bitrue.create_limit_sell_order(pair, float(amount), float(price))
# #             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
# #     except Exception as e:
# #         print(f"Error placing {order_type} order: {e}")

# # def place_market_order(order_type, pair, amount):
# #     """Place a market order (buy or sell)."""
# #     try:
# #         if order_type == "buy":
# #             bitrue.create_market_buy_order(pair, float(amount))
# #             print(f"Market buy order executed: {amount} ZON")
# #         elif order_type == "sell":
# #             bitrue.create_market_sell_order(pair, float(amount))
# #             print(f"Market sell order executed: {amount} ZON")
# #     except Exception as e:
# #         print(f"Error placing market {order_type} order: {e}")

# # def execute_cycle(cycle, current_price):
# #     """Execute a trading cycle."""
# #     print(f"Executing Cycle {cycle}")

# #     if cycle == 1:
# #         trade_amounts = TRADE_AMOUNT_CYCLE1
# #     else:
# #         trade_amounts = TRADE_AMOUNT_CYCLE2

# #     # Step 1: Buy $X at market price
# #     buy_amount = trade_amounts["buy"] / current_price
# #     place_market_order("buy", PAIR_USDT, buy_amount)

# #     # Step 2: Place buy orders 1% and 2% below
# #     for spread in BUY_SPREAD:
# #         buy_price = current_price * (1 - spread)
# #         buy_amount = TRADE_LIMIT / buy_price
# #         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

# #     # Step 3: Sell $Y at market price
# #     sell_amount = trade_amounts["sell"] / current_price
# #     place_market_order("sell", PAIR_USDT, sell_amount)

# #     # Step 4: Place sell orders 0.5% and 1% above
# #     for spread in SELL_SPREAD:
# #         sell_price = current_price * (1 + spread)
# #         sell_amount = TRADE_LIMIT / sell_price
# #         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

# # def main():
# #     """Main bot loop."""
# #     while True:
# #         try:
# #             # Fetch balances
# #             usdt_balance = fetch_balance("USDT")
# #             zon_balance = fetch_balance("ZON")
# #             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

# #             # Check reserve threshold
# #             if usdt_balance < RESERVE_THRESHOLD:
# #                 print("Reserve balance too low! Pausing the bot.")
# #                 break

# #             # Fetch current price
# #             current_price = fetch_price(PAIR_USDT)
# #             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

# #             # Cancel all previous orders
# #             cancel_all_orders(PAIR_USDT)

# #             # Determine action based on price
# #             if current_price >= HIGH_PRICE_THRESHOLD:
# #                 print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
# #                 execute_cycle(1, current_price)
# #             elif current_price >= MIN_PRICE_THRESHOLD:
# #                 print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
# #                 execute_cycle(2, current_price)
# #             else:
# #                 print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

# #             # Delay before the next iteration
# #             time.sleep(RETRY_DELAY)

# #         except Exception as e:
# #             print(f"Error: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()













# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# # SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# # MIN_PRICE_THRESHOLD = Decimal("0.005")
# # HIGH_PRICE_THRESHOLD = Decimal("0.008")
# # RETRY_DELAY = 5  # Delay in seconds between cycles
# # RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# # MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
# # TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON

# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     "apiKey": API_KEY,
# #     "secret": API_SECRET,
# # })

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker["last"]))

# # def fetch_balance(currency):
# #     """Fetch the balance of the specified currency."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance["free"][currency]))

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order["id"], pair)
# #     print(f"All open orders for {pair} canceled.")

# # def place_limit_order(order_type, pair, price, amount):
# #     """Place a limit order (buy or sell)."""
# #     if amount < Decimal("0.0001"):
# #         print("Amount too small, skipping order.")
# #         return
# #     try:
# #         if order_type == "buy":
# #             bitrue.create_limit_buy_order(pair, float(amount), float(price))
# #             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
# #         elif order_type == "sell":
# #             bitrue.create_limit_sell_order(pair, float(amount), float(price))
# #             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
# #     except Exception as e:
# #         print(f"Error placing {order_type} order: {e}")

# # def place_market_order(order_type, pair, amount):
# #     """Place a market order (buy or sell)."""
# #     try:
# #         if order_type == "buy":
# #             bitrue.create_market_buy_order(pair, float(amount))
# #             print(f"Market buy order executed: {amount} ZON")
# #         elif order_type == "sell":
# #             bitrue.create_market_sell_order(pair, float(amount))
# #             print(f"Market sell order executed: {amount} ZON")
# #     except Exception as e:
# #         print(f"Error placing market {order_type} order: {e}")

# # def execute_cycle(cycle, current_price, usdt_balance):
# #     """Execute a trading cycle."""
# #     print(f"Executing Cycle {cycle}")

# #     # Step 1: Market Buy based on fixed amount of $10
# #     market_buy_amount = Decimal("10.00") / current_price  # Buy $10 worth of ZON
# #     place_market_order("buy", PAIR_USDT, market_buy_amount)

# #     # Step 2: Place buy orders 1% and 2% below the current price
# #     for spread in BUY_SPREAD:
# #         buy_price = current_price * (1 - spread)
# #         buy_amount = Decimal("2.00") / buy_price  # Buy $2 worth of ZON
# #         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

# #     # Step 3: Market Sell based on fixed amount of $10
# #     market_sell_amount = Decimal("10.00") / current_price  # Sell $10 worth of ZON
# #     place_market_order("sell", PAIR_USDT, market_sell_amount)

# #     # Step 4: Place sell orders 0.5% and 1% above the current price
# #     for spread in SELL_SPREAD:
# #         sell_price = current_price * (1 + spread)
# #         sell_amount = Decimal("2.00") / sell_price  # Sell $2 worth of ZON
# #         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

# # def main():
# #     """Main bot loop."""
# #     while True:
# #         try:
# #             # Fetch balances
# #             usdt_balance = fetch_balance("USDT")
# #             zon_balance = fetch_balance("ZON")
# #             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

# #             # Check reserve threshold
# #             if usdt_balance < RESERVE_THRESHOLD:
# #                 print("Reserve balance too low! Pausing the bot.")
# #                 break

# #             # Fetch current price
# #             current_price = fetch_price(PAIR_USDT)
# #             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

# #             # Cancel all previous orders
# #             cancel_all_orders(PAIR_USDT)

# #             # Determine action based on price
# #             if current_price >= HIGH_PRICE_THRESHOLD:
# #                 print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
# #                 execute_cycle(1, current_price, usdt_balance)
# #             elif current_price >= MIN_PRICE_THRESHOLD:
# #                 print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
# #                 execute_cycle(2, current_price, usdt_balance)
# #             else:
# #                 print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

# #             # Delay before the next iteration
# #             time.sleep(RETRY_DELAY)

# #         except Exception as e:
# #             print(f"Error: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()




# # import time
# # import ccxt
# # from decimal import Decimal

# # # Configuration
# # API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# # API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"
# # EXCHANGE = "bitrue"
# # PAIR_USDT = "ZON/USDT"
# # BUY_SPREAD = [Decimal("0.01"), Decimal("0.02")]  # 1% and 2% below market price
# # SELL_SPREAD = [Decimal("0.005"), Decimal("0.01")]  # 0.5% and 1% above market price
# # MIN_PRICE_THRESHOLD = Decimal("0.005")
# # HIGH_PRICE_THRESHOLD = Decimal("0.008")
# # RETRY_DELAY = 5  # Delay in seconds between cycles
# # RESERVE_THRESHOLD = Decimal("10.00")  # Reserve USDT threshold
# # MAX_TRADE_AMOUNT = Decimal("1.30")  # Max trade size in USDT
# # TRADE_LIMIT = Decimal("1.30")  # Max trade size in USDT or ZON
# # MARKET_BUY_INTERVAL = 1800  # 30 minutes in seconds
# # OTHER_ACTION_INTERVAL = 120  # 2 minutes for other actions

# # # Initialize exchange
# # bitrue = ccxt.bitrue({
# #     "apiKey": API_KEY,
# #     "secret": API_SECRET,
# # })

# # def fetch_price(pair):
# #     """Fetch the current price of the pair."""
# #     ticker = bitrue.fetch_ticker(pair)
# #     return Decimal(str(ticker["last"]))

# # def fetch_balance(currency):
# #     """Fetch the balance of the specified currency."""
# #     balance = bitrue.fetch_balance()
# #     return Decimal(str(balance["free"][currency]))

# # def cancel_all_orders(pair):
# #     """Cancel all open orders for the pair."""
# #     open_orders = bitrue.fetch_open_orders(pair)
# #     for order in open_orders:
# #         bitrue.cancel_order(order["id"], pair)
# #     print(f"All open orders for {pair} canceled.")

# # def place_limit_order(order_type, pair, price, amount):
# #     """Place a limit order (buy or sell)."""
# #     if amount < Decimal("0.0001"):
# #         print("Amount too small, skipping order.")
# #         return
# #     try:
# #         if order_type == "buy":
# #             bitrue.create_limit_buy_order(pair, float(amount), float(price))
# #             print(f"Buy order placed: {amount} ZON at {price:.4f} USDT")
# #         elif order_type == "sell":
# #             bitrue.create_limit_sell_order(pair, float(amount), float(price))
# #             print(f"Sell order placed: {amount} ZON at {price:.4f} USDT")
# #     except Exception as e:
# #         print(f"Error placing {order_type} order: {e}")

# # def place_market_order(order_type, pair, amount):
# #     """Place a market order (buy or sell)."""
# #     try:
# #         if order_type == "buy":
# #             bitrue.create_market_buy_order(pair, float(amount))
# #             print(f"Market buy order executed: {amount} ZON")
# #         elif order_type == "sell":
# #             bitrue.create_market_sell_order(pair, float(amount))
# #             print(f"Market sell order executed: {amount} ZON")
# #     except Exception as e:
# #         print(f"Error placing market {order_type} order: {e}")

# # def execute_cycle(cycle, current_price, usdt_balance):
# #     """Execute a trading cycle."""
# #     print(f"Executing Cycle {cycle}")

# #     # Calculate trade amount based on available balance
# #     trade_amount = min(TRADE_LIMIT / current_price, usdt_balance / current_price)

# #     # Step 1: Market Buy based on calculated trade amount
# #     place_market_order("buy", PAIR_USDT, trade_amount)

# #     # Step 2: Place buy orders 1% and 2% below the current price
# #     for spread in BUY_SPREAD:
# #         buy_price = current_price * (1 - spread)
# #         buy_amount = TRADE_LIMIT / buy_price
# #         place_limit_order("buy", PAIR_USDT, buy_price, buy_amount)

# #     # Step 3: Market Sell based on calculated trade amount
# #     place_market_order("sell", PAIR_USDT, trade_amount)

# #     # Step 4: Place sell orders 0.5% and 1% above the current price
# #     for spread in SELL_SPREAD:
# #         sell_price = current_price * (1 + spread)
# #         sell_amount = TRADE_LIMIT / sell_price
# #         place_limit_order("sell", PAIR_USDT, sell_price, sell_amount)

# # def main():
# #     """Main bot loop."""
# #     last_market_buy_time = time.time() - MARKET_BUY_INTERVAL  # Ensure a market buy happens immediately at the start
# #     last_other_action_time = time.time() - OTHER_ACTION_INTERVAL  # Ensure other actions are executed right away

# #     while True:
# #         try:
# #             # Fetch balances
# #             usdt_balance = fetch_balance("USDT")
# #             zon_balance = fetch_balance("ZON")
# #             print(f"USDT Balance: {usdt_balance:.2f}, ZON Balance: {zon_balance:.4f}")

# #             # Check reserve threshold
# #             if usdt_balance < RESERVE_THRESHOLD:
# #                 print("Reserve balance too low! Pausing the bot.")
# #                 break

# #             # Fetch current price
# #             current_price = fetch_price(PAIR_USDT)
# #             print(f"Current price of {PAIR_USDT}: {current_price:.4f} USDT")

# #             # Cancel all previous orders
# #             cancel_all_orders(PAIR_USDT)

# #             # Execute market buy every 30 minutes
# #             if time.time() - last_market_buy_time >= MARKET_BUY_INTERVAL:
# #                 print("Executing market buy order due to 30-minute interval.")
# #                 place_market_order("buy", PAIR_USDT, TRADE_LIMIT / current_price)
# #                 last_market_buy_time = time.time()

# #             # Execute other actions every 120 seconds (2 minutes)
# #             if time.time() - last_other_action_time >= OTHER_ACTION_INTERVAL:
# #                 print("Executing other actions (limit orders).")
# #                 execute_cycle(1, current_price, usdt_balance)
# #                 last_other_action_time = time.time()

# #             # Determine action based on price
# #             if current_price >= HIGH_PRICE_THRESHOLD:
# #                 print(f"Price >= {HIGH_PRICE_THRESHOLD}, implementing high price strategy.")
# #                 execute_cycle(1, current_price, usdt_balance)
# #             elif current_price >= MIN_PRICE_THRESHOLD:
# #                 print(f"Price >= {MIN_PRICE_THRESHOLD}, implementing low price strategy.")
# #                 execute_cycle(2, current_price, usdt_balance)
# #             else:
# #                 print(f"Price below {MIN_PRICE_THRESHOLD}, no action taken.")

# #             # Delay before the next iteration
# #             time.sleep(RETRY_DELAY)

# #         except Exception as e:
# #             print(f"Error: {e}")
# #             time.sleep(RETRY_DELAY)

# # if __name__ == "__main__":
# #     main()














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
SELL_WALL_THRESHOLD_MULTIPLIER = Decimal("2")  # Sell wall threshold multiplier
AVERAGE_ORDER_SIZE = Decimal("500")  # Average order size in ZON
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
    for sell_order in order_book:  # Corrected indentation
        price, quantity = sell_order
        if Decimal(quantity) > AVERAGE_ORDER_SIZE * Decimal(threshold_multiplier):
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

            # Place sell order only if sell wall is detected and below the sell wall
            if sell_wall_price:
                adjusted_sell_price = sell_wall_price * (1 - ADJUSTMENT_PERCENTAGE)
                if adjusted_sell_price < current_price:
                    place_limit_order("sell", PAIR_USDT, adjusted_sell_price, trade_amount)
                    print(f"Placed sell order below the detected wall at {adjusted_sell_price:.4f} USDT")

            # Place buy order below the adjusted price
            place_limit_order("buy", PAIR_USDT, adjusted_buy_price, trade_amount)

            # Delay before the next iteration
            time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    main()
