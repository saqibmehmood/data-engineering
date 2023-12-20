from flask import Blueprint, jsonify
from .models import db, Transaction
from sqlalchemy import func

# Blueprint for routes
transactions_bp = Blueprint('transactions', __name__)

# API endpoint to fetch transactions

@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    # Fetch transactions from the database
    transactions = Transaction.query.limit(100).all()

    # Convert transactions to dictionary format
    transactions_list = []
    for transaction in transactions:
        transaction_dict =             {
                'id': transaction.id,
                'invoiceno': transaction.invoiceno,
                'stockcode': transaction.stockcode,
                'description': transaction.description,
                'quantity': transaction.quantity,
                'invoicedate': transaction.invoicedate,
                'unitprice': transaction.unitprice,
                'customerid': transaction.customerid,
                'country': transaction.country
                # Add other fields as needed
            }
        transactions_list.append(transaction_dict)

    return jsonify(transactions_list)


# API endpoint to get total sales per product
@transactions_bp.route('/total_sales', methods=['GET'])
def total_sales_per_product():
    total_sales = db.session.query(
        Transaction.stockcode,
        Transaction.description,
        func.sum(Transaction.quantity).label('total_quantity')
    ).group_by(Transaction.stockcode, Transaction.description).all()

    result = [{'stockcode': item[0], 'description': item[1], 'total_quantity': item[2]} for item in total_sales]

    return jsonify(result)

# API endpoint to get average unit price per product
@transactions_bp.route('/average_unit_price', methods=['GET'])
def average_unit_price_per_product():
    avg_unit_price = db.session.query(
        Transaction.stockcode,
        Transaction.description,
        func.avg(Transaction.unitprice).label('avg_unitprice')
    ).group_by(Transaction.stockcode, Transaction.description).all()

    result = [{'stockcode': item[0], 'description': item[1], 'avg_unitprice': item[2]} for item in avg_unit_price]

    return jsonify(result)