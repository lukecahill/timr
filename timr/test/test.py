"""
Hold testing routes.
"""

from flask import Blueprint, jsonify

test_blueprint = Blueprint("test_blueprint", __name__)

@test_blueprint.route("", methods=["GET"])
def get():
    """
    Test route
    """
    return jsonify("success")
