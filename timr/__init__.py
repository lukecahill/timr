"""
Root init
"""
import logging
import os

from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_wtf.csrf import CSRFProtect

from timr.routes import register_routes
from timr import database


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config["SECURITY_PASSWORD_SALT"] = "ce2f06f6a341e36304d331a64a558b23"

    # usage-specific config overrides
    if test_config:
        app.config.update(test_config)

    init_app(app)
    register_routes(app)

    return app


def init_app(app):
    """Initalize the app post configuration"""
    CSRFProtect(app)
