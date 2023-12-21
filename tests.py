import unittest
import requests
from app import create_app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_top_products_chart(self):
        response = self.app.get('/top_products_chart')
        self.assertEqual(response.status_code, 200)
        data = response.json  # Assuming your response is in JSON format
        self.assertIsInstance(data, list)
        if data:
            for item in data:
                self.assertIsInstance(item, dict)
                self.assertIn('stockcode', item)
                self.assertIn('description', item)
                self.assertIn('total_quantity', item)

    def test_avg_unit_price_chart(self):
        response = self.app.get('/avg_unit_price_chart')
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




#
# class TestTransactionAPI(unittest.TestCase):
#     url = 'http://localhost:5000/transactions'
#
#     def test_get_all_transactions(self):
#         resp = requests.get(self.url)
#         self.assertEqual(resp.status_code, 200)
#         print("Testing get_all_transactions")
#
#
# class TestTotalSalesAPI(unittest.TestCase):
#     url = 'http://localhost:5000/total_sales'
#
#     def test_get_total_sales(self):
#         resp = requests.get(self.url)
#         self.assertEqual(resp.status_code, 200)
#         print("Testing total_sales")
#
#
# class TestAvgUnitPriceAPI(unittest.TestCase):
#     url = 'http://localhost:5000/average_unit_price'
#
#     def test_get_average_unit_price(self):
#         resp = requests.get(self.url)
#         self.assertEqual(resp.status_code, 200)
#         print("Testing average_unit_price")
#
#
# class TestTopProductChartAPI(unittest.TestCase):
#     url = 'http://localhost:5000/top_products_chart'
#
#     def test_get_top_products_chart(self):
#         resp = requests.get(self.url)
#         self.assertEqual(resp.status_code, 200)
#         print("Testing top_products_chart")
#
#
# class TestAvgUnitPriceChartAPI(unittest.TestCase):
#     url = 'http://localhost:5000/avg_unit_price_chart'
#
#     def test_get_top_products_chart(self):
#         resp = requests.get(self.url)
#         self.assertEqual(resp.status_code, 200)
#         print("Testing avg_unit_price_chart")
#
# if __name__ == '__main__':
#     unittest.main()