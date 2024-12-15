# import ccxt

# # Replace with your actual API keys from Bitrue
# api_key = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
# api_secret = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'

# # Initialize the Bitrue API client
# bitrue = ccxt.bitrue({
#     'apiKey': api_key,
#     'secret': api_secret
# })

# # Fetch your account balance
# balance = bitrue.fetch_balance()

# # Print the balance
# print(balance)










# import ccxt
# import requests
# import time
# import hashlib
# import hmac

# # Your Bitrue API credentials
# api_key = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
# api_secret = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'

# # Function to get the server time from Bitrue
# def get_server_time():
#     url = "https://www.bitrue.com/api/v1/time"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         server_time = response.json()
#         return server_time['serverTime']
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching server time: {e}")
#         return None

# # Function to create a signature
# def create_signature(params, secret):
#     query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
#     return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# # Initialize Bitrue API client
# bitrue = ccxt.bitrue({
#     'apiKey': api_key,
#     'secret': api_secret,
# })

# # Get the server time
# server_timestamp = get_server_time()
# if not server_timestamp:
#     exit()

# # Get the current local timestamp (in milliseconds)
# local_timestamp = int(time.time() * 1000)

# # Ensure timestamp synchronization (difference should be less than 5 seconds)
# if abs(local_timestamp - server_timestamp) > 5000:
#     print(f"Warning: Local timestamp and server timestamp differ by more than 5 seconds! Using server time.")
#     timestamp = server_timestamp  # Use server timestamp if local time is too far off
# else:
#     timestamp = local_timestamp  # Use local timestamp if the difference is acceptable

# # Prepare parameters for the request (including the synchronized timestamp)
# params = {
#     'timestamp': str(timestamp),
#     'recvWindow': 5000  # Adjust this value if needed (ensure it's large enough)
# }

# # Generate the signature
# signature = create_signature(params, api_secret)
# params['signature'] = signature

# # Fetch balance with synchronized timestamp and correct parameters
# try:
#     balance = bitrue.fetch_balance({'params': params})
#     print(balance)
# except ccxt.BaseError as e:
#     print(f"Error: {e}")













import ccxt
import time
import requests
import hmac
import hashlib

# Your Bitrue API credentials
api_key = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
api_secret = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'


# Initialize Bitrue API client
bitrue = ccxt.bitrue({
    'apiKey': api_key,
    'secret': api_secret,
})

# Function to get the server time from Bitrue
def get_server_time():
    url = "https://www.bitrue.com/api/v1/time"
    try:
        response = requests.get(url)
        response.raise_for_status()
        server_time = response.json()
        return server_time['serverTime']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching server time: {e}")
        return None

# Function to create a signature
def create_signature(params, secret):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Get the server time
server_timestamp = get_server_time()
if not server_timestamp:
    exit()

# Get the current local timestamp (in milliseconds)
local_timestamp = int(time.time() * 1000)

# Ensure timestamp synchronization (difference should be less than 5 seconds)
if abs(local_timestamp - server_timestamp) > 5000:
    print(f"Warning: Local timestamp and server timestamp differ by more than 5 seconds! Using server time.")
    timestamp = server_timestamp  # Use server timestamp if local time is too far off
else:
    timestamp = local_timestamp  # Use local timestamp if the difference is acceptable

# Prepare parameters for the request (including the synchronized timestamp)
params = {
    'timestamp': str(timestamp),
    'recvWindow': 5000  # Adjust this value if needed (ensure it's large enough)
}

# Generate the signature
signature = create_signature(params, api_secret)
params['signature'] = signature

# Fetch the balance
try:
    balance = bitrue.fetch_balance({'params': params})

    # Filter and print balances for ZON and USDT
    print("Balance for ZON and USDT:")
    for token in ['ZON', 'USDT']:
        if token in balance:
            print(f"{token}: {balance[token]['total']}")
        else:
            print(f"{token}: Not found in balance")
except ccxt.BaseError as e:
    print(f"Error: {e}")


















# import time
# import requests
# import hashlib
# import hmac
# import json
# from urllib.parse import urlencode

# # Replace these with your actual API credentials
# API_KEY = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
# API_SECRET = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'

# # Function to create the signature required for the Bitrue API request
# def create_signature(params, secret):
#     query_string = urlencode(params)
#     return hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

