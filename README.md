# EAN Product Information Fetcher

This project fetches product information using an EAN (European Article Number), also known as a barcode number, and writes the data to an Excel file. If no product information is found for a given EAN, the script will still write the EAN to the Excel file with an empty product title.

## Setup and Running

1. **Install Required Libraries**: This project requires `requests`, `pandas`, and `openpyxl`. You can install these libraries using pip:

    ```bash
    pip install requests pandas openpyxl
    ```

2. **Configure API Details**: API details should be configured in a `config.json` file in the project directory. The file should be structured as follows:

    ```json
    {
        "url": "https://barcodes1.p.rapidapi.com/",
        "headers": {
            "X-RapidAPI-Key": "YOUR_API_KEY",
            "X-RapidAPI-Host": "barcodes1.p.rapidapi.com"
        }
    }
    ```
    Replace "YOUR_API_KEY" with your actual RapidAPI key.

3. **Run the Script**: Run the script using Python:

    ```bash
    python EAN_API.py
    ```

4. **Enter EANs**: When prompted, enter an EAN for which you'd like to fetch product information. If you want to stop the program, type "quit" or "stop".

## Error Handling

This script includes error handling for HTTP errors and general exceptions when making API requests, as well as exceptions when writing to the Excel file. If an error occurs, a message will be printed to the console.

## Limitations and Future Work

This script currently only supports single-threaded operation. In future versions, multithreading could be added to process multiple EANs in parallel.

The script currently fetches product information from a single API. In future versions, support for additional APIs could be added to increase the likelihood of finding product information for a given EAN.

## Contributions

Contributions to this project are welcome. Please submit a pull request or create an issue to propose changes or additions.
