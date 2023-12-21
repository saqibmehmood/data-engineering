import unittest
import requests


class TestTransactionAPI(unittest.TestCase):
    url = 'http://localhost:5000/transactions'

    def test_get_all_transactions(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)
        print("Testing get_all_transactions")


class TestTotalSalesAPI(unittest.TestCase):
    url = 'http://localhost:5000/total_sales'

    def test_get_total_sales(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)
        print("Testing total_sales")


class TestAvgUnitPriceAPI(unittest.TestCase):
    url = 'http://localhost:5000/average_unit_price'

    def test_get_average_unit_price(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)
        print("Testing average_unit_price")


class TestTopProductChartAPI(unittest.TestCase):
    url = 'http://localhost:5000/top_products_chart'

    def test_get_top_products_chart(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)
        print("Testing top_products_chart")


class TestAvgUnitPriceChartAPI(unittest.TestCase):
    url = 'http://localhost:5000/avg_unit_price_chart'

    def test_get_top_products_chart(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)
        print("Testing avg_unit_price_chart")

if __name__ == '__main__':
    unittest.main()