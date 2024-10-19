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
