"""
Database connection.
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


def init_app(app):
    """Initialize app with database"""
    DB.init_app(app)
    Migrate(app, DB)
