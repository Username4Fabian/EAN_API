import csv
import re
import os
import requests
import pandas as pd
import json

# Load the API details from the config file
with open('config.json') as f:
    config = json.load(f)
url = config['url']
headers = config['headers']

# CSV related functions
def get_bez_nr(data):
    for i, header in enumerate(data[0]):
        if header.lower() in ["bezeichnung", "art.nr.", "type", "art.bez.", "name"]:
            return i
    return 0

def get_ean_nr(data):
    for i, header in enumerate(data[0]):
        if header.lower() in ["ean", "ean-code", "ean-nummer", "ean-nr", "ean-nr."]:
            return i
    return 0

def read_file(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        data = list(reader)
    return data

def preprocess(s):
    return re.sub(r"[^a-zA-Z0-9\s]", "", s.upper().strip())

def write_file(data, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(data)

def compare(original_data, combined_data):
    final_data = []
    header = original_data[0] + ["New EAN"]
    final_data.append(header)
    for row in original_data[1:]:
        original_bez = preprocess(row[get_bez_nr(original_data)])
        original_codes = re.findall(r"\b[0-9A-Z-]{4,}\b", original_bez)
        new_row = row + [""]
        if original_codes:
            for current_row in combined_data[1:]:
                current_ean = current_row[get_ean_nr(combined_data)]
                if not current_ean:
                    continue
                current_bez = preprocess(current_row[get_bez_nr(combined_data)])
                current_words = current_bez.split()
                match_found = False
                for original_code in original_codes:
                    if original_code in current_words:
                        new_row[-1] = current_ean
                        match_found = True
                        break
                if match_found:
                    break
        final_data.append(new_row)
    return final_data

def csv_comparison():
    original_path = "gr.csv"
    combined_data_dir = "input_files"

    original_data = read_file(original_path)

    combined_data = []
    for file_name in sorted(os.listdir(combined_data_dir)):
        if file_name.endswith(".csv"):
            combined_data.extend(read_file(os.path.join(combined_data_dir, file_name)))

    final_data = compare(original_data, combined_data)

    write_file(final_data, "gr_Final.csv")


# API related functions
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

def write_to_excel(ean, product_info, filename='products.xlsx'):
    product_info = product_info.get('product', {}) if product_info else {}
    ean = product_info.get('barcode_formats', {}).get('ean_13') if product_info else ean
    title = product_info.get('title') if product_info else ''

    df = pd.DataFrame({'EAN': [ean], 'Title': [title]})
    try:
        if os.path.exists(filename):
            df_existing = pd.read_excel(filename)
            df = pd.concat([df_existing, df], ignore_index=True)
        df.to_excel(filename, index=False)
        print(f'Product info for EAN {ean} has been written to the Excel file.')
    except Exception as e:
        print(f'Error occurred when writing to Excel file: {e}')

def api_query():
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


# Main function
def main():
    while True:
        print("Select an option:")
        print("1: CSV Comparison")
        print("2: API Query")
        print("3: Exit Program")
        
        option = input("Enter your option: ")
        if option == '1':
            csv_comparison()
        elif option == '2':
            api_query()
        elif option == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