# # Function to get the ZON/USDT balance for the specific account
# def get_balance():
#     url = 'https://www.bitrue.com/api/v1/account'

#     # Prepare parameters
#     params = {
#         'api_key': API_KEY,
#         'timestamp': int(time.time() * 1000)
#     }
#     params['signature'] = create_signature(params, API_SECRET)

#     try:
#         # Send the GET request to Bitrue API
#         response = requests.get(url, params=params)
#         data = response.json()

#         # Check if we have successfully received the account data
#         if 'code' in data and data['code'] == 200:
#             # Find the ZON/USDT balance
#             for asset in data['data']:
#                 if asset['asset'] == 'ZON':
#                     print(f"Balance for ZON: {asset['free']} ZON")
#                 elif asset['asset'] == 'USDT':
#                     print(f"Balance for USDT: {asset['free']} USDT")
#         else:
#             print("Error: Could not fetch account balance. Check your API credentials.")
#     except Exception as e:
#         print(f"Error: {e}")

# # Function to repeatedly check balance every 2 minutes
# def monitor_balance(interval_seconds=120):
#     while True:
#         get_balance()
#         time.sleep(interval_seconds)  # Wait for 2 minutes (120 seconds)

# # Call the function to monitor account balance
# monitor_balance()













# import ccxt
# import time
# import requests
# import hmac
# import hashlib

# # Your Bitrue API credentials
# api_key = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
# api_secret = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'

# # Initialize Bitrue API client
# bitrue = ccxt.bitrue({
#     'apiKey': api_key,
#     'secret': api_secret,
# })

# # Function to get the server time from Bitrue
# def get_server_time():
#     url = "https://www.bitrue.com/api/v1/time"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         server_time = response.json()
#         return server_time['serverTime']
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching server time: {e}")
#         return None

# # Function to create a signature
# def create_signature(params, secret):
#     query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
#     return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# # Get the server time
# server_timestamp = get_server_time()
# if not server_timestamp:
#     exit()

# # Get the current local timestamp (in milliseconds)
# local_timestamp = int(time.time() * 1000)

# # Ensure timestamp synchronization (difference should be less than 5 seconds)
# if abs(local_timestamp - server_timestamp) > 5000:
#     print(f"Warning: Local timestamp and server timestamp differ by more than 5 seconds! Using server time.")
#     timestamp = server_timestamp  # Use server timestamp if local time is too far off
# else:
#     timestamp = local_timestamp  # Use local timestamp if the difference is acceptable

# # Prepare parameters for the request (including the synchronized timestamp)
# params = {
#     'timestamp': str(timestamp),
#     'recvWindow': 5000  # Adjust this value if needed (ensure it's large enough)
# }

# # Generate the signature
# signature = create_signature(params, api_secret)
# params['signature'] = signature

# # Fetch the balance
# try:
#     balance = bitrue.fetch_balance({'params': params})
    
#     # Debugging: Print the entire balance to check its structure
#     print("Complete balance data:")
#     print(balance)

#     # Check if there is any non-zero balance for specific tokens
#     print("Tokens with a non-zero balance:")
#     for token, data in balance.items():
#         print(f"{token}: {data}")  # Show the token and its balance data
#         if data['total'] > 0:
#             print(f"{token}: {data['total']}")

# except ccxt.BaseError as e:
#     print(f"Error: {e}")





# import requests
# import hashlib
# import hmac
# import time

# # Your API and Secret Key
# api_key = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
# secret_key  = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'

# # Example function to get account balances
# def get_account_balances():
#     base_url = "https://www.bitrue.com"  # Bitrue's API URL
#     endpoint = "/api/v1/account"  # Example endpoint
#     timestamp = int(time.time() * 1000)

#     # Parameters
#     params = {
#         "timestamp": timestamp
#     }

#     # Generate signature
#     query_string = "&".join([f"{key}={value}" for key, value in params.items()])
#     signature = hmac.new(
#         secret_key.encode('utf-8'),
#         query_string.encode('utf-8'),
#         hashlib.sha256
#     ).hexdigest()

#     # Add signature to parameters
#     params["signature"] = signature

#     # Request headers
#     headers = {
#         "X-MBX-APIKEY": api_key
#     }

#     # Send GET request
#     response = requests.get(base_url + endpoint, headers=headers, params=params)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": response.text}

# # Call the function
# balances = get_account_balances()
# print(balances)











