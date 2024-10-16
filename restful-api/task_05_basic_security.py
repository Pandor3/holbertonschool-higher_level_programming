#!/usr/bin/python3
"""
This module will contain techniques for API
Security and authentication techniques
"""

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


if __name__ == '__main__':
    app.run(PORT=5000)
