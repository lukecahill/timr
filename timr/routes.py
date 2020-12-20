"""
Handle the routes and registration
"""

from timr.test.test import test_blueprint

def register_routes(app):
    """Register the routes/blueprints"""
    # bot dashboard routes
    app.register_blueprint(
        test_blueprint, url_prefix="/test", strict_slashes=False
    )
