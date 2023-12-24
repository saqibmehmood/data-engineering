from flask import Flask
from .models import db
from .routes import transactions_bp

def create_app(test_config=None):
    app = Flask(__name__)

    # Load default configurations from config.py
    app.config.from_object('app.config.Config')

    # Override with test configuration if provided
    if test_config:
        app.config.update(test_config)

    # Initialize the database
    db.init_app(app)

    # Register the blueprint for routes
    app.register_blueprint(transactions_bp)

    return app
