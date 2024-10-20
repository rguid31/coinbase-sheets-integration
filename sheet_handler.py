import gspread
from google.oauth2.service_account import Credentials
from config import SHEET_ID, SHEET_RANGE
import os

def connect_to_sheets():
    try:
        creds_path = os.getenv('GOOGLE_CREDENTIALS_PATH', '.env/google_service_account.json')
        creds = Credentials.from_service_account_file(creds_path)
        
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SHEET_ID).worksheet('Sheet1')
        return sheet
    except FileNotFoundError:
        raise FileNotFoundError("Service account JSON file not found. Please check the path.")
    except gspread.exceptions.APIError as e:
        raise Exception(f"Failed to connect to Google Sheets: {e}")

def write_to_sheet(data, range=SHEET_RANGE):
    try:
        sheet = connect_to_sheets()
        sheet.update(range, data)
    except gspread.exceptions.APIError as e:
        raise Exception(f"Failed to write to Google Sheets: {e}")

def read_from_sheet(range=SHEET_RANGE):
    try:
        sheet = connect_to_sheets()
        return sheet.get(range)
    except gspread.exceptions.APIError as e:
        raise Exception(f"Failed to read from Google Sheets: {e}")
