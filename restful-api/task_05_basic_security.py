#!/usr/bin/python3
"""
This module will contain various techniques for API
security and authentication techniques
"""

import json
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "Test"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("user1"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin1"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Method which will check if a password is correct
    """

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Method which will check if the route is secure
    """

    return ("Basic Auth: Access Granted"), 200


@app.route("/login", methods=["POST"])
def login():
    """
    Method which will identify the user via
    a username and password and give him a
    Json Web Token if the credentials are valid
    """

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Method which will check if a user is authenticated
    via a JSON Web Token
    """

    current_user = get_jwt_identity()
    return ({"JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
def admin_only(username, password):
    """
    Method which will check if a user has the admin role
    and then give him access if the credentials are valid
    """

    if users['role'] != users['admin']:
        return ({"error": "Admin access required"}), 403
    else:
        return ("Admin Access: Granted"), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Method which will return an error message if
    the user have an invalid JWT or doesn't have one
    """

    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Method which will return an error message if
    the user have an invalid JWT
    """

    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Method which will return an error message if
    the JWT has expired
    """

    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Method which will return an error message if
    the JWT has been revoked
    """

    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Method which will return an error message if
    the user have an expired JWT
    """

    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
