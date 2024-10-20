import requests
from config import BASE_URL, HEADERS

def get_products():
    url = f"{BASE_URL}/brokerage/products"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error getting products: {response.status_code}")

def place_order(order_data):
    url = f"{BASE_URL}/brokerage/orders"
    response = requests.post(url, headers=HEADERS, json=order_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error placing order: {response.status_code}")

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        raise Exception("Bad Request: The request was malformed. Please verify the parameters.")
    elif response.status_code == 401:
        raise Exception("Unauthorized: API key is invalid or expired. Please check your credentials.")
    elif response.status_code == 403:
        raise Exception("Forbidden: You do not have permission to access this resource.")
    else:
        raise Exception(f"Error: Received status code {response.status_code}")
