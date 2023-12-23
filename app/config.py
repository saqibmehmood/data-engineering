import os

# class Config:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# Access the environment variables
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')



class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False