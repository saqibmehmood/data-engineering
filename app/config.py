import os

# Access the environment variables
# define enviroment variables

class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
