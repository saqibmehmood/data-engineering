import pandas as pd
import os
import io
import requests
import zipfile
from io import BytesIO
import openpyxl
from sqlalchemy import create_engine, select, func
from sqlalchemy.exc import SQLAlchemyError
from app.utils.constants import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


# SQLAlchemy engine
engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# URL of the ZIP file
url = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
zip_file_name = "online_retail.zip"
xlsx_file_name = "retail.xlsx"
csv_file_name = "retail.csv"

def download_and_extract_zip(url, extract_to='.'):
    if os.path.isfile("retail.csv"):
        print(f"File is already downloaded.")
        return True
    # Download the ZIP file
    response = requests.get(url)

    if response.status_code == 200:
        # Extract the Excel file from the ZIP archive
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            # Find the Excel file in the archive
            xlsx_files = [name for name in zip_file.namelist() if name.lower().endswith('.xlsx')]

            if not xlsx_files:
                print("No Excel file found in the ZIP archive.")
            else:
                # Extract the first Excel file found
                xlsx_file_content = zip_file.read(xlsx_files[0])

                # Save the Excel content to a new file
                with open(xlsx_file_name, "wb") as xlsx_file:
                    xlsx_file.write(xlsx_file_content)

                print(f"Excel file '{xlsx_file_name}' extracted and saved successfully.")

                try:
                    # Convert Excel to CSV using pandas
                    df = pd.read_excel(xlsx_file_name)
                    df.to_csv(csv_file_name, index=False, encoding='utf-8')

                    print(f"CSV file '{csv_file_name}' created successfully.")
                except Exception as e:
                    print(f"Error reading or converting Excel file: {e}")
                # Delete the Excel file
                os.remove(xlsx_file_name)
                print(f"Excel file '{xlsx_file_name}' deleted.")
    else:
        print(f"Failed to download the ZIP file. Status code: {response.status_code}")


def import_csv_to_db(final_name):
    try:
        # Read CSV file
        download_and_extract_zip(url, extract_to='.')
        df = pd.read_csv(final_name)

        # Rename columns to match the SQLAlchemy model
        df.rename(columns={
            'InvoiceNo': 'invoiceno',
            'StockCode': 'stockcode',
            'Description': 'description',
            'Quantity': 'quantity',
            'InvoiceDate': 'invoicedate',
            'UnitPrice': 'unitprice',
            'CustomerID': 'customerid',
            'Country': 'country'
        }, inplace=True)

        # Convert InvoiceDate to datetime
        df['invoicedate'] = pd.to_datetime(df['invoicedate'])

        # Insert data into the database
        df.to_sql('transactions', con=engine, if_exists='append', index=False)
        print("Data imported successfully.")

    except SQLAlchemyError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import_csv_to_db(csv_file_name)
