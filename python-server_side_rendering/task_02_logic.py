#!/usr/bin/python3
"""
This module will be used to create a dynamic content
and use Jinja loops
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            item_data = data.get("items")
    except FileNotFoundError:
        data = []

    return render_template('items.html', items=item_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)