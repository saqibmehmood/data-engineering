import pytest
from app import create_app
from app.models import Transaction, db
from app.utils.constants import INVOICE_DATA, TEST_COUNTRY


@pytest.fixture
def client():
    # Configure the Flask app for testing
    app = create_app({'TESTING': True,
                      'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
                      'SQLALCHEMY_TRACK_MODIFICATIONS': False})

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables in the in-memory database
        yield client

        with app.app_context():
            db.drop_all()  # Drop tables from the in-memory database after the test



def test_calculate_total_sales(client):
    print("1")
    # Test date and country values

    # Add test data to the in-memory database
    with client.application.app_context():
        db.session.add(Transaction(
            invoiceno='10001', stockcode='12345', description='Test Product A', quantity=10,
            invoicedate=INVOICE_DATA, unitprice=20.00, customerid=1, country=TEST_COUNTRY))
        db.session.add(Transaction(
            invoiceno='10002', stockcode='12345', description='Test Product A', quantity=5,
            invoicedate=INVOICE_DATA, unitprice=20.00, customerid=1, country=TEST_COUNTRY))
        db.session.add(Transaction(
            invoiceno='10003', stockcode='67890', description='Test Product B', quantity=3,
            invoicedate=INVOICE_DATA, unitprice=35.00, customerid=2, country=TEST_COUNTRY))
        db.session.commit()
        # Define the expected results
        expected_results = [
            {'stockcode': '12345', 'total_quantity': 15},
            {'stockcode': '67890', 'total_quantity': 3}
        ]

        # Call the API
        response = client.get('/total_sales')
        actual_results = response.get_json()

        # Verify the response status code
        assert response.status_code == 200
        print("###################################################")
        print("data: ", actual_results)
        print("###################################################")
        # Compare actual results with expected results
        # This comparison assumes that the order and structure of the results are consistent
        assert len(actual_results) == len(expected_results)
        for expected, actual in zip(sorted(expected_results, key=lambda x: x['stockcode']),
                                    sorted(actual_results, key=lambda x: x['stockcode'])):
            assert expected['stockcode'] == actual['stockcode']
            assert expected['total_quantity'] == actual['total_quantity']


def test_average_unit_price_per_product(client):
    # Populate the database with test data
    with client.application.app_context():
        db.session.add_all([
            Transaction(stockcode='123', unitprice=10, invoiceno='10001', description='Test Product A', quantity=10,
            invoicedate=INVOICE_DATA, customerid=1, country=TEST_COUNTRY),
            Transaction(stockcode='123', unitprice=20, invoiceno='10001', description='Test Product A', quantity=10,
            invoicedate=INVOICE_DATA, customerid=1, country=TEST_COUNTRY),
            Transaction(stockcode='456', unitprice=30, invoiceno='10001', description='Test Product B', quantity=10,
            invoicedate=INVOICE_DATA, customerid=1, country=TEST_COUNTRY),
            Transaction(stockcode='456', unitprice=40, invoiceno='10001', description='Test Product C', quantity=10,
            invoicedate=INVOICE_DATA, customerid=1, country=TEST_COUNTRY)
        ])
        db.session.commit()

    # Call the API
    response = client.get('/average_unit_price')
    assert response.status_code == 200
    data = response.get_json()

    # Define expected results
    expected_avg_prices = {
        '123': 15.0,  # Average of 10 and 20
        '456': 35.0   # Average of 30 and 40
    }

    # Assert the response matches the expected results
    assert isinstance(data, list)
    for item in data:
        assert item['stockcode'] in expected_avg_prices
        assert abs(item['avg_unit_price'] - expected_avg_prices[item['stockcode']]) < 0.01  # Allowing small rounding differences

@pytest.fixture
def client_actual_db():
    # Configure the Flask app for testing with the actual database
    app = create_app()  # Assuming create_app() without args connects to the actual DB

    with app.test_client() as client:
        yield client

def test_avg_unit_price(client_actual_db):
    """
    Test that avg_unit_price
    """
    response = client_actual_db.get('/average_unit_price')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, dict)
        assert 'stockcode' in item
        assert 'avg_unit_price' in item


def test_top_products(client_actual_db):
    """
    Test that top_products
    """
    response = client_actual_db.get('/total_sales')
    assert response.status_code == 200
    data = response.get_json()  # Use get_json() method
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, dict)
        assert 'stockcode' in item
        assert 'total_quantity' in item








