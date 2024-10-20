from dotenv import load_dotenv
import os

# Load environment variables from the .env file located in the .env folder
load_dotenv(dotenv_path='.env/.env')  # Point to the new location of the .env file

# Access the API key and other environment variables

# Coinbase API
COINBASE_API_KEY = os.getenv('CDP_API_KEY')
BASE_URL = "https://api.coinbase.com/api/v3"
GOOGLE_CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH')

# Google Sheets details
SHEET_ID = os.getenv('SHEET_ID')
SHEET_RANGE = "Sheet1!A1:D20"

# Headers for Coinbase API
HEADERS = {
    'Authorization': f'Bearer {COINBASE_API_KEY}',
    'Content-Type': 'application/json'
}

# === Validation of Environment Variables ===
if not COINBASE_API_KEY:
    raise ValueError("Coinbase API key not found. Please check your .env file.")
if not SHEET_ID:
    raise ValueError("Google Sheet ID not found. Please check your .env file.")

print("Authorization Header:", HEADERS)
