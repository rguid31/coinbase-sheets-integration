import gspread
from google.oauth2.service_account import Credentials
from config import SHEET_ID, SHEET_RANGE

def connect_to_sheets():
    # Point to the JSON credentials file in the .env folder
    creds = Credentials.from_service_account_file('.env/google_service_account.json')
    
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).worksheet('Sheet1')
    return sheet

def write_to_sheet(data):
    sheet = connect_to_sheets()
    sheet.update(SHEET_RANGE, data)

def read_from_sheet():
    sheet = connect_to_sheets()
    return sheet.get(SHEET_RANGE)
