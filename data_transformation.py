def format_coinbase_data(raw_data):
    #Transform Coinbase API data into a format that can be written to Google Sheets.
    formatted_data = []
    for product in raw_data:
        formatted_data.append([
            product['product_id'],
            product['base_currency_id'],
            product['quote_currency_id'],
            product['price']
        ])
    return formatted_data
