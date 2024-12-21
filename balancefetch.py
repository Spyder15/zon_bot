



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










