import requests
import time
import hashlib
import hmac

# Replace with your own Bitrue API credentials
API_KEY = 'cc2c9d8f7883be5a649d62ab8431fddf5bfb023956ec42eaa5cb133d6f85af9b'
API_SECRET = '90eefc78e753a738d8477dd2e48ba82582dd8d91354feadc75b94f0d899d1093'

BASE_URL = 'https://api.bitrue.com'

def create_signature(params):
    """
    Create signature for API request
    """
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    query_string = query_string + f"&api_key={API_KEY}"
    return hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def get_open_orders(symbol):
    """
    Get all open orders for a given symbol (pair)
    """
    endpoint = '/api/v1/openOrders'
    params = {
        'symbol': symbol,
        'api_key': API_KEY,
        'timestamp': str(int(time.time() * 1000))
    }
    params['signature'] = create_signature(params)
    
    response = requests.get(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching open orders: {response.text}")
        return []

def cancel_order(symbol, order_id):
    """
    Cancel a specific order by order ID
    """
    endpoint = '/api/v1/order'
    params = {
        'symbol': symbol,
        'orderId': order_id,
        'api_key': API_KEY,
        'timestamp': str(int(time.time() * 1000))
    }
    params['signature'] = create_signature(params)
    
    response = requests.delete(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        print(f"Successfully cancelled order ID: {order_id}")
    else:
        print(f"Error cancelling order ID {order_id}: {response.text}")

def cancel_all_orders(symbol):
    """
    Cancel all open orders for a given symbol (pair)
    """
    open_orders = get_open_orders(symbol)
    
    if open_orders:
        for order in open_orders:
            order_id = order['orderId']
            cancel_order(symbol, order_id)
    else:
        print(f"No open orders found for {symbol}")

if __name__ == "__main__":
    symbol = 'ZONUSDT'  # The trading pair you want to cancel orders for
    cancel_all_orders(symbol)
