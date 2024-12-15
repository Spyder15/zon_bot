# import ccxt
# import time

# # Set up the API keys for Bitrue
# api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # Create a connection to Bitrue using ccxt
# bitrue = ccxt.bitrue({
#     'apiKey': api_key,
#     'secret': api_secret,
#     'enableRateLimit': True,  # Enable rate limiting
# })

# # Synchronize time
# def sync_time():
#     server_time = bitrue.fetch_time()
#     local_time = int(time.time() * 1000)
#     offset = server_time - local_time
#     print(f"Time offset: {offset} ms")
#     return offset

# # Adjust your nonce function
# time_offset = sync_time()

# def nonce():
#     return int(time.time() * 1000) + time_offset

# bitrue.nonce = nonce  # Overwrite CCXT's default nonce

# def fetch_order_book(pair):
#     try:
#         order_book = bitrue.fetch_order_book(pair)
#         print(f"Order book fetched for {pair}")
#         return order_book
#     except Exception as e:
#         print(f"Error fetching order book: {e}")

# def calculate_order_prices(order_book):
#     highest_bid = order_book['bids'][0][0]  # Highest buy price
#     lowest_ask = order_book['asks'][0][0]  # Lowest sell price

#     # Calculate the 1.5% spread
#     spread = 0.015  # 1.5% spread
#     buy_price = highest_bid * (1 - spread)  # Buy price (lower)
#     sell_price = lowest_ask * (1 + spread)  # Sell price (higher)

#     print(f"Buy Price: {buy_price}, Sell Price: {sell_price}")
#     return buy_price, sell_price

# def calculate_order_amount(pair, daily_target):
#     ticker = bitrue.fetch_ticker(pair)  # Fetch the latest price
#     price = ticker['last']  # Current price of the pair
#     order_amount = daily_target / price  # Amount to trade to meet $2000 volume
#     print(f"Order amount: {order_amount} {pair}")
#     return order_amount

# def place_orders(pair, buy_price, sell_price, order_amount):
#     try:
#         # Place Buy order
#         buy_order = bitrue.create_limit_buy_order(pair, order_amount, buy_price)
#         print(f"Buy order placed: {buy_order}")

#         # Place Sell order
#         sell_order = bitrue.create_limit_sell_order(pair, order_amount, sell_price)
#         print(f"Sell order placed: {sell_order}")
#     except Exception as e:
#         print(f"Error placing orders: {e}")

# def manage_orders(pair, order_amount):
#     try:
#         order_book = fetch_order_book(pair)  # Fetch the latest order book
#         buy_price, sell_price = calculate_order_prices(order_book)  # Calculate new buy/sell prices

#         # Cancel old orders
#         open_orders = bitrue.fetch_open_orders(pair)  # Get any open orders
#         if open_orders:
#             print("Adjusting orders...")
#             for order in open_orders:
#                 bitrue.cancel_order(order['id'], pair)  # Cancel the order

#         # Place new buy and sell orders
#         place_orders(pair, buy_price, sell_price, order_amount)

#     except Exception as e:
#         print(f"Error managing orders: {e}")

# def main():
#     print("Starting bot...")
#     pair = "ZON/USDT"  # Trading pair
#     daily_target = 2000  # Target volume for the day ($2000)

#     # Calculate the amount needed to hit the target
#     order_amount = calculate_order_amount(pair, daily_target)

#     while True:
#         try:
#             # Manage orders: place or adjust orders if needed
#             manage_orders(pair, order_amount)

#             time.sleep(5)  # Sleep for 5 seconds to avoid hitting API rate limits

#         except Exception as e:
#             print(f"Error in main loop: {e}")
#             time.sleep(5)  # Retry after a delay

# if __name__ == "__main__":
#     main()












# import ccxt
# import time

# # Set up the API keys for Bitrue
# api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
# api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# # Create a connection to Bitrue using ccxt
# bitrue = ccxt.bitrue({
#     'apiKey': api_key,
#     'secret': api_secret,
#     'enableRateLimit': True,  # Enable rate limiting
# })

# # Synchronize time
# def sync_time():
#     server_time = bitrue.fetch_time()
#     local_time = int(time.time() * 1000)
#     offset = server_time - local_time
#     print(f"Time offset: {offset} ms")
#     return offset

# # Adjust your nonce function
# time_offset = sync_time()

# def nonce():
#     return int(time.time() * 1000) + time_offset

# bitrue.nonce = nonce  # Overwrite CCXT's default nonce

# def fetch_balance():
#     try:
#         balance = bitrue.fetch_balance()
#         return balance
#     except Exception as e:
#         print(f"Error fetching balance: {e}")
#         return None

# def fetch_order_book(pair):
#     try:
#         order_book = bitrue.fetch_order_book(pair)
#         print(f"Order book fetched for {pair}")
#         return order_book
#     except Exception as e:
#         print(f"Error fetching order book: {e}")
#         return None

# def calculate_order_amount(pair, target_usdt_amount):
#     ticker = bitrue.fetch_ticker(pair)  # Fetch the latest price
#     price = ticker['last']  # Current price of the pair
#     order_amount = target_usdt_amount / price  # Amount to trade to meet target
#     print(f"Order amount: {order_amount} {pair}")
#     return order_amount

# def place_orders(pair, buy_price, sell_price, order_amount):
#     try:
#         # Place Buy order with $500 worth of ZON
#         buy_order = bitrue.create_limit_buy_order(pair, order_amount, buy_price)
#         print(f"Buy order placed: {buy_order}")

#         # Place Sell order
#         sell_order = bitrue.create_limit_sell_order(pair, order_amount, sell_price)
#         print(f"Sell order placed: {sell_order}")
#     except Exception as e:
#         print(f"Error placing orders: {e}")

