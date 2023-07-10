import requests
import pandas as pd
import os
import json

# Load the API details from the config file
with open('config.json') as f:
    config = json.load(f)
url = config['url']
headers = config['headers']

# Function to get product information using EAN
def get_product_info(ean):
    querystring = {"query": ean}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None
    else:
        return response.json()

# Function to write product information to an Excel file
def write_to_excel(ean, product_info, filename='products.xlsx'):
    product_info = product_info.get('product', {}) if product_info else {}
    ean = product_info.get('barcode_formats', {}).get('ean_13') if product_info else ean
    title = product_info.get('title') if product_info else ''

    df = pd.DataFrame({'EAN': [ean], 'Title': [title]})  # Create a DataFrame with the EAN and title
    try:
        if os.path.exists(filename):  # Check if the file already exists
            df_existing = pd.read_excel(filename)  # If yes, load the existing data
            df = pd.concat([df_existing, df], ignore_index=True)  # Concatenate the new data with the existing data
        df.to_excel(filename, index=False)  # Write the data to an Excel file
        print(f'Product info for EAN {ean} has been written to the Excel file.')
    except Exception as e:
        print(f'Error occurred when writing to Excel file: {e}')

# Main function to get user input and write data to Excel
def main():
    while True:
        ean = input('Enter an EAN (or "quit" or "stop" to stop): ')
        if ean.lower() in ['quit', 'stop']:
            break
        product_info = get_product_info(ean)
        if product_info is None:
            print(f'No product info found for EAN {ean}.')
            continue
        try:
            write_to_excel(ean, product_info)
        except Exception as e:
            print(f'Error writing product info for EAN {ean} to the Excel file: {e}')

if __name__ == "__main__":
    main()
