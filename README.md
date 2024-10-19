# Coinbase-Google Sheets Integration

This project integrates Coinbase Advanced Trade API with Google Sheets to retrieve product information from Coinbase and write it to a Google Sheet.

## Setup

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with your API keys and Google Sheets details:
   ```
   CDP_API_KEY=your_coinbase_api_key
   SHEET_ID=your_google_sheet_id
   ```

4. Set up your Google Sheets API credentials and provide the path to the credentials file in `sheet_handler.py`.

5. Run the main script:
   ```
   python main.py
   ```

## Files

- **config.py**: Configuration for API keys, spreadsheet IDs, and headers.
- **coinbase_api.py**: Functions to interact with Coinbase API.
- **sheet_handler.py**: Functions to read from and write to Google Sheets.
- **data_transformation.py**: Helper functions to format data for Google Sheets.
- **main.py**: Main workflow to fetch data from Coinbase and write to Google Sheets.

