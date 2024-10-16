#!/usr/bin/python3
"""
This module will contain techniques for API
Security and authentication techniques
"""

import json
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "ABC&abc&123"
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
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify("Basic Auth: Access Granted"), 200


@app.route("/login", methods=["POST"])
def login():
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
    current_user = get_jwt_identity()
    return ({"JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
def admin_only(username, password):
    if users['role'] != users['admin1']:
        return ({"error": "Admin access required"}), 403
    else:
        return ("Admin Access: Granted"), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(PORT=5000)
