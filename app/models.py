from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    invoiceno = db.Column(db.String(10))
    stockcode = db.Column(db.String(15))
    description = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    invoicedate = db.Column(db.TIMESTAMP)
    unitprice = db.Column(db.Numeric(10, 2))
    customerid = db.Column(db.Integer)
    country = db.Column(db.String(50))

