
import ccxt

API_KEY = "cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b"
API_SECRET = "90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093"

# Initialize exchange
bitrue = ccxt.bitrue({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

def test_api_connection():
    try:
        # Test API by fetching balance
        balance = bitrue.fetch_balance()
        print("API Connected successfully")
        print(f"Available balance: {balance['free']['USDT']}")
    except ccxt.BaseError as e:
        print(f"API Error: {str(e)}")
    except ccxt.NetworkError as e:
        print(f"Network Error: {str(e)}")

test_api_connection()
