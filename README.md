# CSV and API Query Program

This program provides two functionalities:

1. CSV Comparison: Combines data from multiple CSV files, finds matches based on specific codes in the data, and writes the combined data with additional columns to a new CSV file.

2. API Query: Fetches product information from an API using the EAN (European Article Number) as input and writes the fetched data to an Excel file.

## Setup

### Prerequisites

- Python 3.x installed
- Required Python libraries: `requests`, `pandas`, `json`
- CSV files for the CSV comparison functionality
- A `config.json` file containing the API details for the API query functionality

To install the required Python libraries, you can use pip:

```bash
pip install requests pandas
```

### Configuration

The program expects a `config.json` file in the same directory as the main Python script. This file should contain the API details for the API query functionality. The structure of the `config.json` file should be as follows:

```json
{
  "url": "API_URL_HERE",
  "headers": {
    "HEADER_NAME": "HEADER_VALUE",
    "HEADER_NAME": "HEADER_VALUE"
  }
}
```

Replace `"API_URL_HERE"` with the URL of the API, and replace `"HEADER_NAME"` and `"HEADER_VALUE"` with the names and values of the headers required for the API.

## Usage

### Running the Program

Run the main Python script (`main.py` or whatever you have named the main script):

```bash
python main.py
```

You will be presented with a menu:

```
Select an option:
1: CSV Comparison
2: API Query
3: Exit Program
```

Enter `1` to run the CSV comparison functionality or `2` to run the API query functionality. Enter `3` to exit the program.

### CSV Comparison

For the CSV comparison functionality, the program expects CSV files in a directory named `input_files`. It reads data from all CSV files in this directory, combines them, finds matches based on specific codes, and writes the combined data with additional columns to a new CSV file named `gr_Final.csv`.

The specific codes used for matching are alphanumeric strings at least four characters long. The program looks for these codes in the columns whose headers are any of the following: "bezeichnung", "art.nr.", "type", "art.bez.", "name". If a match is found in any row from the combined data, the EAN from that row (from the column with a header containing "ean") is added to the original row in the new column "New EAN".

### API Query

For the API query functionality, the program asks the user to enter an EAN. It then fetches product information from the API and writes this information to an Excel file named `products.xlsx`. If the file already exists, the new data is appended to it; otherwise, a new file is created.

The data written to the Excel file includes the EAN and the title of the product. The title is fetched from the API response.

To stop the program, enter `quit` or `stop`.

## Exit Program

At any time during the operation of the program, you can choose to exit by selecting the "Exit Program" option in the main menu or by entering 'quit' or 'stop' during the API Query operation.
