from flask import Flask
from .models import db
from .routes import transactions_bp

def create_app():
    app = Flask(__name__)

    # Load configurations from config.py
    app.config.from_object('app.config.Config')

    # Initialize the database
    db.init_app(app)

    # Register the blueprint for routes
    app.register_blueprint(transactions_bp)

    return app
