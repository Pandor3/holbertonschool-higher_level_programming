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
    "user1":
    {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1":
    {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
  }


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    access_token = create_access_tokent(identity=username)
    return jsonify(access_token=access_token)

@auth.verify_password
def verifying_password():
    if username in users and users[username] == password:
        return username
    else:
        return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protection():
    return jsonify({"Basic Auth": "Access Granted"}), 200


if __name__ == '__main__':
    app.run()
