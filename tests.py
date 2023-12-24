import unittest
import pytest
from app import create_app
from app.models import Transaction, db
from datetime import datetime


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_top_products(self):
        """
        Test that top_products
        :return:
        """
        response = self.app.get('/total_sales')
        self.assertEqual(response.status_code, 200)
        data = response.json  # Assuming your response is in JSON format
        self.assertIsInstance(data, list)
        if data:
            for item in data:
                self.assertIsInstance(item, dict)
                self.assertIn('stockcode', item)
                self.assertIn('description', item)
                self.assertIn('total_quantity', item)

    def test_avg_unit_price(self):
        """
        Test that avg_unit_price
        :return:
        """
        response = self.app.get('/average_unit_price')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)
        if data:
            for item in data:
                self.assertIsInstance(item, dict)
                self.assertIn('stockcode', item)
                self.assertIn('description', item)
                self.assertIn('avg_unit_price', item)


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
    test_invoice_date = datetime.strptime('2021-01-01 10:00:00', '%Y-%m-%d %H:%M:%S')
    test_country = 'Testland'

    # Add test data to the in-memory database
    with client.application.app_context():
        db.session.add(Transaction(
            invoiceno='10001', stockcode='12345', description='Test Product A', quantity=10,
            invoicedate=test_invoice_date, unitprice=20.00, customerid=1, country=test_country))
        db.session.add(Transaction(
            invoiceno='10002', stockcode='12345', description='Test Product A', quantity=5,
            invoicedate=test_invoice_date, unitprice=20.00, customerid=1, country=test_country))
        db.session.add(Transaction(
            invoiceno='10003', stockcode='67890', description='Test Product B', quantity=3,
            invoicedate=test_invoice_date, unitprice=35.00, customerid=2, country=test_country))
        db.session.commit()
        # Define the expected results
        expected_results = [
            {'stockcode': '12345', 'description': 'Test Product A', 'total_quantity': 15},
            {'stockcode': '67890', 'description': 'Test Product B', 'total_quantity': 3}
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
            assert expected['description'] == actual['description']
            assert expected['total_quantity'] == actual['total_quantity']

    # print("2")
    # # Call the API and validate the response
    # response = client.get('/total_sales')
    # data = response.get_json()
    # print("3")
    # print("###################################################")
    # print("data: ", data)
    # print("###################################################")
    # # Assertions
    # assert response.status_code == 200
    # assert len(data) == 2
    # assert {'stockcode': '12345', 'description': 'Test Product A', 'total_quantity': 15} in data
    # assert {'stockcode': '67890', 'description': 'Test Product B', 'total_quantity': 3} in data


if __name__ == '__main__':
    unittest.main()





