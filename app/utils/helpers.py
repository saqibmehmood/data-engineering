from sqlalchemy import func
from app.models import Transaction
from app import db


def calculate_total_sales():
    total_sales = db.session.query(
        Transaction.stockcode,
        Transaction.description,
        func.sum(Transaction.quantity).label('total_quantity')
    ).group_by(Transaction.stockcode, Transaction.description).all()

    result = [{'stockcode': item[0], 'description': item[1], 'total_quantity': item[2]} for item in total_sales]

    return result


def avg_unit_price_per_product():
    avg_prices = db.session.query(
        Transaction.stockcode,
        Transaction.description,
        func.avg(Transaction.unitprice).label('avg_unit_price')
    ).group_by(Transaction.stockcode, Transaction.description).all()

    result = [{'stockcode': item[0], 'description': item[1], 'avg_unit_price': item[2]} for item in avg_prices]

    return result