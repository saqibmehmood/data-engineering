from flask import Blueprint, jsonify
from .models import db, Transaction
import plotly.graph_objs as go
from flask import render_template
from sqlalchemy import func

from .utils.helpers import calculate_total_sales, avg_unit_price_per_product

# Blueprint for routes
transactions_bp = Blueprint('transactions', __name__)

# API endpoint to fetch transactions

@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    """
    Get all transactions
    :return:
    """
    transactions = Transaction.query.limit(1000).all()

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
    """
    Get total sales per product
    :return:
    """
    result = calculate_total_sales()

    return jsonify(result)

# API endpoint to get average unit price per product
@transactions_bp.route('/average_unit_price', methods=['GET'])
def average_unit_price_per_product():
    result = avg_unit_price_per_product()

    return jsonify(result)



@transactions_bp.route('/top_products_chart', methods=['GET'])
def top_products_chart():
    # Fetch data for top 10 products by total sales
    top_products = calculate_total_sales()  # Using the function to get top products

    # Sort the top products by total sales
    top_products = sorted(top_products, key=lambda x: x['total_quantity'], reverse=True)[:10]

    # Extract product names and total sales
    product_names = [product['stockcode'] for product in top_products]
    total_sales = [product['total_quantity'] for product in top_products]

    # Create a Plotly bar chart
    data = [go.Bar(x=product_names, y=total_sales)]
    layout = go.Layout(title='Top 10 Products by Total Sales')
    fig = go.Figure(data=data, layout=layout)

    # Convert Plotly figure to HTML
    chart_div = fig.to_html(full_html=False)

    return render_template('top_products_chart.html', chart_div=chart_div)


@transactions_bp.route('/avg_unit_price_chart', methods=['GET'])
def avg_unit_price_chart():
    # Fetch data for average unit price per product
    avg_unit_prices = avg_unit_price_per_product()  # Using the function to get average unit prices

    # Sort the products by average unit price
    avg_unit_prices = sorted(avg_unit_prices, key=lambda x: x['avg_unit_price'], reverse=True)

    # Extract product names and average unit prices
    product_names = [product['stockcode'] for product in avg_unit_prices]
    avg_prices = [product['avg_unit_price'] for product in avg_unit_prices]

    # Create a Plotly line chart
    data = [go.Scatter(x=product_names, y=avg_prices, mode='lines+markers')]
    layout = go.Layout(title='Average Unit Price Trend')
    fig = go.Figure(data=data, layout=layout)

    # Convert Plotly figure to HTML
    chart_div = fig.to_html(full_html=False)

    return render_template('avg_unit_price_chart.html', chart_div=chart_div)