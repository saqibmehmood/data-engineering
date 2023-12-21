import os

# Access the environment variables

print("#############################################################")
print("environ: ", os.environ)
print("db_username: ", db_username)
print("db_password: ", db_password)
print("db_host: ", db_host)
print("port: ", db_port)
print("db_name: ", db_name)
print("#############################################################")


class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
