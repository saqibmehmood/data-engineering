import os

from app.utils.constants import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False