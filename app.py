import os
from flask import Flask, render_template
from app import create_app

if not os.path.exists('.env'):
    raise FileNotFoundError("The .env file is missing. Please create a .env file with necessary configurations.")

app = create_app()



if __name__ == '__main__':
    app.run(debug=True)

