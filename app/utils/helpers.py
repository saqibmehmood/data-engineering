from sqlalchemy import func
from app.models import Transaction
from app import db


def calculate_total_sales():
    """
    Calculates the total sales per stockcode
    :return: list of total sales per stockcode
    """
    total_sales = db.session.query(
        Transaction.stockcode,
        func.sum(Transaction.quantity).label('total_quantity')
    ).group_by(Transaction.stockcode).all()

    result = [{'stockcode': item[0], 'total_quantity': item[1]} for item in total_sales]
    return result


def avg_unit_price_per_product():
    """
    Calculates the average unit per product
    :return: list of the average unit price per product
    """
    avg_prices = db.session.query(
        Transaction.stockcode,
        func.avg(Transaction.unitprice).label('avg_unit_price')
    ).group_by(Transaction.stockcode).all()

    result = [{'stockcode': item[0], 'avg_unit_price': item[1]} for item in avg_prices]

    return result