from datetime import datetime
import os

INVOICE_DATA = datetime.strptime('2021-01-01 10:00:00', '%Y-%m-%d %H:%M:%S')
TEST_COUNTRY = 'Testland'

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT =os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