# def manage_orders(pair, order_amount):
#     try:
#         order_book = fetch_order_book(pair)  # Fetch the latest order book
#         highest_bid = order_book['bids'][0][0]  # Highest buy price
#         lowest_ask = order_book['asks'][0][0]  # Lowest sell price

#         # Calculate the 1.5% spread
#         spread = 0.015  # 1.5% spread
#         buy_price = highest_bid * (1 - spread)  # Buy price (lower)
#         sell_price = lowest_ask * (1 + spread)  # Sell price (higher)

#         print(f"Buy Price: {buy_price}, Sell Price: {sell_price}")
        
#         # Cancel any open orders
#         open_orders = bitrue.fetch_open_orders(pair)
#         if open_orders:
#             print("Adjusting orders...")
#             for order in open_orders:
#                 bitrue.cancel_order(order['id'], pair)

#         # Place new buy and sell orders
#         place_orders(pair, buy_price, sell_price, order_amount)

#     except Exception as e:
#         print(f"Error managing orders: {e}")

# def main():
#     print("Starting bot...")
#     pair = "ZON/USDT"  # Trading pair
#     target_usdt_amount = 500  # Target volume for the first trade ($500)

#     # Calculate the amount needed to buy $500 worth of ZON
#     order_amount = calculate_order_amount(pair, target_usdt_amount)

#     while True:
#         try:
#             # Manage orders: place or adjust orders if needed
#             manage_orders(pair, order_amount)

#             time.sleep(5)  # Sleep for 5 seconds to avoid hitting API rate limits

#         except Exception as e:
#             print(f"Error in main loop: {e}")
#             time.sleep(5)  # Retry after a delay

# if __name__ == "__main__":
#     main()














import ccxt
import time

# Bitrue API credentials
api_key = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
api_secret = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# Connect to Bitrue using ccxt
bitrue = ccxt.bitrue({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
})

def is_price_trending_up(pair, interval_seconds=30):
    """
    Check if the price is trending upward over a 30-second interval.
    """
    try:
        # Fetch the current price
        ticker = bitrue.fetch_ticker(pair)
        initial_price = ticker['last']
        print(f"Initial price: {initial_price}")

        # Wait for the interval duration
        time.sleep(interval_seconds)

        # Fetch the price after the interval
        ticker = bitrue.fetch_ticker(pair)
        final_price = ticker['last']
        print(f"Final price: {final_price}")

        # Return True if the price has increased
        return final_price > initial_price

    except Exception as e:
        print(f"Error checking price trend: {e}")
        return False  # Default to no trade if error occurs

def place_staggered_orders(pair, capital_allocation, token_allocation, current_price):
    """
    Place staggered buy and sell orders based on the strategy.
    """
    try:
        # Unpack allocations
        buy_usdt = capital_allocation['buy']
        sell_zon = token_allocation['sell']

        # Define buy order prices
        buy_orders = [
            {'price': current_price * 0.99, 'amount': buy_usdt * 0.25 / (current_price * 0.99)},
            {'price': current_price * 0.98, 'amount': buy_usdt * 0.25 / (current_price * 0.98)},
            {'price': current_price * 0.97, 'amount': buy_usdt * 0.50 / (current_price * 0.97)},
        ]

        # Define sell order prices
        sell_orders = [
            {'price': current_price * 1.03, 'amount': sell_zon * 0.05},
            {'price': current_price * 1.05, 'amount': sell_zon * 0.10},
            {'price': current_price * 1.08, 'amount': sell_zon * 0.20},
        ]

        # Place buy orders
        for order in buy_orders:
            bitrue.create_limit_buy_order(pair, order['amount'], order['price'])
            print(f"Buy order placed: {order['amount']} at {order['price']}")

        # Place sell orders
        for order in sell_orders:
            bitrue.create_limit_sell_order(pair, order['amount'], order['price'])
            print(f"Sell order placed: {order['amount']} at {order['price']}")

    except Exception as e:
        print(f"Error placing staggered orders: {e}")

def small_trade_simulation(pair, current_price):
    """
    Execute small alternating buy/sell trades for volume simulation.
    """
    try:
        # Alternating small buy and sell trades
        buy_amount = 10 / current_price
        sell_amount = 10 / current_price

        # Buy trade
        bitrue.create_limit_buy_order(pair, buy_amount, current_price)
        print(f"Simulated buy: {buy_amount} at {current_price}")

        # Small delay
        time.sleep(2)

        # Sell trade
        bitrue.create_limit_sell_order(pair, sell_amount, current_price * 1.02)
        print(f"Simulated sell: {sell_amount} at {current_price * 1.02}")

    except Exception as e:
        print(f"Error in small trade simulation: {e}")

def main():
    pair = "ZON/USDT"
    capital_allocation = {'buy': 200, 'defense': 300}
    token_allocation = {'sell': 1_000_000, 'reserve': 700_000}
    trade_interval = 30  # 30 seconds interval

    while True:
        try:
            # Fetch current price
            ticker = bitrue.fetch_ticker(pair)
            current_price = ticker['last']
            print(f"Current price of {pair}: {current_price}")

            # Check if the price is trending upward over 30 seconds
            if is_price_trending_up(pair, interval_seconds=trade_interval):
                print("Price is trending upward. Proceeding with trades.")

                # Step 1: Place staggered buy/sell orders
                place_staggered_orders(pair, capital_allocation, token_allocation, current_price)

                # Step 2: Simulate small alternating trades
                small_trade_simulation(pair, current_price)
            else:
                print("Price is not trending upward. Skipping this interval.")

            # Sleep for trade interval before checking again
            time.sleep(trade_interval)

        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(10)  # Retry after a short delay

if __name__ == "__main__":
    main()