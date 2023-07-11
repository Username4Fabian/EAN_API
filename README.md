# EAN Finder

## Description

EAN Finder is a Python-based project designed to process and analyze data related to product information. The program offers two primary functionalities:

1. **CSV Comparison**: This feature performs an in-depth comparison of data from multiple CSV files, focusing on specific fields and conditions. It's a powerful tool for comparing and matching product records, especially when you need to process and analyze large volumes of data.

2. **API Query**: This feature leverages the power of APIs to fetch detailed product information using EANs (European Article Numbers), a widely used barcode standard for retail products. This product information is then stored in an Excel file for easy access and further analysis.

## Features

### CSV Comparison

The CSV Comparison feature is designed to compare the contents of the `gr.csv` file with other CSV files located in the `input_files` directory. The comparison is based on specific fields recognized by their headers, like "bezeichnung", "art.nr.", "type", "art.bez.", "name" for the product name field, and "ean", "ean-code", "ean-nummer", "ean-nr", "ean-nr." for the EAN field. 

Here's a more detailed breakdown of the comparison process:

- **Preprocessing**: The application first preprocesses the data by removing any non-alphanumeric characters and converting all characters to uppercase. This helps standardize the data for accurate comparison.

- **Matching**: After preprocessing, the program identifies matching records based on specific conditions. It looks for matching "codes" in a certain field. 

- **Output**: The result of the comparison is saved in a new CSV file named `gr_Final.csv`. This file includes the original data along with a new column "New EAN" which contains the matched EANs.

### API Query

The API Query feature allows you to fetch product information from an API using EANs. Here's how it works:

- **Input**: The program will prompt you to enter an EAN. 

- **API Request**: Using the EAN provided, the program sends a request to the API specified in the `config.json` file.

- **Data Processing**: The program fetches product information from the API response and processes it.

- **Output**: The processed product information is then written to an Excel file named `products.xlsx`. Each row in the Excel file corresponds to one product, with the EAN and product title as the columns.

- **Repetition**: The program will continue to prompt you for EANs and fetch product information until you decide to stop by typing 'quit' or 'stop'.

## Usage

### Prerequisites

Before running the EAN Finder, ensure the following:

- You have Python installed on your system. The application has been developed and tested on Python 3.7+, but it should work with other versions as well.

- The `gr.csv` file and the files in the `input_files` directory are in the correct format and contain the necessary data.

- The `config.json` file contains the correct API URL and headers.

### Running the program

To run the program, navigate to the directory containing `EAN_Finder.py` in your terminal and execute the following command:

```bash
python EAN_Finder.py
```

After starting the program, you will be presented with a menu offering three options:

1. Perform CSV Comparison
2. Perform API Query
3. Exit Program

You can select an option by typing its corresponding number and pressing Enter. 

For options 1 and 2, the program will automatically process the data and save the results to the corresponding output files (`gr_Final.csv` for CSV Comparison and `products.xlsx` for API Query). For the API Query, you will be prompted to input an EAN for each query. You can stop this process by typing 'quit' or 'stop'.

## Configuration

The program requires a `config.json` file for the API details. This file must contain a `url` field for the API URL, and a `headers` field for the API headers.

Here's an example of how the `config.json` should look:

```json
{
    "url": "https://your-api-url.com",
    "headers": {
        "Your-Header-Key": "Your-Header-Value"
    }
}
```

Replace `"https://your-api-url.com"` with the URL of the API you're using, and `"Your-Header-Key"` and `"Your-Header-Value"` with the key and value of your API headers.

## Input Files

The `gr.csv` file and the files in the `input_files` directory are used for the CSV comparison function. The `gr.csv` file contains a list of product descriptions. The files in the `input_files` directory should be in CSV format and will be used for comparison. Make sure these files are in the correct format and contain the necessary data before running the CSV comparison function.

## API Used

The program uses an API to fetch product information based on EANs. Make sure you have the correct API URL and headers in the `config.json` file.
