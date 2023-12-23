import unittest
import sqlite3
import requests
from sqlalchemy.testing import db

from app import create_app
from unittest.mock import patch
from app.models import Transaction


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



if __name__ == '__main__':
    unittest.main()





