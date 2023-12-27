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

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd data-engineering
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # for Linux/Mac
    venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add the necessary environment variables:
    ```bash
    DB_USERNAME=<your-username>
    DB_PASSWORD=<your-password>
    DB_HOST=<your-host>
    DB_PORT=<your-port>
    DB_NAME=<your-database-name>
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

4. Start the application:
    ```bash
    python app.py
    ```
5. To run the application using Docker, execute the following command:
    ```bash
    docker-compose up -d
    ```


## Endpoints

### `/top_products_chart`

- **Description**: Displays the top 10 products by total sales.
- **Method**: GET
- **Response**: JSON array containing product details (stock code, description, total quantity).

### `/avg_unit_price_chart`

- **Description**: Represents the trend of average unit price over time.
- **Method**: GET
- **Response**: JSON array containing product details (stock code, description, average unit price).

### `/avg_unit_price_chart.html`

- **Description**: Displays the average unit price chart in HTML format.

### `/avg_unit_price_chart.html`

- **Description**: Displays the average unit price chart in HTML format.



## Testing

The project includes unit tests for the APIs. To run the tests, use the following command:
```bash
pytest tests.py
```

## Dockerization

This application can be containerized using Docker. Use the `Dockerfile` and `docker-compose.yml` provided.

---

## .env Configuration

For configuring environment variables, copy the `.env.example` file and modify the values as needed:

```bash
cp .env.example .env


