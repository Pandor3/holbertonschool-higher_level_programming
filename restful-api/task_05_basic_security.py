#!/usr/bin/python3
"""
This module will contain various techniques for API
security and authentication techniques
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "Test"
app.config["JWT_SECRET_KEY"] = "Test"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    if user exist in "database"
    """

    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
    return None


@app.route("/login", methods=["POST"])
def user_login():
    """
    new user and return jwt access token
    """

    username = request.json["username"]
    password = request.json["password"]

    user = users.get(username)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify(access_token=access_token), 200


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    if user exist with BasicAuth
    """

    return "Basic Auth: Access Granted", 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    if is a valid jwt token
    """

    return "JWT Auth: Access Granted", 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    if user is a Admin
    """

    if get_jwt_identity()["role"] != "admin":
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted", 200


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
