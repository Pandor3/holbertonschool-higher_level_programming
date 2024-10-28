#!/usr/bin/python3
"""
This module will be used to contain a simple
API using Python with Flask
"""


import json
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_users(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_new_user():
    data = request.get_json()
    if 'username' not in data or not data['username']:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()