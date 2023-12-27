CREATE TABLE IF NOT EXISTS transactions (
    InvoiceNo VARCHAR(10),
    StockCode VARCHAR(255),
    Description VARCHAR(255),
    Quantity INTEGER,
    InvoiceDate TIMESTAMP,
    UnitPrice NUMERIC(10, 2),
    CustomerID INTEGER,
    Country VARCHAR(50)
);



ALTER TABLE transactions
ADD COLUMN id SERIAL PRIMARY KEY;
