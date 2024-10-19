from coinbase_api import get_products
from sheet_handler import write_to_sheet
from data_transformation import format_coinbase_data

def main():
    try:
        # Step 1: Fetch products from Coinbase API
        raw_products = get_products()
        
        # Step 2: Format the data for Google Sheets
        formatted_data = format_coinbase_data(raw_products)
        
        # Step 3: Write the formatted data to Google Sheets
        write_to_sheet(formatted_data)
        
        print("Data successfully written to Google Sheets.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
