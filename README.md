# Data Engineering Project

This project aims to process and visualize the Online Retail dataset using Python, Flask, and PostgreSQL.

## Overview

This application includes SQL analytics, data processing with Python, web reporting, visualization, and Docker containerization.

## Requirements

- Python 3.x
- PostgreSQL
- Docker
- Flask
- Plotly
- Flask-SQLAlchemy
- Pytest

1. Update the `.env` file with required configurations:
    ```bash
    DB_USERNAME=<your-username>
    DB_PASSWORD=<your-password>
    DB_HOST=<your-host>
    DB_PORT=<your-port>
    DB_NAME=<your-database-name>
    ```
## Dockerization
---

To execute this project via Docker, simply run the command provided below in the project's root directory where the Dockerfile and docker-compose.yml files reside. Upon running these commands, the following tasks will be performed:

Setting up the Flask app and the database.
Creation of necessary tables in the database.
Downloading the online retail dataset.
Conversion of the downloaded file into CSV using a script (to facilitate data copying to the table).
Copying data from the CSV file into the table.


Please Note: The file size is fairly large, so please wait a little bit in order to download, convert, and copy the file data to the table.
```
docker-compose up -d
```
If you need to run the project manually(without docker) you can follow the below given steps
    
1. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # for Linux/Mac
    venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```


## Setting Up Database and Importing Data

### Create Table Schema
To begin, create a table named `transactions` using the following SQL command in your preferred SQL query tool:

```sql
CREATE TABLE transactions (
    InvoiceNo VARCHAR(10),
    StockCode VARCHAR(255),
    Description VARCHAR(255),
    Quantity INTEGER,
    InvoiceDate TIMESTAMP,
    UnitPrice NUMERIC(10, 2),
    CustomerID INTEGER,
    Country VARCHAR(50)
);

```

Use the following command to copy the data from your CSV file into the transactions table. Adjust the file path as needed:
Please note: To copy data into the table, ensure your data is in CSV format. Convert a ".xlsx" file into a CSV file before using the \COPY command.

```
\COPY transactions FROM 'path/to/csv file' DELIMITER ',' CSV HEADER;

```
Add Primary Key
To add a primary key named id to the transactions table, execute the following SQL command:
```
ALTER TABLE transactions
ADD COLUMN id SERIAL PRIMARY KEY;

```

2. Start the application:
    ```bash
    python app.py
    ```



## Endpoints

### `/`
- **Description**: Home page containing the links of graphs.
- **Method**: GET


### `/total_sales`

- **Description**: Displays the top 10 products by total sales.
- **Method**: GET
- **Response**: Displays the top 10 products in JSON array.


### `/top_products_chart`

- **Description**: Displays the top 10 products by total sales.
- **Method**: GET
- **Response**: Displays the top 10 products chart in HTML format.



### `/avg_unit_price_chart_overtime`

- **Description**: Represents the trend of average unit price over time.
- **Method**: GET
- **Response**: Displays the average unit price chart in HTML format

### `/avg_unit_price`

- **Description**: JSON array containing product details (stock code, description, average unit price)..

### `/avg_unit_price_chart`

- **Description**: Displays the average unit price chart in HTML format.



## Testing

The project includes unit tests for the APIs. To run the tests, use the following command:
```bash
pytest tests.py
```




