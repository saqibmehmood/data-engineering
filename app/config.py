import os

from app.utils.constants import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port =os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False