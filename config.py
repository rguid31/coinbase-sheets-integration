import os
from dotenv import load_dotenv

# Load environment variables from the .env file located in the .env folder
load_dotenv(dotenv_path='.env/.env')  # Point to the new location of the .env file

# Access the API key and other environment variables
# Coinbase API
COINBASE_API_KEY = os.getenv('CDP_API_KEY')
BASE_URL = "https://api.coinbase.com/api/v3"

# Google Sheets details
SHEET_ID = os.getenv('SHEET_ID')
SHEET_RANGE = "Sheet1!A1:D20"

# Headers for Coinbase API
HEADERS = {
    'Authorization': f'Bearer {COINBASE_API_KEY}',
    'Content-Type': 'application/json'
}
