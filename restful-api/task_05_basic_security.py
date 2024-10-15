#!/usr/bin/python3
"""
This module will contain techniques for API
Security and authentication techniques
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

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
